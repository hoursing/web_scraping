import requests

url = 'http://www.webscrapingfordatascience.com/basichttp/'
request = requests.get(url)

print("#Status code")
print(request.status_code)
print('#reason')
print(request.reason)
print('#headers')
print(request.headers)
print('#request')
print(request.request)
print('#request.headers')
print(request.request.headers)
print('#request.text')
print(request.text)