import requests
import json

class WeatherService:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        self.weather_data = {}
        self.url = f'https://api.open-meteo.com/v1/forecast?latitude={self.latitude}&longitude={self.longitude}&hourly=temperature_2m'

    def get_current_weather(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            weather_data = response.json()
            self.weather_data = weather_data  # Directly assign the JSON object
        except requests.exceptions.HTTPError as http_err: 
            print(f"HTTP error occurred: {http_err}")
        
        except json.JSONDecodeError as json_err:
            print(f"JSON decode error occurred: {json_err}")
        
        except Exception as err:
            print(f"Other error occurred: {err}")



    def get_time_temp(self):

        time_temp = []
        
        for i in range(len(self.weather_data["hourly"]["time"])):
            time_temp.append((self.weather_data["hourly"]["time"][i], self.weather_data["hourly"]["temperature_2m"][i]))
            
        return time_temp
    
    def get_timezone(self):
        return self.weather_data["timezone"]
    
    def long_lat(self):
        return self.weather_data["longitude"], self.weather_data['latitude']


if __name__ == '__main__':
    weather = WeatherService(10.3167, 123.8907)
    data = weather.get_current_weather()
    print(weather.get_weather_info())
