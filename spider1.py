import requests

url = 'http://books.toscrape.com/'
resp = requests.get(url)
print(resp.status_code)
resp.encoding = resp.apparent_encoding
print(resp.text[:300])
