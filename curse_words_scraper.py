import requests
from bs4 import BeautifulSoup

r = requests.get(
    'http://www.slate.com/blogs/lexicon_valley/2013/09/11/top_swear_words_most_popular_curse_words_on_facebook.html')


def scraper():
    # Check if requests status is 200
    if r.status_code == 200:
        print('** Website Online **')
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

        return cuss_words

    else:
        print('Connection not successful with URL')


def parse_set(l):
    # Loop through list
    for word in l:
        # Check if strings are numbers or capitalized
        if word.istitle() or word.isdigit():
            # Remove strings if matching criterion
            l.remove(word)
    # Store list inside of set to remove doubles
    completed_set = set(filter(None, l))
    # Return filtered list/set
    return completed_set


if __name__ == '__main__':
    unfiltered_set = scraper()
    filtered_set = parse_set(unfiltered_set)
