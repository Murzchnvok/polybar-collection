import sys


try:
    from colored import attr, fg
except:
    print("Module 'colored' not installed.")
    print("Run: pip3 install -r requirements.txt")
    sys.exit(0)

atmosphere = f"""
    .--.
 .-(    ).
(___.__)__)
 {fg(4)}---- -- -{attr(0)}
 {fg(4)}- --- ---{attr(0)}
 """

clouds = """
    .--.
 .-(    ).
(___.__)__)
"""

cloud_moon = f"""
    .--.{fg(4)}""\\{attr(0)}
 .-(    )_{fg(4)}/{attr(0)}
(___.__)__)
"""

cloud_sun = f"""
       {fg(3)}\  /{attr(0)}
    .--.{fg(3)}""\\ _{attr(0)}
 .-(    )_{fg(3)}/{attr(0)}
(___.__)__)
"""

moon = f"""
    {fg(4)}.-.{attr(0)}
   {fg(4)}(   ){attr(0)}
    {fg(4)}`-´{attr(0)}
"""

rain = f"""
    .--.
 .-(    ).
(___.__)__)
   {fg(6)}‘ ‘ ‘{attr(0)}
"""

rain2 = f"""
    .--.
 .-(    ).
(___.__)__)
  {fg(6)}‘ ‘ ‘ ‘{attr(0)}
  {fg(6)}‘ ‘ ‘ ‘{attr(0)}
"""

snow = f"""
    .--.
 .-(    ).
(___.__)__)
   {fg(6)}* * *{attr(0)}
"""

sun = f"""
   {fg(3)}\   /{attr(0)}
    {fg(3)}.-.{attr(0)}
 {fg(3)}- (   ) -{attr(0)}
    {fg(3)}`-´{attr(0)}
   {fg(3)}/   \\{attr(0)}
"""

thunderstorm = f"""
    .--.
 .-(    ).
(___.__)__)
  {fg(6)}‘!‘!‘!‘{attr(0)}
  {fg(6)}‘'‘'‘'‘{attr(0)}
"""

ascii_icons = {
    "01d": sun,
    "01n": moon,
    "02d": cloud_sun,
    "02n": cloud_moon,
    "03d": clouds,
    "03n": clouds,
    "04d": clouds,
    "04n": clouds,
    "09d": rain2,
    "09n": rain2,
    "10d": rain,
    "10n": rain,
    "11d": thunderstorm,
    "11n": thunderstorm,
    "13d": snow,
    "13n": snow,
    "50d": atmosphere,
    "50n": atmosphere,
}


def get_ascii(icon):
    return ascii_icons.get(icon)
