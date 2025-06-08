from dotenv import load_dotenv

load_dotenv()

from prefect import task
import requests
from requests.auth import HTTPBasicAuth
import os

@task
def post_to_wordpress(title: str, content: str):
    url = os.getenv("WP_API_URL")
    user = os.getenv("WP_USER")
    password = os.getenv("WP_APP_PASS")
    
    print(url, user, password)
    data = {
        "title": title,
        "content": content,
        "status": "publish"
    }
    resp = requests.post(f"{url}/posts", auth=HTTPBasicAuth(user, password), json=data)
    return resp.json()

