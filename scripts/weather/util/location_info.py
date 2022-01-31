import requests


def format_city(city: list[str]) -> str:
    return "+".join(city).title()


def get_city() -> str:
    try:
        r = requests.get("https://ipapi.co/json", headers={"User-agent": "Mozilla/5.0"})
        return r.json()["city"]
    except Exception:
        return "london"
