import requests
import os

URLS = {
    "old": "https://downloads.wortschatz-leipzig.de/corpora/eng_news_2010_1M-sentences.txt.gz",
    "new": "https://downloads.wortschatz-leipzig.de/corpora/eng_news_2020_1M-sentences.txt.gz"
}

os.makedirs("data/raw", exist_ok=True)

for label, url in URLS.items():
    print(f"Downloading {label} corpus...")
    r = requests.get(url, stream=True)
    r.raise_for_status()

    path = f"data/raw/{label}.txt.gz"

    with open(path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024 * 1024):
            if chunk:
                f.write(chunk)

    print(f"Saved {label} corpus to {path}")
