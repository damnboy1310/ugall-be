from prefect import task
import requests
import os

@task
def download_images(img_urls: list[str]) -> list[str]:
    paths = []
    os.makedirs("temp_images", exist_ok=True)
    for i, url in enumerate(img_urls):
        headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        resp = requests.get(url, headers=headers)
        path = f"temp_images/img_{i}.jpg"
        with open(path, "wb") as f:
            f.write(resp.content)
        paths.append(path)
    return paths

