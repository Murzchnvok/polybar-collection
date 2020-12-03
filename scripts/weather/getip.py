import json
import urllib.request


def getip():
    """Return your public ip address.

    Returns:
        data['ip'] (str): Return your public ip address
    """
    request = urllib.request.urlopen("https://api.ipify.org?format=json")
    if request.getcode() == 200:
        data = json.loads(request.read())
        return data["ip"]