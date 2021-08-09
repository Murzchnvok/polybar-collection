import json
import os
import urllib.request

from utils.check_unit import check_unit
from utils.get_city import get_city
from utils.iso3 import iso3
from utils.parser import args

# Get your API KEY here https://openweathermap.org/api,
# and set an environment variable for OPENWEATHER_API_KEY with your API KEY.
API_KEY = "970606528befaa317698cc75083db8b2"
OPENWEATHER_API_KEY = (
    args.api_key[0] if args.api_key else os.environ.get("OPENWEATHER_API_KEY", API_KEY)
)
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

NAME = args.city[0] if args.city else get_city()
LANG = args.lang[0] if args.lang else "en"
UNIT = args.unit[0] if args.unit else "standard"


def openweather(city=NAME, lang=LANG, unit=UNIT, api_key=OPENWEATHER_API_KEY):
    try:
        request = urllib.request.urlopen(
            f"{OPENWEATHER_URL}?q={city.replace(' ', '+')}"
            f"&lang={lang}&units={unit}&appid={api_key}"
        )
        if request.getcode() == 200:
            data = json.loads(request.read())

            temp = int(data["main"]["temp"])

            return {
                "name": data["name"],
                "country": iso3().get(data["sys"]["country"]),
                "temp": temp,
                "unit": check_unit(unit),
                "description": data["weather"][0]["description"],
            }

        else:
            print(f"E: {request.getcode()}")

    except Exception as e:
        pass


if __name__ == "__main__":
    weather = openweather()
    temp = weather.get("temp")
    unit = weather.get("unit")
    description = weather.get("description")

    if args.verbose:
        print(f"{temp}{unit}, {description.title()}")
    else:
        print(f"{temp}{unit}")
