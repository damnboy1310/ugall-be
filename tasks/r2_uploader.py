from prefect import task
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

@task
def upload_to_r2(paths: list[str]) -> list[str]:
    session = boto3.session.Session()
    s3 = session.client(
        service_name='s3',
        endpoint_url=os.getenv("R2_ENDPOINT"),
        aws_access_key_id=os.getenv("R2_ACCESS_KEY"),
        aws_secret_access_key=os.getenv("R2_SECRET_KEY")
    )
    uploaded_urls = []
    for path in paths:
        key = f"uploads/{os.path.basename(path)}"
        s3.upload_file(path, os.getenv("R2_BUCKET"), key)
        url = f"{os.getenv('R2_CDN_BASE')}/{key}"
        uploaded_urls.append(url)
    return uploaded_urls

