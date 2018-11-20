from lxml import etree

#pip install lxml
#获取p标签，P一定要大写！！！

html = etree.parse("./test.html")
p = html.xpath('//div[@class="c_c"]/P')
# p = html.xpath('//P')
print(p)
print(type(p))
print(p[0].text)
for i in p:
    print(i.text)