import pandas as pd
import jieba.analyse
import time
import jieba
import jieba.posseg
import os, sys


def input(trainname):
    traindata = []
    with open(trainname, 'rb') as f:
        line = f.readline()
        count = 0
        while line:
            try:
                traindata.append(line)
                count += 1
            except:
                print("error:", line, count)
            line = f.readline()
    return traindata


start = time.clock()

filepath = './data/test_querylist.csv'
QueryList = input(filepath)

writepath = './data/test_querylist_writefile-1w.csv'
csvfile = open(writepath, 'w')

POS = {}
for i in range(len(QueryList)):
    # print (i)
    if i % 2000 == 0 and i >= 1000:
        print(i, 'finished')
    s = []
    str = ""
    words = jieba.posseg.cut(QueryList[i])  # 带有词性的精确分词模式
    allowPOS = ['n', 'v', 'j']
    for word, flag in words:
        POS[flag] = POS.get(flag, 0) + 1
        if (flag[0] in allowPOS) and len(word) >= 2:
            str += word + " "

    cur_str = str.encode('utf8')
    cur_str = cur_str.decode('utf8')
    s.append(cur_str)

    csvfile.write(" ".join(s) + '\n')
csvfile.close()

end = time.clock()
print("total time: %f s" % (end - start))