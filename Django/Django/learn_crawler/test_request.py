import requests
#pip install requests

# payload = {
#     'hello':'world'
# }
# url = 'http://httpbin.org/get'
# # r = requests.get(url)
# # r = requests.get(url,params = payload)
# # r = requests.get(url,headers = payload)

# url = 'http://httpbin.org/post'
# r = requests.post(url,headers = payload,data = payload)
# #传json
# import json
# r = requests.post(url,data = json.dumps(payload))
# #传文件
# f = {
#     'files':open('test.txt','rb')
# }
# r = requests.post(url,files = f)
# #传 cookies
# url = 'http://httpbin.org/cookies'
# c = {
#     "cookies_are":'working'
# }
# # c = dict(cookies_are='working')
# r = requests.get(url,cookies=c)
# print(r.txt)

# # print(r.url)
# print(r.text)

# #超时
# r = requests.get(url,timeout = 0.001)
# r = requests.get(url,timeout = 1000)

# #持久会话
# s = requests.Session()
# s.get('http://httpbin.org/cookies/set/sessioncookies/12345')
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

#代理
proxies = {
    'https':'http://1.2.3.4:5'
}
r = requests.post('https://www.baidu.com',proxies = proxies)
print(r.status_code)