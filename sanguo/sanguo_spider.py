# @Time : 2021/7/22 3:28 下午
# @Author : Bais
# @Email : 17343001493@163.com
# @File : sanguo_spider.py
import json
import requests
from lxml import etree
from bs4 import BeautifulSoup

class sanGuoSpider:

    def __init__(self):
        self.url = "http://www.shicimingju.com/book/sanguoyanyi.html"

    def parse_url(self):
        response = requests.get(self.url)
        html_str = response.content.decode()
        return html_str

    def get_content_list(self, html_str):
        content_list = []
        html = etree.HTML(html_str)
        li_list = html.xpath('//div[@class="book-mulu"]')
        for li in li_list:
            item = {}
            item["title"] = li.xpath('.//ul/li/a/text()')
            # item["title"] = item["title"][0] if len(item["title"]) > 0 else None
            item["url"] = html.xpath('.//ul/li/a/@href')
            # item["url"] = item["url"][0] if len(item["url"]) > 0 else None
            content_list.append(item)
            print(item, "******************")
            print(content_list)
        return content_list

    def save_content_list(self, content_list):
        with open("./sanguo.txt", "a") as f:
            for i in content_list:
                f.write(json.dumps(i, ensure_ascii=False, indent=4))
        print("save success-----")

    def run(self):  # 实现主要逻辑
        # 1、发送请求获取响应
        html_str = self.parse_url()
        # 2、提取数据
        content_list = self.get_content_list(html_str)
        # 3、保存
        self.save_content_list(content_list)



if __name__ == '__main__':
    sanguo_spider = sanGuoSpider()
    sanguo_spider.run()
