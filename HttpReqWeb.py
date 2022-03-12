from urllib.request import urlopen, Request

url = "https://www.wikipedia.org/"
request = Request(url)
response = urlopen(request)
html = response.read()
response.close()
print(html)
print(response)
print(request)

import requests
url = "https://www.wikipedia.org"
r = requests.get(url)
text = r.text
print(text)
