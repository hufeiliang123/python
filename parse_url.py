# @Time : 2021/6/27 11:25 上午
# @Author : Bais
# @Email : 17343001493@163.com
# @File : parse_url.py

import requests
from retrying import retry

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36"}


@retry(stop_max_attempt_number=3)
def _parse_url(url, method, data):
    print("-" * 20)
    if method == "POST":
        response = requests.post(url, headers=headers, data=data)
    else:
        response = requests.get(url, headers=headers, timeout=3)
    assert response.status_code == 200
    return response.content.decode()


def parse_url(url, method="GET", data=None):
    try:
        html_str = _parse_url(url, method, data=data)
    except:
        html_str = None
    return html_str


if __name__ == '__main__':
    url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=0"
    print(parse_url(url))
    # url = input()
    # parse_url(url)
