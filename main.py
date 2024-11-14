from tkinter import *
from location import LocationService
from weather import WeatherService

class Main:
    def __init__(self):
        self.city = ''
        self.latitude = None
        self.longitude = None
        self.weather_data = None

    def get_weather(self):
        print("yow")


if __name__ == "__main__":

    main = Main()


    root = Tk()
    root.title("Weather App")
    root.geometry('400x400')

    root.config(bg='#243642')

    # Button to trigger the HTTPS call
    btn = Button(root, text="Get Weather", command=main.get_weather())
    btn.pack()

    root.mainloop()