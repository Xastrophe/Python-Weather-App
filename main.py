import sys
import os
from tkinter import Tk, Button
from location import LocationService
from weather import WeatherService

# Add the paths to the sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))

from ui.box1 import Box1
from ui.box2 import Box2

class Main:
    def __init__(self):
        self.city = ''
        self.latitude = None
        self.longitude = None
        self.weather_data = None
        self.root = Tk()

        #____INITIALIZE UI____#
        self.root.title("Weather App")
        self.root.geometry('1000x1000')
        self.root.config(bg='#081226')

        self.create_widgets()

    def create_widgets(self):
        self.box1 = Box1(self.root, 200, 200)
        self.box1.pack(pady=10)

        self.box2 = Box2(self.root, 200, 200)
        self.box2.pack(pady=10)

        self.get_weather_button = Button(self.root, text="Get Weather", command=self.get_weather)
        self.get_weather_button.pack(pady=10)

    def get_weather(self):
        print("Fetching weather data...")

if __name__ == "__main__":
    main = Main()
    main.root.mainloop()