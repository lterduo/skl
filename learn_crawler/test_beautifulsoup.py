from bs4 import BeautifulSoup
#pip install beautifulsoup4
html = '''
'''
#soup = BeautifulSoup(html)
#with open('article.txt','rb') as f: #出现编码错误
with open('rmrb1.html','r',encoding='utf-8') as f:
    html = f.read()
soup = BeautifulSoup(html,'lxml')
# print(soup.prettify())
# riqi = soup.select('div #riqi_')
# riqi = soup.select('#riqi_')
riqi = soup.select('div[id=riqi_]')
riqi_s = ''
for i in riqi:
    riqi_s = i.get_text()
print(riqi_s)

