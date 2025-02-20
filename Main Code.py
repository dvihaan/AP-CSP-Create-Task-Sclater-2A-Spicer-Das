import requests 

def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['current_weather']['temperature']
        weatherCode = data['current_weather']['weathercode']
        return temperature, weatherCode
    else: 
        return None

def displayWeather(latitude, longitude):
    temperature, weatherCode = get_weather(latitude, longitude)
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
        print(f"{temperature}°C, {weatherDict[weatherCode]}")
    else:
        print("API request failed")

def getCoords(city):
    url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    response = requests.get(url)
    if response.status_code == 200:
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
    cityName = input("Enter city name: ")
    latitude, longitude = getCoords(cityName)
    displayWeather(latitude, longitude)

if __name__ == "__main__":
    main()