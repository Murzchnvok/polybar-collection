import json
from pathlib import Path


def get_iso3(alpha2: str) -> str:
    return json.loads(open(Path(__file__).parent / "iso3.json").read()).get(alpha2)
