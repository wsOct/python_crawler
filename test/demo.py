import requests
from bs4 import BeautifulSoup
import pandas as pd
import pandas
#
# url = 'https://book.douban.com/tag/%E6%97%A5%E6%9C%AC%E6%96%87%E5%AD%A6'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42'}
# re = requests.get(url,headers = headers)
# # print(re.text)
# res = BeautifulSoup(re.text, 'html.parser')
#
#
# for a in res.select('#subject_list li'):
#     # print(a)
#     name=a.select('.info a')[0].get('title')
#     # for i in a.select('.info a'):
#     #     print(i.get)
#     print(name)
#     # a.find()
#     # print(a_res)
#     # print(a_res.get('title'))



# url = 'http://www.stats.gov.cn/sj/tjgb/nypcgb/qgnypcgb/202302/t20230206_1902103.html'
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42'}
# re = requests.get(url,headers = headers)
# # print(re.text)
# re.encoding = 'utf-8'
# res = BeautifulSoup(re.text, 'html.parser')
#
# columns = ['全国','东部地区','中部地区','西部地区','东北地区']
#
# t = res.find('table', class_="MsoNormalTable")
# # print(t)
# data_list = []
# prefix = ''
# for i, tr in enumerate(t.find_all('tr')[2:]):
#     data = list(tr.stripped_strings)
#     print(data)
#     if len(data) > 6:
#         data[0] = ''.join(data[:2])
#         data.pop(1)
#     if i in (5,6,7,9,10,11,14,15,16,17):
#         data[0] = f'{prefix}-{data[0]}'
#     if i in (4,8,13):
#         prefix = data[0]
#     else:
#         data_list.append(data)
# # print(data_list)
#
# print('--------------------------------')
#
# data_dict = {}
# for j, col in enumerate(columns):
#     if col not in data_dict:
#         data_dict[col] = {}
#     for i, dl in enumerate(data_list):
#         print(data_list[i])
#         data_dict[col][data_list[i][0]] = data_list[i][j+1]
#
# print(data_dict)
# print('---------------------------')
#
# df=pandas.DataFrame(data_dict)
# df.index.name = '指标'
# df.to_csv('data/demo.csv')
#
# # ['全国']['有火车站']=8.6
# # ['全国']['有码头']=7.7


url = 'http://www.stats.gov.cn/sj/zxfb/202302/t20230228_1919011.html'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.42'}
re = requests.get(url,headers = headers)
re.encoding = 'utf-8'
res = BeautifulSoup(re.text, 'html.parser')
# print(re.text)

t = res.find_all('table', class_="MsoNormalTable")[11]
# print(t)

columns = []
col_tr = t.find('tr')
for i, td in enumerate(col_tr.find_all('td')):
    col = ''.join(td.stripped_strings)
    if i == 2:
        col = '出口'+col
    elif i == 5:
        col = '进口' + col
    columns.append(col)
# print(columns)

data_list = []
for row in t.find_all('tr')[1:]:
    data = list(row.stripped_strings)
    data_list.append(data)
# print(data_list)
#
data_dict = {}
for i, col in enumerate(columns[1:]):
    if col not in data_dict:
        data_dict[str(col)] = {}
    for j, data in enumerate(data_list):
        data_dict[col][data[0]] = float(data[i+1])
# print(data_dict)
print(data_dict['出口额（亿元）'])
print(data_dict['出口额（亿元）']['东盟'])

df=pandas.DataFrame(data_dict)
df.index.name = columns[0]

print(df['出口额（亿元）'])
df.loc[:,'出口增长额'] = round(df['出口额（亿元）'] / (1+df['出口比上年增长（%）']/100), 2)
df.loc[:,'进出口总额'] = round((df['出口额（亿元）']/(df['占全部出口比重（%）']/100)) + (df['进口额（亿元）']/(df['占全部进口比重（%）']/100)), 2)
print(df)
new_df = df.sort_values(by = '进出口总额', ascending=False)
print(new_df)
new_df.to_csv('data/demo.csv')


