import sys

from string import Template
from openweather import openweather
from utils.ascii_icons import get_ascii

try:
    from colored import attr, fg
except:
    print("Module 'colored' not installed.")
    print("Run: pip3 install -r requirements.txt")
    sys.exit(0)


output_template = Template(
    """ ${city}, ${country}
 ${icon}
 ${temp}${unit} - ${temp_min}º / ${temp_max}º
 ${description}
"""
)


def weather_cli(verbose, color):
    try:
        weather_info = openweather()

        city_name = weather_info.get("city_name").title()
        country = weather_info.get("country")
        description = weather_info.get("description").title()
        icon = weather_info.get("icon")
        temp = weather_info.get("temp")
        temp_min = weather_info.get("temp_min")
        temp_max = weather_info.get("temp_max")
        unit = weather_info.get("unit")

        if verbose:
            verbose_output = output_template.substitute(
                city=city_name,
                country=country,
                icon=get_ascii(icon),
                temp=f"{temp:.0f}",
                unit=unit,
                temp_min=f"{temp_min:.0f}",
                temp_max=f"{temp_max:.0f}",
                description=description,
            )
            print(verbose_output)
        else:
            if color:
                print(f"{attr(1)}{fg(4)}{temp:.0f}{unit}{attr(0)}")
            else:
                print(f"{temp:.0f}{unit}")
    except Exception as e:
        print("E: something went wrong")
        print(e)
