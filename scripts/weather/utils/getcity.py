import json
import urllib.request

from utils.getip import getip


def getcity():
    """Return the name of the city you're in based on your external ip address.

    Returns:
        data['city'] (str): Return the name of your city
    """
    request = urllib.request.urlopen("http://ip-api.com/json/" + getip())
    if request.getcode() == 200:
        data = json.loads(request.read())
        return data["city"]
