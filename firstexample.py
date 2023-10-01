import requests

url = 'http://www.webscrapingfordatascience.com/basichttp/'
request = requests.get(url)

print(request.text)