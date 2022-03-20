import argparse

USAGE_MESSAGE = """%(prog)s [-c [CITY_NAME]] [-u [UNIT]] [-a [API_KEY]] [-l [LANGUAGE]] [-v]

Some examples:
~$ %(prog)s
::> 275 K

~$ %(prog)s -c london
::> 291 K

~$ %(prog)s -u imperial -v
::> 79ºF, Scattered Clouds

~$ %(prog)s -v -C -u metric
::> 26ºC, Broken Clouds

~$ %(prog)s -c florida -u metric -v
::> 27ºC, Thunderstorm

~$ %(prog)s -c rio de janeiro -u metric -a 439d4b804bc8187953eb36d2a8c26a02 -v -l pt_br
::> 25ºC, Céu Limpo
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
    nargs="+",
    help="city name",
)
parser.add_argument(
    "-l",
    metavar="LANG",
    dest="lang",
    type=str,
    nargs=1,
    help="language (en, es, fr, ja, pt, pt_br, ru, zh_cn)",
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

args = parser.parse_args()
