import requests

API_KEY = "5c0c7564c591168c52d740f8623cc43e"

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params, timeout=10)

    if response.status_code == 200:
        data = response.json()

        print("\n--- WEATHER REPORT ---")
        print("City:", data["name"])
        print("Temperature:", data["main"]["temp"], "°C")
        print("Humidity:", data["main"]["humidity"], "%")
        print("Weather:", data["weather"][0]["description"].title())

    else:
        print("Unable to get weather data.")
        print("Error:", response.json().get("message", "Unknown error"))

except requests.exceptions.RequestException:
    print("Network error. Check your internet connection.")