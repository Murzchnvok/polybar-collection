import json
import urllib.request

from check_unit import check_unit

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def openweather(city_name, unit, api_key):
    try:
        request = urllib.request.urlopen(
            f"{OPENWEATHER_URL}?q={city_name.replace(' ', '+')}&units={unit}&appid={api_key}"
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
