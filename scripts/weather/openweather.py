import json
import os
import urllib.request

from utils.check_unit import check_unit
from utils.getcity import getcity
from utils.iso3 import iso3
from utils.parser import args


# This API KEY is for my personal usage.
# Please get your own API KEY here https://openweathermap.org/api,
# and set an environment variable for OPENWEATHER_API_KEY with your API KEY.
API_KEY = "970606528befaa317698cc75083db8b2"
OPENWEATHER_API_KEY = (
    args.api_key[0] if args.api_key else os.environ.get("OPENWEATHER_API_KEY", API_KEY)
)
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

CITY_NAME = args.city[0] if args.city else getcity()
LANG = args.lang[0] if args.lang else "en"
UNIT = args.unit[0] if args.unit else "metric"


def openweather(city=CITY_NAME, lang=LANG, unit=UNIT, api_key=OPENWEATHER_API_KEY):
    try:
        request = urllib.request.urlopen(
            f"{OPENWEATHER_URL}?q={city.replace(' ', '+')}&lang={lang}&units={unit}&appid={api_key}"
        )
        if request.getcode() == 200:
            data = json.loads(request.read())

            _id = data["id"]
            name = data["name"]
            timezone = data["timezone"]
            country = data["sys"]["country"]
            sunrise = data["sys"]["sunrise"]
            sunset = data["sys"]["sunset"]

            temp = data["main"]["temp"]
            temp_min = data["main"]["temp_min"]
            temp_max = data["main"]["temp_max"]
            humidity = data["main"]["humidity"]
            feels_like = data["main"]["feels_like"]
            description = data["weather"][0]["description"]

            country = iso3().get(country)
            unit = check_unit(unit)

            weather_info = {
                "id": _id,
                "timezone": timezone,
                "city_name": name,
                "country": country,
                "sunrise": sunrise,
                "sunset": sunset,
                "temp": temp,
                "temp_min": temp_min,
                "temp_max": temp_max,
                "feels_like": feels_like,
                "description": description,
                "humidity": humidity,
                "unit": unit,
            }
            return weather_info

        else:
            print(f"E: {request.getcode()}")

    except Exception as e:
        print(e)
