import json
import urllib.request

data = json.loads(urllib.request.urlopen("http://wttr.in/?format=j1").read())
cur_temp = [cur_temp["temp_C"] for cur_temp in data["current_condition"]]

print(f"{cur_temp[0]}")
