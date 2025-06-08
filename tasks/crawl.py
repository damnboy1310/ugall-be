from prefect import task
import requests
from selectolax.parser import HTMLParser

@task
def crawl_dcinside(url: str):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    res = requests.get(url, headers=headers)

    tree = HTMLParser(res.text)
    title_el = tree.css_first(".title_subject")
    title = title_el.text() if title_el else "NO_TITLE"

    content_div_el = tree.css_first(".write_div")
    content_div = content_div_el.html if content_div_el else "NO_CONTENT"

    img_tags = tree.css(".write_div img")
    img_urls = [img.attributes.get("src") for img in img_tags if img.attributes.get("src")]

    return res.status_code, title, content_div, img_urls
