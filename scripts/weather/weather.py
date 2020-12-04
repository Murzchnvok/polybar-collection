from utils.parser import args
from weather_gui import weather_gui
from weather_cli import weather_cli

if __name__ == "__main__":
    if args.gui:
        weather_gui()
    else:
        weather_cli(args.verbose, args.color)
