import os

import openweather
from util import location_info, parser

# Get your API KEY here https://openweathermap.org/api,
# and set an environment variable for OPENWEATHER_API_KEY with your API KEY.
OPENWEATHER_API_KEY = "970606528befaa317698cc75083db8b2"


def main() -> None:
    args = parser.args

    city = (
        location_info.format_city(args.city) if args.city else location_info.get_city()
    )
    api_key = (
        args.api_key[0]
        if args.api_key
        else os.environ.get("OPENWEATHER_API_KEY", OPENWEATHER_API_KEY)
    )
    lang = args.lang[0] if args.lang else "en"
    unit = args.unit[0] if args.unit else "standard"

    weather = openweather.get_weather(city, lang, unit, api_key)
    if weather:
        temp, desc = weather.values()
        if args.verbose:
            print(f"{temp}, {desc}")
        else:
            print(f"{temp}")


if __name__ == "__main__":
    main()
