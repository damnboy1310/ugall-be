from tasks.image_downloader import download_images
import os

def test_download_images():
    img_urls = [
        "https://picsum.photos/200",
        "https://picsum.photos/300"
    ]

    paths = download_images.fn(img_urls)

    for path in paths:
        assert os.path.exists(path)

