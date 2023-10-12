"""
Usage:
    main.py CITY [--api_key=<KEY>]
    main.py CITY [-t | -w | -h]


Get the current weather information for a city

Arguments:
    CITY                Name of the city to get the weather information for

Options:
    --help              Show this screen
    -t --temperature    Show the temperature in °C for the city
    -w --wind           Show the wind direction and speed
    -h --humidity       Show the hunidity in %
    -a --all            Show temperature, wind and humidity
    -k --api_key=KEY        Your OpenWeather API KEY
"""


from typing import Any
from docopt import docopt

from dotenv import load_dotenv
import os

load_dotenv()
API_KEY=os.getenv("OWE_API_KEY")


from weather import (
    get_complete_forecast,
    http_get,
    get_temperature,
    get_humidity,
    get_wind_speed,
    get_wind_direction,
)




def parse(args:dict[str,Any]):
    city = args['CITY']

    api_key = args['--api_key']
    if not api_key: api_key = API_KEY

    opt_temp = args['--temperature']
    opt_humid = args['--humidity']
    opt_wind = args['--wind']

    # No option choosen so we want all
    if not any([opt_humid,opt_temp,opt_wind]):
        opt_wind = opt_humid = opt_temp = True

    weather_forecast = get_complete_forecast(http_get_fn=http_get, api_key=api_key, city=city)

    temperature = get_temperature(weather_forecast)
    humidity = get_humidity(weather_forecast)
    wind_speed = get_wind_speed(weather_forecast)
    wind_dir = get_wind_direction(weather_forecast)

    print(f"The weather for {city}:")
    if opt_temp:
        print(f"The current temperature is {temperature:.1f} °C.")

    if opt_humid:
        print(f"The current humidity is {humidity}")

    if opt_wind:
        print(
            f"The current wind speed is {wind_speed} m/s "
            f"from direction {wind_dir} degrees."
        )


if __name__ == "__main__":
    args = docopt(__doc__)
    parse(args)


