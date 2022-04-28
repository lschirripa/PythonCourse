import requests

response = requests.get('http://api.open-notify.org/astros.json')

json = response.json()

for persons in json['people']:
    print(persons['name'])