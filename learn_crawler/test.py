import datetime
from bs4 import BeautifulSoup
import requests
import re
import json
from duanju import *


def json_save(url, headers):  # 爬取正文，生成json并保存
    web_data = requests.get(url, headers=headers)
    web_data.encoding = 'utf-8'  # 解决乱码问题
    soup = BeautifulSoup(web_data.text, 'lxml')

    number = 0
    title = soup.h1.string.strip()
    print('title:', title)
    title_sub = soup.h2.string
    if title_sub is None:
        title_sub = ''
    s = soup.h4.string
    author_name = []
    if s is not None:
        for s1 in s.split(' '):
            if s1 != '':
                author_name.append(s1)
    s = soup.select('.lai')[0].text


    publish_time = re.findall('\d\d\d\d年\d\d月\d\d日', s)[0]
    print('publish_time:', publish_time)
    s = soup.select('#ozoom > p ')
    content = ''
    abstract = ''  # 暂时没碰到啊，不知道怎么取
    author_org = ''
    for s1 in s:
        s2 = s1.text.strip()
        if s2[0:4] == '（作者为' or s2[0:5] == '（作者单位' or s2[0:6] == '（作者分别为':
            author_org = s2[1:-2]
            print('author_org:', author_org)
        else:
            content = content + '\n' + s2
    source_name = '人民日报'
    source = {'name': source_name, "issue": "", "category": "报刊"}
    total_size = len(content) + len(title) + len(abstract)

    sentences = []
    sections = []
    chapters = []
    contents = []
    sens = duanju_wenzhang(content)
    location = []  # 分段位置
    chap = []  # 取chapter名称和位置
    i = 0
    while i < len(sens):
        print("sens: " + str(i) + '  ' + sens[i])
        if sens[i][-1] not in ('。', '！', '？', '…', '”'):
            location.append(i)
            print('location 出现：sens[i][-1]:' + sens[i][-1])
        i = i + 1
    if len(location) != 0:
        if location[-1] == len(sens) - 1:  # 防止把最后一句没标点的判断为chapter
            location.pop()
    chaptername = ''
    if len(location) == 0:
        # 测试，最后一句娶不到
        # chap.append({"name": chaptername, "loc1": 0, "loc2": len(sens) - 1})
        chap.append({"name": chaptername, "loc1": 0, "loc2": len(sens) })
    j = 0

    if len(location) != 0:
        for i in location:
            if i == 0:
                chaptername = sens[0]
                continue
            chap.append({"name": chaptername, "loc1": j, "loc2": i})
            j = i
            chaptername = sens[i]
        chap.append({"name": chaptername, "loc1": j, "loc2": len(sens)})
    print('chap:   ',chap)
    for c in chap:
        sentences = []  # 处理每段前先把sentences清空
        loc1 = c["loc1"]
        loc2 = c["loc2"]
        for sen1 in sens[loc1:loc2]:
            sentences.append({"page_num": 1, "is_cross_page": False, 'sentence': sen1})

        sections = [{'name': '', "sentences": sentences}]
        chapters = [{'name': c["name"], 'section': sections}]
        contents.append({"chapter": chapters})
    author = []
    for i in author_name:
        author.append({'name': i, 'organization': author_org})
    publish_time1 = publish_time[0:4] + '-' + publish_time[5:7] + '-' + publish_time[8:10]
    data = {'number': '', 'title': title, 'title_en': '', 'title_sub': title_sub, \
            'author': author, 'source': source, "keywords": "", "abstract": abstract, "abstract_en": "",
            "references": "", \
            "publish_time": publish_time1, "base_category": "重要报刊", 'base_sub_category': source_name, \
            "subject_category": {"first_class": "", "second_class": "", "third_class": ""}, \
            'contents': contents, "total_page_size": 1, "total_size": total_size, "url": ""}
    import os
    pubtime = publish_time[0:4] + publish_time[5:7] + publish_time[8:10]
    number = int()
    print(pubtime, '    ', publish_time)
    s = os.listdir('./json/')
    # rmrb2018112301.json
    i = 1
    for s1 in s:
        if s1[4:12] == pubtime and s1[-4:] == 'json':
            i = i + 1
    import codecs  # 中文问题
    filename = './json/' + 'rmrb' + str(pubtime) + '0' + str(i) + '.json'
    data['number'] = '10' + pubtime + '0' + str(i)
    with codecs.open(filename, 'w', 'utf-8') as f:
        json.dump(data, f, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)


headers = {
    'User-Agent': 'Windows Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0'
}
json_save('http://paper.people.com.cn/rmrb/html/2018-01/05/nw.D110000renmrb_20180105_1-07.htm', headers)