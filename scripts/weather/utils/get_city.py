import json
import urllib.request

from .get_ip import get_ip


def get_city():
    request = urllib.request.urlopen("http://ip-api.com/json/" + get_ip())
    if request.getcode() == 200:
        data = json.loads(request.read())
        return data["city"]
    else:
        print(f"E: {request.getcode()}")