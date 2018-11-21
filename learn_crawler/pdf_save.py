import requests
import re

path = './pdf/'
def pdf_save(url,headers):
    data = requests.get(url, headers=headers)
    file_name = re.findall('rmrb\d*.pdf', url)
    print(file_name)
    if file_name:
        fp = open(path + file_name[0], 'wb')
        fp.write(data.content)
        fp.close()

# url = 'http://paper.people.com.cn/rmrb/page/2018-08/18/07/rmrb2018081807.pdf'
# headers = {
#     'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
# }
# pdf_save(url,headers)
