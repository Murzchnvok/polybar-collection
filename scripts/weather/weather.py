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


def openweather(city, lang, unit, api_key=OPENWEATHER_API_KEY):
    try:
        url = f"{OPENWEATHER_URL}?q={city}&lang={lang}&units={unit}&appid={api_key}"
        request = urllib.request.urlopen(url)
        if request.getcode() == 200:
            data = json.loads(request.read())
            return {
                "name": data["name"],
                "country": iso3().get(data["sys"]["country"]),
                "temp": int(data["main"]["temp"]),
                "unit": check_unit(unit),
                "description": data["weather"][0]["description"],
            }
        else:
            print(f"E: {request.getcode()}")
    except:
        return None


if __name__ == "__main__":
    city = args.city[0] if args.city else get_city()
    lang = args.lang[0] if args.lang else "en"
    unit = args.unit[0] if args.unit else "standard"

    weather = openweather(city, lang, unit)
    if weather:
        name = weather.get("name")
        country = weather.get("country")
        temp = weather.get("temp")
        unit = weather.get("unit")
        description = weather.get("description")

        if args.verbose:
            print(f"{temp}{unit}, {description.title()} - {name}, {country}")
        else:
            print(f"{temp}{unit}")
    else:
        print("-1")
