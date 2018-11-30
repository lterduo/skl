import datetime
from bs4 import BeautifulSoup
import requests
import re
from pdf_save import pdf_save
from crawler_content import *

#爬取第七版，如果是理论版，获取下层网址，并保存pdf； 调用json_save爬取下层网址并保存json
def get_info(url,headers):
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'  # 解决乱码问题
    soup = BeautifulSoup(web_data.text, 'lxml')
    banmian = soup.select('.ban_t > div > ul > li ')  # 注意一定要加空格
    pdf = soup.select('.ban_t > div > ul > li > a')
    print(banmian[0].text.strip())
    banmian0 = banmian[0].text.strip().split('\n')[0].strip()  # 取出第一行，去掉空格，判断是否为'07版:理论'
    print('banmian0:', banmian0)
    print(pdf[0])
    if banmian0 == '07版:理论':
        #写pdf
        pdffile = pdf[0].get('href')
        print(pdffile)
        '''  http://paper.people.com.cn/rmrb/page/2018-08/18/07/rmrb2018081807.pdf
                                   ../../../page/2018-01/02/07/rmrb2018010207.pdf'''
        pdffile = "http://paper.people.com.cn/rmrb/" + re.findall('page.*', pdffile)[0]
        pdf_save(pdffile, headers)
        #获取具体地址，爬取内容并保存json
        urls7 = soup.select('#titleList > ul > li > a ')
        for s in urls7:
            print(s.get('href'))
            '''
            http://paper.people.com.cn/rmrb/html/2018-08/02/nbs.D110000renmrb_07.htm
            http://paper.people.com.cn/rmrb/html/2018-08/02/nw.D110000renmrb_20180802_1-07.htm
                                                            nw.D110000renmrb_20180802_1-07.htm'''
            s = re.findall('.*\d\d/\d\d/', url)[0] + s.get('href')
            print(s)
            json_save(s,headers)


#按时间获取url
daystart = datetime.datetime.strptime("2018-01-01", "%Y-%m-%d").date()
daystop = datetime.datetime.strptime("2018-01-31",'%Y-%m-%d').date()
urls = []
while daystart <= daystop:
    day = daystart.strftime("%Y-%m/%d")
    s = 'http://paper.people.com.cn/rmrb/html/'+day+'/nbs.D110000renmrb_07.htm'
    urls.append(s)
    daystart = daystart + datetime.timedelta(days=1)

headers = {
    'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
}
for url in urls:
    get_info(url,headers)