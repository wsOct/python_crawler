import requests

# response = requests.get('https://httpbin.org/get')
# print(response)

# payload = {'key1': 'value1', 'key2': 'value2'}
# response = requests.get('https://httpbin.org/get', params = payload)
# # print(response.url)
# headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36'}
# response = requests.get('https://httpbin.org/get', params = payload, headers = headers)

# response = requests.get('https://httpbin.org/get/status/400')
# print(response.text)
# print(response.status_code)
# print(response.text)
# print('----------------------------')
# print(response.content)
# print('----------------------------')
# print(response.json())
# 服务器返回的响应头
# print(response.headers)
# 客户端发送给服务器的请求的头部
# print(response.request.headers)
# print(response.headers['content-type']) #不区分大小写
# print(response.headers.get('content-type'))

# cookies = dict(cookies_are='working')
# r = requests.get('http://httpbin.org/cookies', cookies=cookies)
# print(r.text)

# ----------------------POST-------------------------
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post("http://httpbin.org/post", data=payload)
# # print(r.text)

