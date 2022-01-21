import os

import requests

from util.get_city import get_city
from util.get_iso3 import get_iso3
from util.parser import args
from util.unit_suffix import unit_suffix

# Get your API KEY here https://openweathermap.org/api,
# and set an environment variable for OPENWEATHER_API_KEY with your API KEY.
API_KEY = "970606528befaa317698cc75083db8b2"
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def openweather(city: str, lang: str, unit: str, api_key: str) -> dict:
    try:
        r = requests.get(
            f"{OPENWEATHER_URL}?q={city}&lang={lang}&units={unit}&appid={api_key}"
        )
        data = r.json()
        city = data.get("name")
        country = data.get("sys").get("country")
        temp = data.get("main").get("temp")
        unit = unit
        desc = data.get("weather")[0].get("description")

        return {
            "city": city,
            "country": get_iso3(country),
            "temp": int(temp),
            "unit": unit_suffix(unit),
            "desc": desc.title(),
        }
    except:
        return {"error": "something is not right"}


def main() -> None:
    city = args.city[0] if args.city else get_city()
    lang = args.lang[0] if args.lang else "en"
    unit = args.unit[0] if args.unit else "standard"
    api_key = (
        args.api_key[0]
        if args.api_key
        else os.environ.get("OPENWEATHER_API_KEY", API_KEY)
    )

    weather = openweather(city, lang, unit, api_key)
    if error := weather.get("error"):
        print(error)
    else:
        city, country, temp, unit, desc = weather.values()
        if args.verbose:
            print(f"{temp}{unit}, {desc} - {city}, {country}")
        else:
            print(f"{temp}{unit}")


if __name__ == "__main__":
    main()
