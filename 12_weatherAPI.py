import requests

api_key = "7939dab06210394b8dfd6c750c368799"
lat = str(28.538336)
lon = str(-81.379234)
city_name = 'villa urquiza'
api_url = "https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key+"&units=metric" 

#OLD API URL: "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+api_key

request = requests.get(api_url)

json = request.json()

description = json.get("weather")[0].get("description")
temp = str(json.get("main").get("temp"))
tempMAX = str(json.get("main").get("temp_max"))
tempMIN = str(json.get("main").get("temp_min"))

print("Today's forecast is " + description)
print("TEMP for today is " + temp)
print("the MAX temp is " +tempMAX)
print("the MIN temp is " +tempMIN)

