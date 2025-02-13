import sys
from pathlib import Path

import requests


def main():
    url_fmt = "https://{}.wiktionary.org/w/index.php?title={}&action=raw"
    folder = Path(__file__).parent / "data"
    for locale in folder.iterdir():
        for file in locale.glob("*.wiki"):
            current_content = file.read_text().strip()
            url = url_fmt.format(locale.name, file.stem)
            with requests.get(url) as req:
                if not req.ok:
                    continue
                new_content = req.text.strip()
            if current_content != new_content:
                file.write_text(req.text + "\n")
                print(f"Updated {file}", flush=True)


if __name__ == "__main__":
    sys.exit(main())
