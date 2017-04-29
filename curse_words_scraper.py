import requests
from bs4 import BeautifulSoup


def slate_curse_scraper():
    # Send off request
    r = requests.get(
        'http://www.slate.com/blogs/lexicon_valley/2013/09/11/top_swear_words_most_popular_curse_words_on_facebook.html')

    # Check if requests status is 200
    if r.status_code == 200:
        print('** {url} IS ONLINE! **'.format(url=r.url))
        # All HTML content
        html = r.text
        # Create soup object
        soup = BeautifulSoup(html, 'lxml')
        # All tables
        tables = soup.find_all('table', {'class': 'interactive_table'})

        # Empty list for cuss words
        cuss_words = list()

        # Loop through all tables
        for table in tables:
            # Store all `tr` tags
            table_row = table.find_all('tr')
            # Loop through `tr` tags
            for table_td in table_row[1:]:
                # Store all `td` tags
                table_data = table_td.find_all('td')
                # Loop through all `td` tags
                for words in table_data:
                    # Add `td` text to list
                    cuss_words.append(words.text)
        # Return completed list
        return cuss_words
    # If no connection was made with URL
    else:
        # If connection was unsuccessful 
        print('** COULD NOT CONNECT TO: {url} **'.format(url=r.url))


def deadspin_curse_scraper():
    # Send off request
    r = requests.get('http://deadspin.com/behold-the-ultimate-curse-word-bracket-457043269')

    # Check if requests status is 200
    if r.status_code == 200:
        print('** {url} IS ONLINE! **'.format(url=r.url))
        # All HTML content
        html = r.text
        # Create soup object
        soup = BeautifulSoup(html, 'lxml')
        # Find all `ol` tags
        ol = soup.find_all('ol')

        # Empty cuss_words list
        cuss_words = list()

        # Loop through all `ol` tags
        for elem in ol:
            # Store all `li` tags
            li_data = elem.find_all('li')
            # Loop through all `li` tags
            for li in li_data:
                # Append words to list
                cuss_words.append(li.text)
        # Return completed list
        return cuss_words
    # If no connection was made with URL
    else:
        # If connection was unsuccessful
        print('** COULD NOT CONNECT TO: {url} **'.format(url=r.url))


def parse_list(l):
    # Loop through list
    for word in l:
        # Check if strings are numbers or capitalized
        if word.istitle() or word.isdigit():
            # Remove strings if matching criterion
            l.remove(word)
    # Make all words lowercase
    lowered_l = [x.lower() for x in l]
    # Store list inside of set to remove doubles
    completed_set = set(filter(None, lowered_l))
    # Return filtered list/set
    return completed_set


if __name__ == '__main__':
    # Slate.com Words
    slate_unfiltered_list = slate_curse_scraper()
    slate_filtered_set = parse_list(slate_unfiltered_list)
    # Deadspin.com Words
    deadspin_unfiltered_list = deadspin_curse_scraper()
    deadspin_filtered_set = parse_list(deadspin_unfiltered_list)
    # Combine both sets together to remove doubles
    complete_cuss_set = slate_filtered_set.union(deadspin_filtered_set)
