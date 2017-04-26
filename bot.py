import praw
import pdb
import re
import os

reddit = praw.Reddit('bot1')

subreddit = reddit.subreddit('pythonforengineers')

# If `.txt` file is not created, create empty list
# This statement only get executed on the first time the script is run
if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []

# If `posts_replied_to.txt` file exits
else:
    # Open file
    with open("posts_replied_to.txt", "r") as f:
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
            submission.reply("Donald Trump says: SAD!")
            # Console log which post was replied to
            print("Bot replying to : ", submission.title)
            # Append post ID to list
            posts_replied_to.append(submission.id)

# Open txt file
with open("posts_replied_to.txt", "w") as f:
    # Loop through list
    for post_id in posts_replied_to:
        # Write post ID's to txt file
        f.write(post_id + "\n")