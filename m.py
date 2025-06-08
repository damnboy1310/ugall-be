import requests
from selectolax.parser import HTMLParser

def parse_dcinside_post(url):
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    res = requests.get(url, headers=headers)
    if res.status_code != 200:
        raise Exception(f"❗ 요청 실패: HTTP {res.status_code}")

    tree = HTMLParser(res.text)

    # 제목 추출
    title_node = tree.css_first(".title_subject")
    title = title_node.text(strip=True) if title_node else "제목 없음"

    # 본문 HTML 추출
    content_node = tree.css_first(".write_div")
    contents_html = content_node.html if content_node else "<p>본문 없음</p>"

    # 첨부파일 링크 추출
    attachments = []
    attach_root = tree.css_first(".appending_file")
    if attach_root:
        for li in attach_root.css("li"):
            a_tag = li.css_first("a")
            if a_tag and "href" in a_tag.attributes:
                attachments.append(a_tag.attributes["href"])

    return {
        "url": url,
        "title": title,
        "contents": contents_html,
        "attachments": attachments
    }

def save_html(contents_html, filename="contents.html"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(contents_html)
    print(f"✅ 본문 HTML이 {filename} 로 저장되었습니다.")

if __name__ == "__main__":
    test_url = "https://gall.dcinside.com/board/view/?id=programming&no=1234567"  # 실제 글 URL로 바꾸기 https://gall.dcinside.com/board/view/?id=dcbest&no=336234
    result = parse_dcinside_post(test_url)

    print("🔗 URL:", result["url"])
    print("📝 제목:", result["title"])
    print("📎 첨부파일:")
    for href in result["attachments"]:
        print("   -", href)

    save_html(result["contents"])  # contents.html 저장
