import sys

try:
    from colored import attr, fg
except:
    print("You need to install 'colored'")
    print("Run: pip3 install colored --user")
    sys.exit(0)

USAGE_MESSAGE = f"""{attr(1)}{fg(2)}%(prog)s {fg(3)}[-c [CITY_NAME]] [-u [UNIT]] [-a [API_KEY]] {fg(4)}[-v]{attr(0)}

Some examples:
~$ {attr(1)}{fg(2)}%(prog)s{attr(0)}
::> 275 K

~$ {attr(1)}{fg(2)}%(prog)s {fg(3)}-c london{attr(0)}
::> 291 K

~$ {attr(1)}{fg(2)}%(prog)s {fg(3)}-u imperial {fg(4)}-v{attr(0)}
::> 79ºF, Scattered Clouds

~$ {attr(1)}{fg(2)}%(prog)s {fg(4)}-v -C{fg(3)} -u metric{attr(0)}
::> {attr(1)}{fg(4)}26ºC{attr(0)}, {fg(5)}Broken Clouds{attr(0)}

~$ {attr(1)}{fg(2)}%(prog)s {fg(3)}-c florida -u metric {fg(4)}-v{attr(0)}
::> 27ºC, Thunderstorm

~$ {attr(1)}{fg(2)}%(prog)s {fg(3)}-c "rio de janeiro" -u metric -a 439d4b804bc8187953eb36d2a8c26a02 {fg(4)}-v{attr(0)}
::> 25ºC
"""