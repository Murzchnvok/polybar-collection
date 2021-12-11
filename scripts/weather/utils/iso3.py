import json
import urllib.request
from pathlib import Path


def iso3():
    try:
        return json.loads(open(Path(__file__).parent / "iso3.json").read())
    except:
        try:
            request = urllib.request.urlopen("http://country.io/iso3.json")
            if request.getcode() == 200:
                try:
                    return json.loads(request.read())
                except json.JSONDecodeError:
                    print("E: Couldn't load Json data.")
            else:
                print(f"E: {request.getcode()}")
        except urllib.error.HTTPError:
            print("E: 404, url not found!")
