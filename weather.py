import json

import requests

key_weather = ""  # your API keys Weather
# API website : https://openweathermap.org/current
# API response need coord lat and lng from website GEO

class Response_Weather:
    def __init__(self, data):
        self.data = data
        self.response = requests.get(f"https://api.openweathermap.org/data/2.5/"
                                     f"weather?lat={self.data[0]}&lon={self.data[1]}&appid={key_weather}"
                                     f"&units=metric")
        self.response_main = self.response.json()
        self.temp()

    def temp(self):
        with open("weather.json", 'w') as file:
            file_ = json.dumps(self.response_main, indent=4)
            file.write(file_)
        return self.response_main

    def main(self):
        return self.response_main['main']

    def weather(self):
        return self.response_main['weather'][0]['main']

    def temp_main(self):
        return self.response_main['main']['temp']

    def temp_description(self):
        return self.response_main['weather'][0]['description']

    def feels_like(self):
        return self.response_main["main"]["feels_like"]

    def presure(self):
        return  self.response_main['main']['pressure']

    def wind(self):
        return self.response_main['wind']['speed']

    def clouds(self):
        return self.response_main['clouds']['all']

