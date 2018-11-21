import requests

payload = {
    'hello':'world'
}
url = 'http://httpbin.org/get'
# r = requests.get(url)
# r = requests.get(url,params = payload)
# r = requests.get(url,headers = payload)

url = 'http://httpbin.org/post'
r = requests.post(url,headers = payload,data = payload)
# print(r.url)
print(r.text)