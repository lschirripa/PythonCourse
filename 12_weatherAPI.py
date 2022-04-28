import requests

api_key = "7939dab06210394b8dfd6c750c368799"
lat = str(28.538336)
lon = str(-81.379234)
city_name = 'orlando'
api_url = "https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key

#OLD API URL: "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+api_key

request = requests.get(api_url)

json = request.json()

print(json)