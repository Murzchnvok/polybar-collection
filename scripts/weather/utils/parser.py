import sys

from .usage_message import USAGE_MESSAGE

try:
    import argparse
except:
    print("Module 'argparse' not installed.")
    print("Run: pip3 install -r requirements.txt")
    sys.exit(0)

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
