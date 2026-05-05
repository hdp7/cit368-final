import requests
import sqlite3

#API key should be encrypted, not in plain text
API_KEY = "VEhpcyBpcyBhIGZha2Uga2V5LCBidXQgbWF5YmUgbG9va3MgbGlrZSBvbmU="
#URL should be stored elsewhere (ex. a secrets file)
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
DB = None

def get_weather(city):
    
    #insert a validation function for the city here
    
    params = {
        "q": city,
        "appid": API_KEY,
    }

    response = requests.get(BASE_URL, params=params)

    #collect from 3rd party API
    data = response.json()
    
    city_name = data["name"]
    temp = data["main"]["temp"]

    #insert into DB
    #This should be handle by another file
    c = DB.cursor()
    c.execute("INSERT INTO history (city, temp) VALUES (" + city_name +", " + temp + ")")
    DB.commit()

    print(f"\nWeather in " + city)
    print(f"Temperature: {temp}°C")
    
if __name__ == "__main__":
    DB = sqlite3.connect("weather.db")
    
    #collect from user
    city = input("Enter city name: ")
    #Input should be validated before being used
    get_weather(city)