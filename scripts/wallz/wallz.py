import json
import shutil
import subprocess
from pathlib import Path

import requests

from util import parser

BASE_DIR = Path(__file__).parent

BASE_URL = "https://www.bing.com"
LANG_CODES = ["en-US", "ja-JP"]

WALL_DIR = BASE_DIR / "wallpapers"
if not Path.exists(WALL_DIR):
    Path.mkdir(WALL_DIR)


class Wallz:
    def __init__(self):
        self.URLS_FILE = BASE_DIR / "urls.json"
        self.urls = {}

        try:
            self.urls = json.loads(open(self.URLS_FILE, "r+").read())
        except FileNotFoundError:
            open(self.URLS_FILE, "w+").write("{}")
        except json.decoder.JSONDecodeError:
            pass

    def get_daily(self):
        r = requests.get(
            f"{BASE_URL}/HPImageArchive.aspx?format=js&n=1",
            headers={"user-agent": "Mozilla/5.0"},
        )
        url = r.json()["images"][0]["url"]
        return self.return_url(url)

    def get_urls(self):
        for code in LANG_CODES:
            for i in range(2):
                print(i, code)
                r = requests.get(
                    f"{BASE_URL}/HPImageArchive.aspx?format=js&n=8&idx={i}&mkt={code}",
                    headers={"user-agent": "Mozilla/5.0"},
                )
                data = r.json()["images"]
                for url in data:
                    url, filename = self.return_url(url["url"])
                    self.urls[self.set_id()] = {"url": url, "filename": filename}
        self.save_to_json()

    def get_url(self):
        if len(self.urls) == 0:
            self.get_urls()

        try:
            data = self.urls.pop(list(self.urls.keys())[0])
            self.save_to_json()
            return data["url"], data["filename"]
        except KeyError:
            self.get_urls()
        self.save_to_json()

    def get_image(self, daily=True):
        if daily:
            url, filename = self.get_daily()
        else:
            url, filename = self.get_url()

        filepath = WALL_DIR / filename
        if not filepath.exists():
            r = requests.get(url, headers={"user-agent": "Mozilla/5.0"})
            with open(filepath, "wb") as f:
                for chunk in r.iter_content(chunk_size=128):
                    f.write(chunk)

        self.set_image(filepath)

    def set_image(self, filepath):
        subprocess.run(["feh", "--bg-fill", filepath])

    def return_url(self, url):
        url = f"{BASE_URL}{url}"
        filename = url.split("id=")[1].split("&")[0]
        return url, filename

    def clear_urls(self):
        Path.unlink(self.URLS_FILE, missing_ok=True)

    def remove_images(self):
        shutil.rmtree(WALL_DIR, ignore_errors=True)

    def set_id(self):
        try:
            return str(max(int(k) for k in self.urls.keys()) + 1)
        except ValueError:
            return "1"

    def save_to_json(self):
        json.dump(self.urls, open(self.URLS_FILE, "w"), indent=True)


def main() -> None:
    wallz = Wallz()

    args = parser.args
    if args.clear:
        wallz.clear_urls()
    elif args.remove:
        wallz.remove_images()
    elif args.daily:
        wallz.get_image()
    else:
        wallz.get_image(daily=False)


if __name__ == "__main__":
    main()
