import PySimpleGUI as sg

from openweather import openweather


def weather_gui():
    try:
        weather_info = openweather()

        city_name = weather_info.get("city_name").title()
        country = weather_info.get("country")
        description = weather_info.get("description").title()
        temp = weather_info.get("temp")
        temp_min = weather_info.get("temp_min")
        temp_max = weather_info.get("temp_max")
        unit = weather_info.get("unit")

        font_ubuntu = "UbuntuMono Nerd Font"

        sg.theme("Default 1")
        layout = [
            [
                sg.Text(
                    f"{city_name}, {country}",
                    background_color="white",
                    font=(font_ubuntu, 16),
                    justification="center",
                    size=(100, 2),
                    text_color="black",
                )
            ],
            [
                sg.Button(
                    border_width=0,
                    bind_return_key=True,
                    button_color=("white", "white"),
                    image_filename="weather-icons/cloud-rain.png",
                    image_size=(300, 150),
                    key="update",
                )
            ],
            [
                sg.Text(
                    f"{temp:.0f}{unit}",
                    background_color="white",
                    font=(font_ubuntu, 40),
                    justification="center",
                    size=(100, 1),
                    text_color="black",
                )
            ],
            [
                sg.Text(
                    f"{description}",
                    background_color="white",
                    font=(font_ubuntu, 16),
                    justification="center",
                    size=(100, 2),
                    text_color="black",
                )
            ],
            [
                sg.Text(
                    f"{temp_min:.0f}º / {temp_max:.0f}º",
                    background_color="white",
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
            background_color="white",
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
