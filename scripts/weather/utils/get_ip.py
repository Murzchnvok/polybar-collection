import json
import urllib.request


def get_ip():
    request = urllib.request.urlopen("https://ipapi.co/json")
    if request.getcode() == 200:
        data = json.loads(request.read())
        return data["ip"]
    else:
        print(f"E: {request.getcode()}")
