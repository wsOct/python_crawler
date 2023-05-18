from bs4 import BeautifulSoup

# 构造一个网页数据
html_doc = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="title">
            <b>The Dormouse's story</b>
        </p>

        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a>
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
        and they lived at the bottom of a well.</p>

        <p class="story">...</p>
    </body>
</html>
"""

# soup = BeautifulSoup("<html>A Html Text</html>", "html.parser")
# soup.prettify()  # prettify 有括号和没括号都可以
# 获取标签
res = BeautifulSoup(html_doc, 'html.parser')
print(res.a)
# 获取标签的名称
print(res.a.name)
# 获取标签内文本
print(res.a.text)
print(res.a.string)
# 获取标签内属性
print(res.a.attrs)
# 获取指定属性值
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


