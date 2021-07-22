# @Time : 2021/7/22 3:28 下午
# @Author : Bais
# @Email : 17343001493@163.com
# @File : sanguo_spider.py
import json
import requests
from bs4 import BeautifulSoup


class sanGuoSpider:

    def __init__(self):
        self.url = "http://www.shicimingju.com/book/sanguoyanyi.html"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3741.400 QQBrowser/10.5.3863.400'}

    def parse_url(self):
        response = requests.get(self.url,self.headers)
        response.encoding = response.apparent_encoding

        return response.text

    def save_content_list(self, page_text):
        soup = BeautifulSoup(page_text, 'lxml')
        # 解析章节标题和详情页url
        li_list = soup.select('.book-mulu > ul > li')
        with open('./sanguo3.txt',"w",encoding='utf-8') as f:
            for li in li_list:
                title = li.a.string
                detail_url = 'http://www.shicimingju.com' + li.a['href']  # 超链接不是完整URL，需要点击超链接查看完整URL
                # 对详情页发起请求，解析出章节内容
                detail_page_text = requests.get(url=detail_url, headers=self.headers).text
                # 解析出详情页中相关的章节内容
                detail_soup = BeautifulSoup(detail_page_text, 'lxml')
                div_tag = detail_soup.find('div', class_='chapter_content')
                # 解析到了章节的内容
                content = div_tag.text
                f.write(title + ': ' + detail_url + '\n')
                print(title, "爬取成功!!!")

    def run(self):  # 实现主要逻辑
        # 1、发送请求获取响应
        page_text = self.parse_url()
        # 2、提取数据
        # content_list = self.get_content_list(html_str)
        # 3、保存
        self.save_content_list(page_text)


if __name__ == '__main__':
    sanguo_spider = sanGuoSpider()
    sanguo_spider.run()
