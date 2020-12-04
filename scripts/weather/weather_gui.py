import PySimpleGUI as sg

from openweather import openweather
from utils.parser import args
from utils.themes import *


weather_conditions = {
    "Clear": "sun",
    "Clouds": "cloud",
    "Drizzle": "cloud-drizzle",
    "Rain": "cloud-rain",
    "Snow": "cloud-snow",
    "Thunderstorm": "cloud-lightning",
}


def weather_gui():
    try:
        weather_info = openweather()

        city_name = weather_info.get("city_name").title()
        country = weather_info.get("country")
        main_desc = weather_info.get("main_desc").title()
        description = weather_info.get("description").title()
        temp = weather_info.get("temp")
        temp_min = weather_info.get("temp_min")
        temp_max = weather_info.get("temp_max")
        unit = weather_info.get("unit")

        font_ubuntu = "UbuntuMono Nerd Font"

        sg.theme("MonoWhite")
        icon_name = weather_conditions.get(main_desc)
        weather_icon = f"weather-icons/{icon_name}.png"
        if args.dark_theme:
            sg.theme("MonoDark")
            weather_icon = f"weather-icons/w-{icon_name}.png"

        layout = [
            [
                sg.Text(
                    f"{city_name}, {country}",
                    font=(font_ubuntu, 16),
                    justification="center",
                    size=(100, 2),
                )
            ],
            [
                sg.Button(
                    border_width=0,
                    bind_return_key=True,
                    image_filename=weather_icon,
                    image_size=(300, 150),
                    key="update",
                )
            ],
            [
                sg.Text(
                    f"{temp:.0f}{unit}",
                    font=(font_ubuntu, 40),
                    justification="center",
                    size=(100, 1),
                )
            ],
            [
                sg.Text(
                    f"{description}",
                    font=(font_ubuntu, 16),
                    justification="center",
                    size=(100, 2),
                )
            ],
            [
                sg.Text(
                    f"{temp_min:.0f}º / {temp_max:.0f}º",
                    font=(font_ubuntu, 16),
                    justification="center",
                    size=(100, 1),
                    text_color="grey",
                )
            ],
        ]

        window = sg.Window(
            "MonoWeather",
            layout,
            auto_size_buttons=True,
            auto_size_text=True,
            finalize=True,
            # background_color=bg_color,
            size=(300, 410),
        )

        while True:
            event, _ = window.read()
            if event == sg.WIN_CLOSED:
                break

            elif event == "update":
                window.close()
                weather_gui()

        window.close()

    except Exception as e:
        print("E: something went wrong")
        print(e)


if __name__ == "__main__":
    weather_gui()
