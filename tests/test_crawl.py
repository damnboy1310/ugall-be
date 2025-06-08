from tasks.crawl import crawl_dcinside

def test_crawl_dcinside():
    url = "https://gall.dcinside.com/board/view/?id=programming&no=1234567"  # 실제 글 URL로 대체

    status_code, title, content_html, img_urls = crawl_dcinside.fn(url)

    # === 직접 확인용 print ===
    print(f"Status: {status_code}")
    print(f"Title: {title}")
    print(f"Content length: {len(content_html)}")
    print(f"Image URLs: {img_urls}")

    # === assert 테스트 ===
    assert status_code == 200, f"Expected status 200, got {status_code}"
    assert isinstance(title, str)
    assert isinstance(content_html, str)
    assert isinstance(img_urls, list)
