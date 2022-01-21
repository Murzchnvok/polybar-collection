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
    description="Just a simple Bing Daily Wallpaper script.",
)
parser.add_argument(
    "-d",
    "--daily",
    action="store_true",
    dest="daily",
    help="get the daily wallpaper",
)
parser.add_argument(
    "-c",
    "--clear",
    action="store_true",
    dest="clear",
    help="clear the url links",
)
parser.add_argument(
    "-r",
    "--remove",
    action="store_true",
    dest="remove",
    help="remove downloaded wallpapers",
)

args = parser.parse_args()
