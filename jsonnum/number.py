import os
import json
import codecs

l = os.listdir()
number = 0
for l1 in l:
    number = '10'+ l1[4:-5]
    print(l1,'     ',number)
    load_dict = {}
    if l1[-4:] == 'json':
        with codecs.open(l1, 'r','utf-8') as load_f:
            load_dict = json.load(load_f)
            print(load_dict)
            load_dict['number'] = number
        with codecs.open(l1, "w",'utf-8') as dump_f:
            json.dump(load_dict, dump_f, sort_keys=False, indent=4, separators=(',', ': '), ensure_ascii=False)