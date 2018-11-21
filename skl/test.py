# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
import json
from .duanju import duanju

def index(request):
    return render(request, 'index.html')

def add(request):
    title = request.GET['title']
    title_sub = request.GET['title_sub']
    author_name = request.GET['author_name']
    author_org = request.GET['author_org']
    author = {'name':author_name,'organization':author_org}
    abstract = request.GET['abstract']
    source_name = request.GET['source_name']
    source = {'name':source_name,"issue": "", "category": "期刊"}
    publish_time = request.GET['publish_time']
    temps = request.GET['content']
    sentences = []
    sections = []
    chapters = []
    contents = []
    temps = temps.split('\n')
    for s in temps:
        # 去掉空行
        s = s.strip().strip('\n')
        if s  == "":
            continue
        sens = duanju(s)
        for sen1 in sens:
            sentences.append({"page_num": 1, "is_cross_page": 'false', 'sentence:': sen1})
        sections = []
        chapters = []
        sections=[{'name':'',"sentences": sentences}]
        chapters=[{'name':'','section':sections}]
        contents.append({"chapter": chapters})

    data = {'number':'','title':title,'title_en':'','title_sub':title_sub,\
    'author':author,'source':source,"keywords":"","abstract":abstract,"abstract_en":"","references":"",\
    "publish_time":publish_time,"base_category":"重要报刊",'base_sub_category ':source_name, \
    "subject_category": {"first_class": "","second_class": "","third_class": ""},\
    'contents':contents}

    import codecs  # 中文问题
    filename = './json/' + str(author_name) + '-' + str(title) + '.json'
    with codecs.open(filename, 'w', 'utf-8') as f:
        json.dump(data, f, sort_keys=False , indent=4, separators=(',', ': '), ensure_ascii=False)

    return render(request, 'seccess.html')

