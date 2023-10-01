import requests

url = 'https://en.wikipedia.org/w/index.php' + \
    '?title=List_of_Game_of_Thrones_episodes&oldid=802553687'

response = requests.get(url)
html_contents = response.text

print(response.text)