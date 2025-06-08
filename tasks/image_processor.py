from prefect import task
from PIL import Image

@task
def process_images(img_paths: list[str]) -> list[str]:
    processed = []
    for path in img_paths:
        img = Image.open(path)
        img = img.resize((800, int(img.height * 800 / img.width)))
        img.save(path, optimize=True, quality=80)
        processed.append(path)
    return processed

