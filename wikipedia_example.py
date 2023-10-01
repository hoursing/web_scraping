import requests
from bs4 import BeautifulSoup

url = 'https://en.wikipedia.org/w/index.php' + \
    '?title=List_of_Game_of_Thrones_episodes&oldid=802553687'

response = requests.get(url)
html_contents = response.text

html_soup = BeautifulSoup(html_contents, 'html.parser')

# print(html_soup.find('h1'))
# print(html_soup.find('', {'id': 'p-logo'}))
# for found in html_soup.find_all(['h1', 'h2']):
#     print(found)
# print(html_soup)

# We'll use a list to store our episode list
episodes = []
ep_tables = html_soup.find_all('table', class_='wikiepisodetable')
print(ep_tables)

for table in ep_tables:
    headers = []
    rows = table.find_all('tr')

    # Start by fetching the header cells from the first row to determine
    # The field names
    for header in table.find('tr').find_all('th'):
        headers.append(header.text)
    # Then go though all the rows except the first one
    for row in table.find('tr'):
        values = []
        # And get the column cells, the first one being inside a th-tag
        for col in row.find_all(['th','td']):
            values.append(col.text)
        if values:
            episode_dict = {headers[i]: values[i] for i in range(len(values))}
            episodes.append(episode_dict)
# Show result
for episode in episodes:
    print(episode)
