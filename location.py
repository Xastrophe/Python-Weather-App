import requests

class LocationService:
    def __init__(self, url='https://ipinfo.io/json'):
        self.url = url
    
    def get_current_coords(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()
        location = data['loc'].split(',')
        latitude = float(location[0])
        longitude = float(location[1])
        return latitude, longitude
    
    def get_current_location_data(self):
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        return data['city'], data['region'], data['country'], data['timezone']
    
if __name__ == '__main__':
    location = LocationService()
    lat, long = location.get_current_coords()
    print(f"Latitude: {lat}, Longitude: {long}")
    city, region, country, timezone = location.get_current_location_data()
    print(f"City: {city}, Region: {region}, Country: {country}, Timezone: {timezone}")