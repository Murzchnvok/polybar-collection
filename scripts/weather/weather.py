import argparse
import os
import sys

from getcity import getcity
from openweather import openweather

try:
    from colored import attr, fg
except:
    print("You need to install 'colored'")
    print("Run: pip3 install colored --user")
    sys.exit(0)

# This API KEY is for my personal usage.
# Please get your own API KEY here https://openweathermap.org/api,
# and set an environment variable for OPENWEATHER_API_KEY with your API KEY.
API_KEY = "970606528befaa317698cc75083db8b2"
OPENWEATHER_API_KEY = os.environ.get("OPENWEATHER_API_KEY", API_KEY)


def weather_output(verbose, color):
    try:
        weather_info = openweather(
            args.city[0] if args.city else getcity(),
            args.unit[0] if args.unit else "",
            args.api_key[0] if args.api_key else OPENWEATHER_API_KEY,
        )

        description = weather_info.get("description").title()
        temp = weather_info.get("temp")
        unit = weather_info.get("unit")

        if color:
            if verbose:
                print(
                    f"{attr(1)}{fg(4)}{temp:.0f}{unit}{attr(0)}, {fg(5)}{description}{attr(0)}"
                )
            else:
                print(f"{attr(1)}{fg(4)}{temp:.0f}{unit}{attr(0)}")
        else:
            if verbose:
                print(f"{temp:.0f}{unit}, {description}")
            else:
                print(f"{temp:.0f}{unit}")
    except Exception as e:
        print("E: something went wrong")
        print(e)


USAGE_MESSAGE = f"""{attr(1)}{fg(2)}%(prog)s {fg(3)}[-c [CITY_NAME]] [-u [UNIT]] [-a [API_KEY]] {fg(4)}[-v] [--color]{attr(0)}

Some examples:
~$ {attr(1)}{fg(2)}%(prog)s{attr(0)}
::> 275 K

~$ {attr(1)}{fg(2)}%(prog)s {fg(3)}-c london{attr(0)}
::> 291 K

~$ {attr(1)}{fg(2)}%(prog)s {fg(3)}-u imperial {fg(4)}-v{attr(0)}
::> 79ºF, Scattered Clouds

~$ {attr(1)}{fg(2)}%(prog)s {fg(4)}-v -C{fg(3)} -u metric{attr(0)}
::> {attr(1)}{fg(4)}26ºC{attr(0)}, {fg(5)}Broken Clouds{attr(0)}

~$ {attr(1)}{fg(2)}%(prog)s {fg(3)}-c florida -u metric {fg(4)}-v --color{attr(0)}
::> {attr(1)}{fg(4)}27ºC{attr(0)}, {fg(5)}Thunderstorm{attr(0)}

~$ {attr(1)}{fg(2)}%(prog)s {fg(3)}-c "rio de janeiro" -u metric -a 439d4b804bc8187953eb36d2a8c26a02 {fg(4)}-v{attr(0)}
::> 25ºC
"""
parser = argparse.ArgumentParser(
    usage=USAGE_MESSAGE,
    description="Display information about the weather.",
)
parser.add_argument(
    "-c",
    metavar="CITY",
    dest="city",
    type=str,
    nargs=1,
    help="city name (default: try to get your city using your public ip address)",
)
parser.add_argument(
    "-u",
    metavar="metric/imperial",
    choices=("metric", "imperial"),
    dest="unit",
    type=str,
    nargs=1,
    help="unit of temperature (default: kelvin)",
)
parser.add_argument(
    "-a",
    metavar="API_KEY",
    dest="api_key",
    nargs=1,
    help="API Key",
)
parser.add_argument(
    "-v",
    "--verbose",
    action="store_true",
    dest="verbose",
    help="verbose mode",
)
parser.add_argument(
    "-C",
    "--color",
    action="store_true",
    dest="color",
    help="colorful output",
)


if __name__ == "__main__":
    args = parser.parse_args()

    weather_output(args.verbose, args.color)
