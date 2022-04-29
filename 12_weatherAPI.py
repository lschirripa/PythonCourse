import requests

def get_api_info():
    api_key = "7939dab06210394b8dfd6c750c368799"

    city_name = 'villa urquiza'

    api_url = "https://api.openweathermap.org/data/2.5/weather?q="+city_name+"&appid="+api_key+"&units=metric" 
    #OLD API URL: "https://api.openweathermap.org/data/2.5/weather?lat="+lat+"&lon="+lon+"&appid="+api_key 
    #lat = str(28.538336)
    #lon = str(-81.379234)

    request = requests.get(api_url)
    json = request.json()

    description = json.get("weather")[0].get("description")
    temp = str(json.get("main").get("temp"))
    tempMAX = str(json.get("main").get("temp_max"))
    tempMIN = str(json.get("main").get("temp_min"))

    return {
                'description' : description,
                 'temp' : temp,
                 'tempMAX' : tempMAX,
                 'tempMIN' : tempMIN    
            
    }

def main():
    
    api_info = get_api_info()
    
    print("Today's forecast is " + api_info.get('description'))
    print("TEMP for today is " + api_info.get('temp'))
    print("the MAX temp is " + api_info.get('tempMAX'))
    print("the MIN temp is " + api_info.get('tempMIN'))

main()
