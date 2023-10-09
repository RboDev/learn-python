from typing import Any

import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OWE_API_KEY")


class CityNotFoundError(Exception):
    pass

class RequestsClient:
    def __init__(self, api_key:str) -> None:
        self.api_key = api_key

    def fetch(self, city:str):
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={self.api_key}"
        response = requests.get(url, timeout=5).json()
        if "main" not in response:
            raise CityNotFoundError(
                f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n"
            )
        return response


class WeatherService:
    def __init__(self, client: RequestsClient) -> None:
        self.client = client
        self.full_weather_forecast: dict[str, Any] = {}

    def retrieve_forecast(self, city: str) -> None:
        response = self.client.fetch(city)
        self.full_weather_forecast = response


def main() -> None:
    city = "Utrecht"

    client = RequestsClient(api_key = API_KEY)
    service = WeatherService(client)
    service.retrieve_forecast(city=city)
    temp = service.full_weather_forecast["main"]["temp"]
    hum = service.full_weather_forecast["main"]["humidity"]
    wind_speed = service.full_weather_forecast["wind"]["speed"]
    wind_direction = service.full_weather_forecast["wind"]["deg"]
    print(f"The current temperature in {city} is {temp:.1f} °C.")
    print(f"The current humidity in {city} is {hum}%.")
    print(
        f"The current wind speed in {city} is {wind_speed} m/s from direction {wind_direction} degrees."
    )


if __name__ == "__main__":
    main()
