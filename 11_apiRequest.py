import requests

response = requests.get('http://api.open-notify.org/astros.json')

json = response.json()

for persons in json['people']:
    print(persons['name'])


# {
#    "message":"success",
#    "number":11,
#    "people":[
#       {
#          "name":"Raja Chari",
#          "craft":"ISS"
#       },
#       {
#          "name":"Tom Marshburn",
#          "craft":"ISS"
#       },
#       {
#          "name":"Kayla Barron",
#          "craft":"ISS"
#       },
#       {
#          "name":"Matthias Maurer",
#          "craft":"ISS"
#       },
#       {
#          "name":"Oleg Artemyev",
#          "craft":"ISS"
#       },
#       {
#          "name":"Denis Matveev",
#          "craft":"ISS"
#       },
#       {
#          "name":"Sergey Korsakov",
#          "craft":"ISS"
#       },
#       {
#          "name":"Kjell Lindgren",
#          "craft":"ISS"
#       },
#       {
#          "name":"Bob Hines",
#          "craft":"ISS"
#       },
#       {
#          "name":"Samantha Cristoforetti",
#          "craft":"ISS"
#       },
#       {
#          "name":"Jessica Watkins",
#          "craft":"ISS"
#       }
#    ]
# }