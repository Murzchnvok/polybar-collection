import requests


def format_city(city: str) -> str:
    return "+".join(city.strip().split())


def get_city() -> str:
    try:
        r = requests.get("https://ipapi.co/json")
        data = r.json()
        return format_city(data["city"])
    except:
        print("Couldn't load json data")
