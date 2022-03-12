import requests

url = 'http://www.omdbapi.com/?i=tt3896198&apikey=a7b3eb50'
r = requests.get(url)
json_data = r.json()
for key, value in json_data.items():
    print(key + ":", value)
