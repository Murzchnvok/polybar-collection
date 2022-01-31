import requests

from util import unit_info

OPENWEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city: str, lang: str, unit: str, api_key: str) -> dict[str, str] | None:
    try:
        r = requests.get(
            f"{OPENWEATHER_URL}?q={city}&lang={lang}&units={unit}&appid={api_key}",
            headers={"User-agent": "Mozilla/5.0"},
        )
        data = r.json()
        temp = data.get("main").get("temp")
        desc = data.get("weather")[0].get("description")
        unit = unit_info.unit_suffix(unit)

        return {
            "temp": f"{int(temp)}{unit}",
            "desc": desc.title(),
        }
    except Exception:
        return None
