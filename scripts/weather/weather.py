import json
import urllib.request

# TODO: add argparse for better usage
# TODO: funtion for wttr
# http://wttr.in/?format=j1

# get your own api key https://openweathermap.org/api
OPENWEATHER_API_KEY = "970606528befaa317698cc75083db8b2"
OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


# Temperature in Kelvin is used by default.
# For temperature in Fahrenheit: imperial
# For temperature in Celsius: metric
def openweather(city_name, units="", api_key=OPENWEATHER_API_KEY):
    request = urllib.request.urlopen(
        f"{OPENWEATHER_URL}?q={city_name.replace(' ', '+')}&units={units}&appid={api_key}"
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

        if units == "metric":
            unit = "ºC"
        elif units == "imperial":
            unit = "ºF"
        else:
            unit = " K"

        print(f"{temp:.0f}{unit}")

    else:
        print(f"E: {request.getcode()}")


openweather("aracaju", units="metric")
