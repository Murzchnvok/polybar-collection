import json
import urllib.request


def iso3():
    """Return a dictionary of ISO3 countries code.

    Returns:
        data (dict): Return a dictionary with the ISO3 countries code.
    """
    request = urllib.request.urlopen("http://country.io/iso3.json")
    if request.getcode() == 200:
        data = json.loads(request.read())
        return data
