import requests
import sqlite3

#API key should be stored in a secrets file and gitignored
API_KEY = "VEhpcyBpcyBhIGZha2Uga2V5LCBidXQgbWF5YmUgbG9va3MgbGlrZSBvbmU="
#https should be used instead of http for secure protocol
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
DB = None

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
    }

    response = requests.get(BASE_URL, params=params)

    #collect from 3rd party API
    #data from a 3rd party API needs to be sanitized and validated
    #There should not be any kind of SQL statements in anything being returned (see below)
    data = response.json()
    
    #city name should only be able to have letters and should not exceed certain number of characters
    city_name = data["name"]
    #temperature should only be able to be numbers and "-" sign. Numbers should not exceed 3 character or none at all
    temp = data["main"]["temp"]

    #insert into DB
    c = DB.cursor()
    #this data has not been validated yet and is being inserted directly into SQL
    #city name and temp are both values that are from an external party, it needs validated
    #a fix would be to use prepared statements
    c.execute("INSERT INTO history (city, temp) VALUES (" + city_name +", " + temp + ")") #VALUES (?, ?)
    DB.commit()

    print(f"\nWeather in " + city)
    print(f"Temperature: {temp}°C")
    
if __name__ == "__main__":
    DB = sqlite3.connect("weather.db")
    
    #collect from user
    #input from the user should be validated and sanitized as well
    #city name should only be able to have letters and should not exceed a certain number of character
    city = input("Enter city name: ")
    get_weather(city)