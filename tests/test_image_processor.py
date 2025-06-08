from tasks.image_processor import process_images
from PIL import Image
import os

def test_process_images():
    paths = ["temp_images/img_0.jpg", "temp_images/img_1.jpg"]  # 위 test_download 후 존재
    result = process_images.fn(paths)

    for path in result:
        img = Image.open(path)
        assert img.width == 800

