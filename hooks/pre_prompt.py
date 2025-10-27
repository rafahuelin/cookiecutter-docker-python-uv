import json
from datetime import date
from pathlib import Path

import requests
from requests import Response


def get_supported_python_versions() -> list[dict]:
    url = "https://endoflife.date/api/python.json"
    response: Response = requests.get(url)
    if response.status_code == 200:
        data: list[dict] = response.json()
        supported_versions: list[dict] = [version for version in data if date.fromisoformat(version['eol']) > date.today()]
        return supported_versions
    else:
        raise Exception("Failed to fetch data")

def get_latest_uv_version() -> str:
    response = requests.get("https://pypi.org/pypi/uv/json")
    response_data = response.json()
    latest_version = response_data["info"]["version"]
    return latest_version

def main():
    versions = get_supported_python_versions()
    config_path = Path(__file__).parents[1] / "cookiecutter.json"
    data = json.loads(config_path.read_text())
    data["_supported_python_versions"] = {v["cycle"]: v for v in versions}
    data['python_version'] = [version["cycle"] for version in versions]
    data["_uv_version"] = get_latest_uv_version()
    config_path.write_text(json.dumps(data, indent=4))

if __name__ == "__main__":
    main()