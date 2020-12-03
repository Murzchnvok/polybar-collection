def check_unit(unit):
    """Return the abbreviation name for a unit.

    Args:
        unit (str): Name of the unit (imperial or metric)

    Returns:
        unit (str): Return the abbreviation name for the unit
    """
    if unit == "metric":
        unit = "ºC"
    elif unit == "imperial":
        unit = "ºF"
    else:
        unit = " K"

    return unit