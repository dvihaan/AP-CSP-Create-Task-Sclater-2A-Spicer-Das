import requests #Library required for using APIs

def getWeather(latitude, longitude):
    #Set up the API request URL
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200: #Check if the request was successful
        #Extract the temperature and weather code from the API response
        data = response.json()
        temperature = data['current_weather']['temperature']
        weatherCode = data['current_weather']['weathercode']
        return temperature, weatherCode
    else: 
        return None

def displayWeather(latitude, longitude):
    temperature, weatherCode = getWeather(latitude, longitude) #Get the temperature and weather code at a certain location
    #Dictionary mapping weather codes to descriptions
    weatherDict = {
        0: "Clear skies",
        1: "Mostly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Depositing rime fog",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Heavy drizzle",
        56: "Light freezing drizzle",
        57: "Heavy freezing drizzle",
        61: "Light rain",
        63: "Moderate rain",
        65: "Heavy rain",
        66: "Light freezing rain",
        67: "Heavy freezing rain",
        71: "Light snow fall",
        73: "Moderate snow",
        75: "Heavy snow",
        77: "Hail",
        80: "Light showers",
        81: "Moderate showers",
        82: "Violent rain",
        85: "Light snow",
        86: "Heavy snow",
        95: "Light thunderstorm",
        96: "Moderate thunderstorm",
        99: "Heavy thunderstorm"
    }
    if temperature is not None:
        #Print the temperature and weather description
        print(f"{temperature}°C, {weatherDict[weatherCode]}")
    else:
        print("API request failed")

def getCoords(city):
    #Set up the API request URL
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(url)
    if response.status_code == 200: #Check if API request was successful
        #Extract latitude and longitude from the API response
        data = response.json()
        if data['results']:
            latitude = data['results'][0]['latitude']
            longitude = data['results'][0]['longitude']
            return latitude, longitude
        else:
            return None, None
    else:
        return None, None

def main():
    cont = True
    while cont:
        cityName = input("Enter city name: ")
        latitude, longitude = getCoords(cityName)
        if latitude is not None:
            displayWeather(latitude, longitude)
        else:
            print("City not found")
        cont = input("Do you want to check the weather for another city? (y/n) ") == "y"

if __name__ == "__main__":
    main()