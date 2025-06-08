from tasks.wordpress import post_to_wordpress

def test_post_to_wp():
    html = "<h1>pytest test post</h1><p>본문 내용</p>"
    response = post_to_wordpress.fn("테스트 글", html)

    assert "id" in response
    assert "link" in response

