import re

test_string = 'hello2018-12-01 heo helo hello helllo'
# result = re.search('l',test_string)
# result = re.findall('\d',test_string)
result = re.findall('hel?o',test_string)
# result = re.sub('-','=',test_string)
print(result)

