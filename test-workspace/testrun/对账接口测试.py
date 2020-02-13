#coding=utf-8

def replaceParam(source,txt):
    #先把数据库数据按照分号划分
    replaceparam_array =source.split(';')
    for replaceparam in replaceparam_array:
        replaceparam1 = replaceparam.split(',')
        element1 = replaceparam1[0]
        element2 = replaceparam1[1]
        a=txt.replace('x',element1)
        a=a.replace('y',element2)
        print(a)

if __name__=='__main__':
    f = open('C:\\Users\\luqy\\Desktop\\a.sql', 'r')
    lines = f.readlines()
    # print(lines)
    lines2 = ''.join(lines)
    a = lines2.replace('\n', '')
    b = a.replace('insert into WSSBFSB_DDXX (ORDERID, QUERYID)values (', '')
    b = b.replace(');', ';')
    b = b.replace('\'', '')
    b = b.replace(', ', ',')

    replace = replaceParam(b,'1|@|20180501|@|085312|@|20180501|@|410000|@|1|@|110110189509182679|@|x|@|y|@|2|@|156|@|102.54|@||@|2|@|20180502|@|41000011245432|@|公司一二')
    # print(b)

    # -*- coding: utf-8 -*-