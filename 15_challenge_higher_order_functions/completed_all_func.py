from typing import Any, Callable, Protocol

import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OWE_API_KEY")


class CityNotFoundError(Exception):
    pass


def get(url: str) -> dict[str, Any]:
    response = requests.get(url, timeout=5)
    return response.json()


def get_forecast(city: str, api_key: str, getter: Callable[[str], dict[str, Any]]) -> dict[str, Any]:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = getter(url)
    if "main" not in response:
        raise CityNotFoundError(
            f"Couldn't find weather data. Check '{
                city}' if it exists and is correctly spelled.\n"
        )
    return response


def temperature(full_weather_forecast: dict[str, Any]) -> float:
    temperature = full_weather_forecast["main"]["temp"]
    return temperature - 273.15  # convert from Kelvin to Celsius


def humidity(full_weather_forecast: dict[str, Any]) -> int:
    return full_weather_forecast["main"]["humidity"]


def wind_speed(full_weather_forecast: dict[str, Any]) -> float:
    return full_weather_forecast["wind"]["speed"]


def wind_direction(full_weather_forecast: dict[str, Any]) -> int:
    return full_weather_forecast["wind"]["deg"]


def main() -> None:
    city = "Tempe"

    weather = get_forecast(city, api_key=API_KEY, getter=get)

    print(f"The current temperature in {city} is {temperature(weather): .1f} °C.")
    print(f"The current humidity in {city} is {humidity(weather)}%.")
    print(
        f"The current wind speed in {city} is {wind_speed(weather)} m/s "
        f"from direction {wind_direction(weather)} degrees."
    )


if __name__ == "__main__":
    main()
