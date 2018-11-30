import re

s = 'http://paper.people.com.cn/rmrb/html/2018-08/15/nw.D110000renmrb_20180815_1-07.htm'
s1 = re.findall('renmrb_\d\d\d\d\d\d\d\d_\d',s)
print(s1[0])

s2 = ['0','1','2','3']
s3 = ''.join(s2)
print(s3)