# from bs4 import BeautifulSoup
# import requests
# import pandas as pd
#
# head = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
# }
#
# baseurl = "https://movie.douban.com/top250"
# list = []
#
# for i in range(0, 250, 25):
#
#     params = {'start': i}
#     res = requests.get(url=baseurl, headers=head, params=params)
#     connect = res.text
#     res = BeautifulSoup(connect, 'html.parser')
#     movies = res.select('.grid_view li')
#
#     for i in movies:
#         info = {
#             "title": "",
#             "score": 0,
#             "num": 0
#         }
#         info['title'] = i.find(name='span', class_='title').text
#         info['score'] = i.find(class_='rating_num').text
#         info['num'] = i.select(".star span")[-1].text.replace("人评价", "")
#         list.append(info)
#
# print(list)
# movie_info = pd.DataFrame(list, index=range(1, len(list)+1))
# movie_info.to_csv('data/douban_movie.csv')

# from bs4 import BeautifulSoup
# import requests
# import csv
# import pandas as pd
#
# titles =('城市','天气现象', '风向风力','最高温度','最低温度')
#
# def parsePage(url):
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
#     }
#     rep =requests.get(url=url, headers=headers)
#     rep.encoding='utf-8'
#     html =rep.text
#     soup =BeautifulSoup(html,'html.parser')
#     conMidtab =soup.find('div',class_='conMidtab')
#     tables = conMidtab.find_all('table')
#     lst =[] #保存数据
#     for table in tables:
#         trs =table.find_all('tr')[2:]
#         # for tr in trs: # 这里的话 直辖市正常，省会第一个数据会错
#         for index,tr in enumerate(trs): #enumerate返回两个值，一个是index一个是tr
#             #获取所有的td td代表城市的气温风力数据
#             tds =tr.find_all('td')
#             # 第一个是省会城市/直辖市信息，需要跳过
#             begin = 1 if index==0 else 0# td下标起始位置
#             city_td = tds[begin]
#             info ={}
#             city = list(city_td.stripped_strings)[0]
#             # 取天气现象
#             temp_at=list(tds[begin+1].stripped_strings)[0]
#             # 取风向风力
#             temp_wind=tds[begin+2]
#             temp_w_list=list(temp_wind.stripped_strings)
#             temp_w = temp_w_list[0]+temp_w_list[1]
#             # 取最高气温
#             temp_td_high=tds[begin+3]
#             temp_high = list(temp_td_high.stripped_strings)[0]
#             # 取最低温度
#             temp_td_low =tds[-2] #最低温度数据在倒数第二个
#             temp_low =list(temp_td_low.stripped_strings)[0]
#
#             info['城市']=city
#             info['天气现象']=temp_at
#             info['风向风力']=temp_w
#             info['最高温度']=temp_high
#             info['最低温度'] =temp_low
#             lst.append(info)
#     return lst
#
#
# def writeData(lst):
#     with open('城市温度.csv','w',encoding='utf-8',newline='') as f:
#         dwriter =csv.DictWriter(f, titles)
#         dwriter.writeheader()
#         dwriter.writerows(lst)
#
#
# def spliteCSV(filename):
#     data = pd.read_csv(filename)
#     data.loc[:, '温差'] = data['最高温度'] - data['最低温度']
#     data_normal = data.loc[data['温差']<10]
#     data_abnormal = data.loc[data['温差']>=10]
#     print(data_normal)
#     print('---------------------')
#     print(data_abnormal)
#
#
#
# def main():
#     url ='http://www.weather.com.cn/textFC/hb.shtml'
#     lst=parsePage(url)
#     writeData(lst)
    # spliteCSV('城市温度.csv')
#
#
# if __name__ == '__main__':
#     main()


# 	saveToCSV

# class practice
from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

titles =('城市','天气现象', '风向风力','最高温度','最低温度')


class Spider:
    def __init__(self, url, user_agent, filename):
        self.url = url
        self.user_agent = user_agent
        self.filename = filename

    def getHTMLContent(self):
        headers = {'User-Agent': self.user_agent}
        rep = requests.get(self.url, headers = headers)
        rep.encoding = 'utf-8'
        return rep.text

    def getSoup(self):
        html = self.getHTMLContent()
        return BeautifulSoup(html, 'html.parser')

    def parsePage(self):
        soup = self.getSoup()
        conMidtab = soup.find('div', class_='conMidtab')
        tables = conMidtab.find_all('table')
        lst = []  # 保存数据
        for table in tables:
            trs = table.find_all('tr')[2:]
            # for tr in trs: # 这里的话 直辖市正常，省会第一个数据会错
            for index, tr in enumerate(trs):  # enumerate返回两个值，一个是index一个是tr
                # 获取所有的td td代表城市的气温风力数据
                tds = tr.find_all('td')
                # 第一个是省会城市/直辖市信息，需要跳过
                begin = 1 if index == 0 else 0  # td下标起始位置
                city_td = tds[begin]
                info = {}
                city = list(city_td.stripped_strings)[0]
                # 取天气现象
                temp_at = list(tds[begin + 1].stripped_strings)[0]
                # 取风向风力
                temp_wind = tds[begin + 2]
                temp_w_list = list(temp_wind.stripped_strings)
                temp_w = temp_w_list[0] + temp_w_list[1]
                # 取最高气温
                temp_td_high = tds[begin + 3]
                temp_high = list(temp_td_high.stripped_strings)[0]
                # 取最低温度
                temp_td_low = tds[-2]  # 最低温度数据在倒数第二个
                temp_low = list(temp_td_low.stripped_strings)[0]

                info['城市'] = city
                info['天气现象'] = temp_at
                info['风向风力'] = temp_w
                info['最高温度'] = temp_high
                info['最低温度'] = temp_low
                lst.append(info)
        return lst

    def saveToCSV(self, content):
        with open(self.filename, 'w', encoding='utf-8', newline='') as f:
            dwriter = csv.DictWriter(f, titles)
            dwriter.writeheader()
            dwriter.writerows(content)


if __name__ == '__main__':
    # url = 'http://www.weather.com.cn/textFC/hb.shtml'
    # user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'
    # filename = '城市温度class.csv'
    # sp = Spider(url, user_agent, filename)
    # sp.saveToCSV(sp.parsePage())

    test_dict = {'a':5, 'd':3, 'c':4}
    print(test_dict)

    # 按照值排序
    value_sort_list = sorted(test_dict.items(), key=lambda x: x[1], reverse=False)
    print(f'按照值：{value_sort_list}')
    # 按照键排序
    key_sort_list = sorted(test_dict.items(), key=lambda x: x[0], reverse=False)
    print(f'按照键：{key_sort_list}')

    # 按照值排序后变字典
    new_dict={}
    for i in value_sort_list:
        new_dict[i[0]] =i[1]
    # print(new_dict)
    new_dict = {i[0]:i[1] for i in value_sort_list}
    print(new_dict)
    # 按照键排序后变字典
    new_dict = {i[0]: i[1] for i in key_sort_list}
    print(new_dict)


# def add(x,y):
#     return x+y
#
#     lambda x,y: x+y
#
#
#
