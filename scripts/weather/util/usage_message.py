USAGE_MESSAGE = f"""%(prog)s [-c [CITY_NAME]] [-u [UNIT]] [-a [API_KEY]] [-l [LANGUAGE]] [-v]

Some examples:
~$ %(prog)s
::> 275 K

~$ %(prog)s -c london
::> 291 K

~$ %(prog)s -u imperial -v
::> 79ºF, Scattered Clouds

~$ %(prog)s -v -C -u metric
::> 26ºC, Broken Clouds

~$ %(prog)s -c florida -u metric -v
::> 27ºC, Thunderstorm

~$ %(prog)s -c "rio de janeiro" -u metric -a 439d4b804bc8187953eb36d2a8c26a02 -v -l pt_br
::> 25ºC, Céu Limpo
"""