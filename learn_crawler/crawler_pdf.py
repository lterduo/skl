import requests
import re
from bs4 import BeautifulSoup
from pdf_save import pdf_save
headers = {
    'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
}
url = 'http://paper.people.com.cn/rmrb/html/2018-08/02/nbs.D110000renmrb_07.htm'

web_data = requests.get(url, headers=headers)
web_data.encoding = 'utf-8' #解决乱码问题
soup = BeautifulSoup(web_data.text, 'lxml')
banmian = soup.select('.ban_t > div > ul > li ') #注意一定要加空格
pdf = soup.select('.ban_t > div > ul > li > a')
print(banmian[0].text.strip())
banmian0 = banmian[0].text.strip().split('\n')[0].strip()  #取出第一行，去掉空格，判断是否为'07版:理论'
print('banmian0:' ,banmian0)
print(pdf[0])
if banmian0 == '07版:理论':
    pdffile = pdf[0].get('href')
    print(pdffile)
    '''  http://paper.people.com.cn/rmrb/page/2018-08/18/07/rmrb2018081807.pdf
                               ../../../page/2018-01/02/07/rmrb2018010207.pdf'''
    pdffile = "http://paper.people.com.cn/rmrb/"+ re.findall('page.*',pdffile)[0]
    pdf_save(pdffile,headers)

    urls7 = soup.select('#titleList > ul > li > a ')
    for i in urls7:
        print(i.get('href'))
        '''
        http://paper.people.com.cn/rmrb/html/2018-08/02/nbs.D110000renmrb_07.htm
        http://paper.people.com.cn/rmrb/html/2018-08/02/nw.D110000renmrb_20180802_1-07.htm
                                                nw.D110000renmrb_20180802_1-07.htm'''
        s = re.findall('.*\d\d/\d\d/', url)[0] + i.get('href')
        print(s)
