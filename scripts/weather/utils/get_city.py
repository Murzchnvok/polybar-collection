import json
import urllib.request

# r = requests.get("https://ipapi.co/json", headers={"user-agent": "Mozilla/5.0"})
# r = requests.get(url, headers={"user-agent": "Mozilla/5.0"})
# data = r.json()
# print(data["city"])


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
