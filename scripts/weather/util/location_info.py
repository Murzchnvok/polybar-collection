import json
from pathlib import Path

import requests


def country_code_to_iso3(alpha2: str) -> str:
    return json.loads(open(Path(__file__).parent / "iso3.json").read()).get(alpha2)


def format_city(city: list) -> str:
    return " ".join(city).title()


def get_city() -> str:
    try:
        r = requests.get("https://ipapi.co/json")
        data = r.json()
        return data["city"]
    except:
        print("Couldn't load json data")
