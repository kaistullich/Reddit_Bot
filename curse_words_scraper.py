import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.slate.com/blogs/lexicon_valley/2013/09/11/top_swear_words_most_popular_curse_words_on_facebook.html')

def scraper():
    # Check if requests status is 200
    if r.status_code == 200:
        print('** Website Online **')
        # All HTML content
        html = r.text
        soup = BeautifulSoup(html, 'lxml')
         # All tables
        tables = soup.find_all('table', {'class': 'interactive_table'})

        # Empty set for cuss words
        cuss_words = list()

        # Loop through all tables
        for table in tables:
            # Store all `tr` tags
            table_row = table.find_all('tr')
            # Loop through `tr` tags
            for table_td in table_row:
                # Store all `td` tags
                table_data = table_td.find_all('td')
                # Loop through all `td` tags
                for words in table_data:
                    # Add `td` text to set
                    cuss_words.append(words.text)

        return cuss_words

    else:
        print('Connection not successful with URL')

def parse_set(l):
    for word in l:
        # word = word.strip('+-')
        if word.istitle() or word.isdigit():
            l.remove(word)

    completed_set = list(filter(None, l))

    return completed_set


if __name__ == '__main__':
    unfiltered_set = scraper()
    filtered_set = parse_set(unfiltered_set)

    print(filtered_set)

    # Full Set
    # cuss_words = {'', '9', 'Britain', '11', 'South', '10', '20', '45-54', 'fag', 'crap', 'bugger', 'shit', 'Canada',
    #               '25-34', 'West', '7', '18-24', '17', '13', 'damn', 'bollocks', 'douche', 'pussy', '13-17', 'Both',
    #               'Female', '19', 'asshole', '14', 'bloody', 'Male', 'dick', 'darn', '18', '5', '12', 'cunt', '35-44',
    #               'cock', '4', '1', '2', '3', 'slut', 'Midwest', 'U.S.', '16', 'arsehole', 'fuck', '6', '55+', 'bitch',
    #               '15', 'bastard', 'piss', 'Australia', '8', 'Northeast'
    #               }
