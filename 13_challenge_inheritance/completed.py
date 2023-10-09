from typing import Any

import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OWE_API_KEY")

class CityNotFoundError(Exception):
    pass


class WeatherService:
    def __init__(self, api_key: str) -> None:
        self.api_key = api_key

    def retrieve_forecast(self, city:str) -> dict[str, Any]:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}"
        response = requests.get(url, timeout=5).json()
        if "main" not in response:
            raise CityNotFoundError(
                f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n"
            )

        return response

    def get_temperature_celsius(self, forecast:dict[str, Any]) -> float:
        return forecast["main"]["temp"] - 273.15

class MyWeatherService:
    def __init__(self, weather_service: WeatherService) -> None:
        self.service = weather_service

    def retrieve_forecast(self, city:str = "Paris") -> None:
        forecast = self.service.retrieve_forecast(city)
        # print the temperature in Celsius
        temp = self.service.get_temperature_celsius(forecast)
        print(f"The current temperature in {city} is {temp:.1f} °C.")


if __name__ == "__main__":
    weather_svc = WeatherService(API_KEY)
    my_weather_svc = MyWeatherService(weather_svc)
    my_weather_svc.retrieve_forecast()

