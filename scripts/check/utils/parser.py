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
    description="A 'check' to check if service is active and return status and color.",
)
parser.add_argument(
    "-s",
    "--service",
    metavar="SERVICE",
    choices=("nft", "tor", "privoxy"),
    dest="service",
    type=str,
    nargs=1,
    help="service name",
)
parser.add_argument(
    "-c",
    "--color",
    action="store_true",
    dest="color",
    help="return color name",
)

args = parser.parse_args()
