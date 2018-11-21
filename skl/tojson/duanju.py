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

#将一篇文章断句
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

se = '……'
# se = '“一个人要坚定理想信念，一个企业也要坚持好自己的发展目标。”河钢集团党委书记、董事长于勇说，节目第十一集中习近平总书记关于理想信念的阐述，极大地坚定了河钢集团职工深入推进供给侧结构性改革、实现高质量发展的信心和决心。'
# se = '新修订的《中国共产党纪律处分条例》出台后，他和同事组织全州党员干部参与汉藏两种语言主题知识竞赛。“共产党员修身不是抽象的，而是具体的，应落实到学习、生活、工作的一言一行当中。”'
se1 = duanju(se)
print(list(se1))
