import os
import requests
from requests.adapters import HTTPAdapter

API = os.environ.get("POLYBAR_WEATHER_API", "46276f91dcb44de4ac0134024262101")

def get_weather() -> str:
    try:
        s = requests.Session()
        s.mount("https://", HTTPAdapter(max_retries=5))
        r = s.get(f"http://api.weatherapi.com/v1/current.json?key={API}&q=auto:ip")
        data = r.json()
        current_temp = data["current"]["temp_c"]
        return f"{int(current_temp)}ºC"
    except requests.exceptions.ConnectionError:
        return "E: connection error"

def main():
    print(get_weather())

if __name__ == "__main__":
    main()
