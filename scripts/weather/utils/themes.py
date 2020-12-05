themes = {
    "black": {
        "bg_color": "#000000",
        "city_color": "#404040",
        "temp_color": "#ffffff",
        "desc_color": "#ffffff",
        "min_max_color": "#404040",
    },
    "dracula": {
        "bg_color": "#282a36",
        "city_color": "#6272a4",
        "temp_color": "#50fa7b",
        "desc_color": "#bd93f9",
        "min_max_color": "#6272a4",
    },
    "gruvbox": {
        "bg_color": "#282828",
        "city_color": "#458588",
        "temp_color": "#fadb27",
        "desc_color": "#d65d0e",
        "min_max_color": "#bdae93",
    },
    "light": {
        "bg_color": "#ffffff",
        "city_color": "#000000",
        "temp_color": "#000000",
        "desc_color": "#000000",
        "min_max_color": "#757575",
    },
    "neon": {
        "bg_color": "#000020",
        "city_color": "#186DFF",
        "temp_color": "#03EAFF",
        "desc_color": "#FFE900",
        "min_max_color": "#DA06FF",
    },
    "nord": {
        "bg_color": "#2E3440",
        "city_color": "#5E81AC",
        "temp_color": "#EBCB8B",
        "desc_color": "#B48EAD",
        "min_max_color": "#81A1C1",
    },
}


def get_theme(theme):
    return themes.get(theme) if theme in themes else themes.get("light")