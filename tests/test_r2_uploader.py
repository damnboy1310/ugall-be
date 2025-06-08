from tasks.r2_uploader import upload_to_r2

def test_upload_to_r2():
    test_imgs = ["temp_images/img_0.jpg"]
    urls = upload_to_r2.fn(test_imgs)

    for url in urls:
        assert url.startswith("https://")

