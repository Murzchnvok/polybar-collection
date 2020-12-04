import sys

from openweather import openweather

try:
    from colored import attr, fg
except:
    print("You need to install 'colored'")
    print("Run: pip3 install colored --user")
    sys.exit(0)


def weather_cli(verbose, color):
    try:
        weather_info = openweather()

        description = weather_info.get("description").title()
        temp = weather_info.get("temp")
        unit = weather_info.get("unit")

        if color:
            if verbose:
                print(
                    f"{attr(1)}{fg(4)}{temp:.0f}{unit}{attr(0)}, {fg(5)}{description}{attr(0)}"
                )
            else:
                print(f"{attr(1)}{fg(4)}{temp:.0f}{unit}{attr(0)}")
        else:
            if verbose:
                print(f"{temp:.0f}{unit}, {description}")
            else:
                print(f"{temp:.0f}{unit}")
    except Exception as e:
        print("E: something went wrong")
        print(e)
