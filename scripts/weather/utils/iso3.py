import json
import urllib.request


def iso3():
    request = urllib.request.urlopen("http://country.io/iso3.json")
    if request.getcode() == 200:
        return json.loads(request.read())
    else:
        print(f"E: {request.getcode()}")
