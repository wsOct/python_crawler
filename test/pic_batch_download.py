import requests
from bs4 import BeautifulSoup

'''
1.拿到html源代码
2.找到代码中图片的信息（URL）
3.向图片的url发起请求，保存返回的信息并保存在文件里
'''

url = 'https://mp.weixin.qq.com/s/7qgz2PNaUxcf-WxUzzbf5A'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
res = requests.get(url, headers = headers)
# print(res.text)

html_doc = res.text

soup = BeautifulSoup(html_doc, 'html.parser')

for i, pic_src in enumerate(soup.find_all('img', attrs={'class': 'rich_pages'})):
    pic_link = pic_src.get('data-src')
    print(pic_link)
    pic_content = requests.get(pic_link).content
    filename = f'img_{i}.jpeg'
    with open(filename, 'wb+') as f:
        f.write(pic_content)
