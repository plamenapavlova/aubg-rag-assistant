from src import config
import json
import requests


def download_all():
    config.RAW_DIR.mkdir(parents = True, exist_ok = True)
    with open(config.SOURCES_FILE, "r", encoding = "utf-8") as file:
        sources =json.load(file)

    for source in sources:
        store = config.RAW_DIR/source["filename"]
        if store.exists():
            print(source["filename"], " already downloaded")
            continue
        try:
            response = requests.get(source["url"], timeout = 60, headers={"User-Agent": "aubg-student-rag-project"})
            response.raise_for_status()
            with open(store, 'wb') as file:
                file.write(response.content)
                print(source["filename"], " downloaded successfully")
        except requests.RequestException as e:
            print(source["filename"], " failed:", e,  " download manually from ", source["url"])


if __name__ == "__main__":
    download_all()

