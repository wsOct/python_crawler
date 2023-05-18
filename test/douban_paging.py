import requests
from bs4 import BeautifulSoup

url = 'https://movie.douban.com/j/search_subjects'

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
params = {
    'tyep': 'movie',
    'tag': '热门',
    'page_limit': 50,
    'page_start': 0
}
res = requests.get(url, headers = headers, params=params)
movie_list = res.json()['subjects']
for movie in movie_list:
    # print(movie)
    print(movie.get('title'))
# print(movie_list)