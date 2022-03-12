import json

with open('snakes-on-plane.json', 'r') as json_file:
    json_data = json.load(json_file)

for key, value in json_data.items():
    print(key + ':', value)
