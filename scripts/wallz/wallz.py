import argparse
import shutil
import subprocess
from pathlib import Path

import requests

BASE_DIR = Path(__file__).parent
WALL_DIR = BASE_DIR / "wallpapers"

if not Path.is_dir(WALL_DIR):
    Path.unlink(WALL_DIR, missing_ok=True)
    Path.mkdir(WALL_DIR, exist_ok=True)

BASE_URL = "https://www.bing.com"
API_URL = f"{BASE_URL}/HPImageArchive.aspx?format=js&n=1"


def set_wallpaper(filepath: Path) -> None:
    subprocess.run(["feh", "--bg-fill", filepath])


def remove_wallpapers() -> None:
    shutil.rmtree(WALL_DIR, ignore_errors=True)


def get_daily_wallpaper() -> None:
    with requests.Session() as s:
        r = s.get(API_URL).json().get("images")[0]
        image_url = r.get("url")
        filepath = WALL_DIR / (image_url.split(".")[1] + ".jpg")
        if not filepath.exists():
            r = s.get(BASE_URL + image_url)
            with open(filepath, "wb") as f:
                [f.write(chunk) for chunk in r.iter_content(chunk_size=None)]

    set_wallpaper(filepath)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Download Bing Daily Wallpaper.",
    )
    parser.add_argument(
        "-r",
        "--remove",
        action="store_true",
        dest="remove",
        help="remove downloaded wallpapers",
    )

    args = parser.parse_args()

    if args.remove:
        remove_wallpapers()
    else:
        get_daily_wallpaper()


if __name__ == "__main__":
    main()
