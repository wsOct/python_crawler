'''
Python 基础
'''
a = 123.123
# 保留2位小数，四舍五入
b = round(a, 2)
# class的定义和使用
# 类首字符大写，如CuteDog
class Dog:
# 构造函数，定义示例对象的属性，如小狗的名字，年龄
    def __init__(self, name):
        self.name = name
    # 方法，缩进，写在类里面
    def bark(self, words):
    # 方法具体的代码
        print(f'我叫{self.name}, 我想说{words}')

# 创建对象，类名(参数)
dog1 = Dog("puppy")
# 获取对象属性，对象名.属性
print(dog1.name)
# 调用方法，对象名.方法名(方法参数)
dog1.bark('天气真好')

# 字典的操作
data_dict = {}
# 遍历字典，使用.items(), 返回字典的keys和values, 所以for key, value
for key, value in data_dict.items():
    print(key)
    print(value)

'''
csv文件操作
'r' 代表读，'w'代表覆盖写，'w+'或者'a'代表追加写，'wb+'代表以二进制内容格式追加写入
'''
import csv

filename = 'data/test.csv'

# 读取
with open("data/students.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    # 一行行读取并打印
    for row in reader:
        print(row)

# 写入
data = [
    ('name', 'age', 'gender'),
    ('Jane', '16', 'F'),
    ('Tom', '14', 'M'),
    ('Leon', '15', 'M'),
]

# 覆盖写入
with open('data/student-1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    # 一下子写入多行
    writer.writerows(data)
    # 也可以一行行写入, 使用writerow
    # for d in data:
    #     writer.writerow(d)

# 追加写入
with open('data/students.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    # 一下子写入多行
    writer.writerows(data)

# 按照字典的样式写入csv文件
# title是csv文件的列标题
titles = ('城市','天气现象', '风向风力','最高温度','最低温度')
content = []
with open(filename, 'w', encoding='utf-8', newline='') as f:
    dwriter = csv.DictWriter(f, titles)
    # 先写入列标题头
    dwriter.writeheader()
    # 写入剩下的内容，content的格式如下(由字典组成的列表)：[{},{},{}] 具体参考weahter_practice.py文件
    dwriter.writerows(content)


'''
爬虫基础
'''
import requests

# 记得url里有http:// 或者 https://
url = 'url'
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
# params中存放请求的参数，比如用户名, 密码，还有分页信息
# 比如下面的params, 其中的page_limit, page_start这两个参数名是从网页请求中获得的
# params = {
#     'tyep': 'movie',
#     'tag': '热门',
#     'page_limit': 50,
#     'page_start': 0
# }
params = {'key1': 'value1', 'key2': 'value2'}
# 如果发现没有内容返回，首先检查是否返回200
response = requests.get(url, headers = headers, params = params)
# 设置utl-8格式，为了正确现实中文内容
response.encoding = 'utf-8'
# 返回的html内容，这是最常使用的
print(response.text)
# 返回二进制格式内容
print(response.content)
# 按照json格式打印返回的内容，一般是知道返回内容为json格式后才会这么使用
print(response.json())
# 服务器返回的响应头
print(response.headers)

# bs4 使用
from bs4 import BeautifulSoup
res = BeautifulSoup(response.text, 'html.parser')
# 获取标签内文本, .test, .string
print(res.a.text)
print(res.a.string)
# 获取标签内属性 .attrs
print(res.a.attrs)
# 获取指定属性值, get('')
print(res.a.attrs.get('href'))
print(res.a.get('href'))
# 获取子节点
for i in res.p.children:
    print(i)
# 获取标签内部所有的元素
print(res.p.contents)
# 获取标签的父标签
print(res.p.parent)
print(res.p.parent.name)
# 获取最上级节点
for i in res.p.parents:
    print(i)

# find返回满足条件的第一个标签，find_all, select返回的是列表
# 查找指定标签名的标签 默认只找符合条件的第一个
print(res.find(name='p'))
# 查找具有某个特定属性的标签 默认只找符合条件的第一个
print(res.find(name='p', id='title'))
# 为了解决关键字冲突 会加下划线区分
print(res.find(name='p', class_='title'))
# 使用attrs参数 直接避免冲突
print(res.find(name='p', attrs={'class': 'title'}))


# 查询某一个标签，查找的结果是一个列表
print(res.find_all('a'))
for link in res.find_all('a'):
    print(link.get('href'))

# 查找class含有title的标签
print(res.select('.title'))
# 查看class含有sister标签内部所有的后代span
print(res.select('.title b'))
# 查找id等于title的标签
print(res.select('#title'))
# 返回下面所有的字符串.stripped_strings
print(res.select('.title').stripped_strings)
# 可以将字符串组合成一个列表
print(list(res.select('.title').stripped_strings))
# 可以将查找条件多级共同使用：如查找标签id=subject_id 下面的所以li标签：res.select('#subject_id li')
# 由于find和select返回的是列表，所以可以直接通过索引下标访问返回的内容，如：res.select('#subject_id li')[0]


'''
pandas基础
'''
# 基础内容参考文件：pandas_practice.py, pandas_csv_weather.py
# 注意数据清洗的部分，判空和去重
import pandas as pd

data_dict = {}
# columns是csv的列标题，如['国家和地区','出口额（亿元）','出口比上年增长（%）','占全部出口比重（%）']
columns = []

df=pd.DataFrame(data_dict)
# columns[0]是'国家和地区'，把他作为索引index的name，避免写入csv文件的时候第一行第一列为空，导致逗号开头
df.index.name = columns[0]
# 按照某列排序
# axis 如果axis=0，那么by=“列名”； 如果axis=1，那么by=“行名”, 默认值为0
# ascending: True则升序，默认为True
new_df = df.sort_values(by = '进出口总额', axis=0, ascending=False)
# pandas写入csv
new_df.to_csv('data/demo.csv')

