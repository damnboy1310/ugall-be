from prefect import flow
from tasks.crawl import crawl_dcinside
from tasks.image_downloader import download_images
from tasks.image_processor import process_images
from tasks.r2_uploader import upload_to_r2
from tasks.wordpress import post_to_wordpress

@flow
def main(url: str):
    _status_code, title, content_html, img_urls = crawl_dcinside(url)
    local_paths = download_images(img_urls)
    processed_paths = process_images(local_paths)
    cdn_urls = upload_to_r2(processed_paths)

    # Replace image URLs in content
    for i, cdn_url in enumerate(cdn_urls):
        content_html = content_html.replace(img_urls[i], cdn_url)

    post_to_wordpress(title, content_html)

if __name__ == "__main__":
    test_url = "https://gall.dcinside.com/board/view/?id=programming&no=1234567"
    main(test_url)

