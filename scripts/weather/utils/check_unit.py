def check_unit(unit="standard"):
    if unit == "metric":
        unit = "ºC"
    elif unit == "imperial":
        unit = "ºF"
    else:
        unit = " K"

    return unit
