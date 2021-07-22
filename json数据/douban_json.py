# @Time : 2021/6/27 11:58 上午
# @Author : Bais
# @Email : 17343001493@163.com
# @File : douban_json.py
from parse_url import parse_url
import json

url = 'https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=50&page_start=0'
html_str = parse_url(url)
print(type(html_str))
ret = json.loads(html_str)  # 把字符串转化成python类型
print(type(ret))
ret2 = json.dumps(ret)  # 把python类型转化成json字符串
print(type(ret2))
with open('1.json', "w") as f:
    f.write(json.dumps(ret, ensure_ascii=False, indent=4))

temp_list = ret["subjects"]
for temp in temp_list:
    print("电影名:%s       URL：%s          评分:%s \t" % (temp['title'],temp['url'], temp['rate']))
