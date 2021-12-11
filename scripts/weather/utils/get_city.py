import json
import urllib.request


def return_city(city):
    return "+".join(city.strip().split())


def get_city(default_city="London"):
    try:
        request = urllib.request.urlopen("https://ipapi.co/json")
        if request.getcode() == 200:
            try:
                data = json.loads(request.read())
                return return_city(data["city"])
            except json.JSONDecodeError:
                print("E: Couldn't load Json data.")
        else:
            print(f"E: {request.getcode()}")
    except:
        return return_city(default_city)
