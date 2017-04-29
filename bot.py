# Subbredit: https://www.reddit.com/r/pythonforengineers

import json
import logging
import os
import random
import re
import time
import sys

import praw

from praw.exceptions import APIException
from quotes import quote_replies

# Logging file
logging.basicConfig(filename='logfile.log', format='\n%(asctime)s %(message)s', level=logging.ERROR)


# Setup for errors
def error_handling():
    return ('\n{}. {}, @ line: {}'.format(sys.exc_info()[0],
                                          sys.exc_info()[1],
                                          sys.exc_info()[2].tb_lineno))
# Config file
with open('config.json') as f:
    config = json.load(f)

# Create `reddit` PRAW object
reddit = praw.Reddit(user_agent=config['user_agent'],
                     client_id=config['client_id'],
                     client_secret=config['client_secret'],
                     username=config['username'],
                     password=config['password']
                     )

# Subreddit tot target
subreddit = reddit.subreddit('pythonforengineers')

# If `.txt` file is not created, create empty list
# This statement only get executed on the first time the script is run
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If `posts_replied_to.txt` file exits
else:
    # Open file
    with open("posts_replied_to.txt") as f:
        # Read file contents
        posts_replied_to = f.read()
        # Split on new lines
        posts_replied_to = posts_replied_to.split("\n")
        # If list contains empty values remove
        posts_replied_to = list(filter(None, posts_replied_to))

# Loop through `hot` posts (limit to 5)
for submission in subreddit.new(limit=5):
    # Check if post ID is inside of file already
    if submission.id not in posts_replied_to:
        # Check title of post contains `i love python`
        if re.search("i love python", submission.title, re.IGNORECASE):
            # Reply to post
            try:
                submission.reply('Useless Quote Bot: ' + random.choice(quote_replies))
            except APIException:
                logging.error(error_handling())
            # Console log which post was replied to
            print("Bot replying to : ", submission.title)
            # Append post ID to list
            posts_replied_to.append(submission.id)
            # Temporary `Rate limit` fix: TODO adjust this
            time.sleep(5)

# Open txt file
with open("posts_replied_to.txt", "w") as f:
    # Loop through list with Post IDs
    for post in posts_replied_to:
            # Write Post IDs to txt file
            f.write(post + '\n')
