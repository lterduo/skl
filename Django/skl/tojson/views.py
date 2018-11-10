# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from .duanju import *

def index(request):
    return render(request, 'index.html')

def add(request):
    title = request.GET['title']
    title = title.strip()
    title_sub = request.GET['title_sub']
    title_sub = title_sub.strip()
    author_name1 = request.GET['author_name1']
    author_name1 = author_name1.strip()
    author_org1 = request.GET['author_org1']
    author_org1 = author_org1.strip()
    author_name2 = request.GET['author_name2']
    author_name2 = author_name2.strip()
    author_org2 = request.GET['author_org2']
    author_org2 = author_org2.strip()
    author_name3 = request.GET['author_name3']
    author_name3 = author_name3.strip()
    author_org3 = request.GET['author_org3']
    author_org3 = author_org3.strip()
    author = [{'name':author_name1,'organization':author_org1}]
    if author_name2 != '':
        author.append({'name':author_name2,'organization':author_org2})
    if author_name3 != '':
        author.append({'name':author_name3,'organization':author_org3})
    abstract = request.GET['abstract']
    source_name = request.GET['source_name']
    source = {'name':source_name,"issue": "", "category": "报刊"}
    publish_time = request.GET['publish_time']
    publish_time = publish_time.strip()
    temps = request.GET['content']
    total_size = len(temps) + len(title) + len(abstract)
    sentences = []
    sections = []
    chapters = []
    content = []
    # temps = temps.split('\n')
    # for s in temps:
    #     s = s.strip().strip('\n') # 去掉空行
    #     if s  == "":
    #         continue
    #     sens = duanju(s) #用断句函数处理s，返回[sentences]
    #     sentences = [] #处理每段前先把sentences清空
    #     for sen1 in sens:
    #         sentences.append({"page_num": 1, "is_cross_page": 'false', 'sentence:': sen1})
    #
    #     sections = [{'name': '', "sentences": sentences}]
    #     chapters = [{'name': '', 'section': sections}]
    #     content.append({"chapter": chapters})
    sens = duanju_wenzhang(temps)
    location = []  # 分段位置
    chap = [] #取chapter名称和位置
    i = 0
    while i < len(sens):
        print("sens:   " + sens[i])
        if sens[i][-1] not in ('。', '！', '？', '…', '”'):
            location.append(i)
        i = i + 1
    if len(location) != 0:
        if location[-1] == len(sens)-1:#防止把最后一句没标点的判断为chapter
            location.pop()
    chaptername = ''
    if len(location) == 0:
        chap.append({"name": chaptername, "loc1": 0, "loc2": len(sens)-1})
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

    for c in chap:
        sentences = []  # 处理每段前先把sentences清空
        loc1 = c["loc1"]
        loc2 = c["loc2"]
        for sen1 in sens[loc1:loc2]:
            sentences.append({"page_num": 1, "is_cross_page": 'false', 'sentence:': sen1})

        sections = [{'name': '', "sentences": sentences}]
        chapters = [{'name': c["name"], 'section': sections}]
        content.append({"chapter": chapters})

    publish_time1 = publish_time[0:4] + '-'+publish_time[5:7] + '-'+publish_time[8:10]
    data = {'number':'','title':title,'title_en':'','title_sub':title_sub,\
    'author':author,'source':source,"keywords":"","abstract":abstract,"abstract_en":"","references":"",\
    "publish_time":publish_time1,"base_category":"重要报刊",'base_sub_category ':source_name, \
    "subject_category": {"first_class": "","second_class": "","third_class": ""},\
    'contents':content,"total_page_size": 1,"total_size": total_size,"url": ""}

    import os
    pubtime = publish_time[0:4] + publish_time[5:7] + publish_time[8:10]
    print(pubtime,'    ',publish_time)
    s = os.listdir('./json/')
    #rmrb2018112301.json
    i = 1
    for s1 in s:
        if s1[4:12] == pubtime and s1[-4:] =='json':
            i = i + 1
    import codecs  # 中文问题

    filename = './json/' +'rmrb'+ str(pubtime) + '0'+ str(i) + '.json'
    with codecs.open(filename, 'w', 'utf-8') as f:
        json.dump(data, f, sort_keys=False , indent=4, separators=(',', ': '), ensure_ascii=False)

    return render(request, 'seccess.html')