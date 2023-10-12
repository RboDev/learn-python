from dataclasses import dataclass
from typing import Any
import requests

import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OWE_API_KEY")

import asyncio

type WeatherForecast =  dict[str, Any]


@dataclass
class UrlTemplateClient:
    template: str

    def get(self, data: WeatherForecast) -> Any:
        url = self.template.format(**data)
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise an exception if the request failed
        return response.json()


class CityNotFoundError(Exception):
    pass


async def get_capital(country: str) -> str:
    client = UrlTemplateClient(template="https://restcountries.com/v3/name/{country}")
    response = await client.get({"country": country})

    # The API can return multiple matches, so we just return the capital of the first match
    return response[0]["capital"][0]


async def get_forecast(city: str) -> WeatherForecast:
    client = UrlTemplateClient(
        template=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=123456789"
    )
    response = await client.get({"city": city})
    if "main" not in response:
        raise CityNotFoundError(
            f"Couldn't find weather data. Check '{city}' if it exists and is correctly spelled.\n"
        )
    return response


def get_temperature(full_weather_forecast: WeatherForecast) -> float:
    temperature = full_weather_forecast["main"]["temp"]
    return temperature - 273.15  # convert from Kelvin to Celsius

async def get_country_weather(country:str) -> tuple[str,WeatherForecast]:
    capital = await get_capital(country)
    print(f"The capital of {country} is {capital}")
    weather_forecast = await get_forecast(capital)
    print(f"The current temperature in {capital} is {get_temperature(weather_forecast):.1f} °C.")
    return capital, weather_forecast



async def main() -> None:
    countries = ["United States of America", "Australia", "Japan", "France", "Brazil"]


    tasks = [asyncio.create_task(get_country_weather(country)) for country in countries]

    await asyncio.gather(*tasks)

    # print 


    #     print(f"The capital of {country} is {capital}")

    #     weather_forecast = await get_forecast(capital)
    #     print(
    #         f"The current temperature in {capital} is {get_temperature(weather_forecast):.1f} °C."
    #     )


if __name__ == "__main__":
    asyncio.run(main())
