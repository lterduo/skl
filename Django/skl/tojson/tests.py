# -*- coding: utf-8 -*-
from django.test import TestCase
import json
# Create your tests here.
#将一段话断句
def duanju(section):
    sentences = []
    sentence = ''
    i = 0
    while 1 == 1:
        i = i + 1
        # lenth1 = len(section)
        if section == '': #终止
            break
        if i == len(section):  # 防止最后一句没有断句标点而漏掉
            sentence = section
            sentences.append(sentence)
            break
        s = section[i-1]
        if s == "“":  # 继续循环找后引号
            j = 0
            for s1 in section:
                j = j + 1
                if s1 == "”":
                    if section[j - 2] in ('。', '！', '？', '…'):
                        sentence = section[0:j]
                        sentences.append(sentence)
                        section = section[j:]
                        i = 0
                        break
        if s in ('。', '！', '？'):  # 没有双引号后直接分句
            sentence = section[0:i]
            sentences.append(sentence)
            section = section[i:]
            i = 0
        if s == '…' and section[i] == '…':
            sentence = section[0:i+1]
            sentences.append(sentence)
            section = section[i+1:]
            i = 0
    return sentences
se = '……'
# se = '“一个人要坚定理想信念，一个企业也要坚持好自己的发展目标。”河钢集团党委书记、董事长于勇说，节目第十一集中习近平总书记关于理想信念的阐述，极大地坚定了河钢集团职工深入推进供给侧结构性改革、实现高质量发展的信心和决心。'
# se = '新修订的《中国共产党纪律处分条例》出台后，他和同事组织全州党员干部参与汉藏两种语言主题知识竞赛。“共产党员修身不是抽象的，而是具体的，应落实到学习、生活、工作的一言一行当中。”'
def duanju_wenzhang(temps):
    sentences = []
    temps = temps.split('\n')
    for s in temps:
        s = s.strip().strip('\n')  # 去掉空行
        if s == "":
            continue
        sens = duanju(s)  # 用断句函数处理s，返回[sentences]
        for sen1 in sens:
            sentences.append(sen1)
    return sentences


temps = '''chapter1

“一个人要坚定理想信念，     一个企业也要坚持好自己的发展目标。”河钢集团党委书记、董事长于勇说，节目第十一集中习近平总书记关于理想信念的阐述，极大地坚定了河钢集团职工深入推进供给侧结构性改革、实现高质量发展的信心和决心。
新修订的《中国共产党纪律处分条例》出台后，他和同事组织全州党员干部参与汉藏两种语言主题知识竞赛。“共产党员修身不是抽象的，而是具体的，应落实到学习、生活、工作的一言一行当中。”

第二章
1。2。
不是章节。'''
def test(temps):
    sens = duanju_wenzhang(temps)
    i = 0
    chaptername = ''
    location = [] #分段位置
    chap = []
    while i < len(sens):
        print("sens:   " + sens[i])
        # print(sens[i][-1])
        if sens[i][-1] not in ('。', '！', '？', '…','”'):
            location.append(i)
            print(i)
        i= i + 1
    if location[-1] == len(sens) - 1:  # 防止把最后一句没标点的判断为chapter
        location.pop()
    chaptername = ''
    if len(location) == 0:
        chap.append({"name": chaptername, "loc1": 0, "loc2": len(sens) - 1})
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

    sections = []
    chapters = []
    content=[]
    for c in chap:
        sentences = []  # 处理每段前先把sentences清空
        loc1 = c["loc1"]
        loc2 = c["loc2"]
        for sen1 in sens[loc1:loc2]:
            sentences.append({"page_num": 1, "is_cross_page": 'false', 'sentence:': sen1})
        sections = [{'name': '', "sentences": sentences}]
        chapters = [{'name': c["name"], 'section': sections}]
        content.append({"chapter": chapters})

    import codecs  # 中文问题
    data = {"chap":content}
    filename = 'test.txt'
    with codecs.open('test.json', 'w', 'utf-8') as f:
        json.dump(data, f, sort_keys=False , indent=4, separators=(',', ': '), ensure_ascii=False)
test(temps)
publish_time=' 2018年02月01日'
pubtime = publish_time[0:4] + publish_time[5:7] + publish_time[8:10]
print(pubtime)
# dic = [{'name':'lt','loc1':0,'loc2':8},{'name':'tt','loc1':9}]
# print(dic[1]['loc1'])
#os.path.basename()
import os
s = os.listdir('../json/')
s1 = 'rmrb2018112301.json'
print(s1[-4:])