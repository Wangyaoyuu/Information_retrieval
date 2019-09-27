import json
from collections import Counter
import collections
import math

Index={}          #    总索引
Paper_number=0    #标记文章总数量
Word_frequency={} #“有该词”文章的数量

for i in open('tweets.txt'):
    Paper_number=Paper_number+1
    index={}      #针对每个tweets单独的索引
    dict = json.loads(i)
    array_text=(dict['text']).lower().split(" ")
    array_username=dict['userName'].lower().split(" ")
    array=array_text+array_username
    res = Counter(array)
    res = sorted(res.items(), key=lambda x: x[0])
    #print(res)
    indexed={}
    for i in res():
        if(i[0] not in Word_frequency.keys()):
            Word_frequency[i[0]]=0
        Word_frequency[i[0]]=Word_frequency[i[0]]+1
        indexed[i[0]]=math.log(1+i[1], 10)#计算tft
    Index[dict["tweetId"]]=indexed


for i in Index.keys():
    for j in Index[i].keys():
        Index[i][j]=Index[i][j]*math.log(Paper_number/Word_frequency[j],10)#计算dft

#正规化
for i in Index.keys():
    Sum=0
    for j in Index[i].keys():
        Sum+= Index[i][j] ** 2
    Sum=math.sqrt(Sum)
    for j in Index[i].keys():
        Index[i][j]=Index[i][j]/Sum

#对查询的字符串进行处理
def find(str):
    str=str.lower().split(" ")
    str_num = Counter(str)
    str_num_sorted = sorted(str_num.items(), key=lambda x: x[0])
    query={}
    for i in str_num_sorted:
        query[i[0]]=math.log(1+i[1], 10)*math.log(Paper_number/Word_frequency[i[0]],10)

    #正规化
    Sum=0
    for i in query.keys():
        Sum += query[i] ** 2
    Sum = math.sqrt(Sum)
    for i in query.keys():
        query[i]=query[i]/Sum
    return query

#计算评分最高的n
def compute(paper,query,num):
    q=dict(query)
    score_dic={}
    for i in paper.keys():
        p = dict(paper[i])
        score=0
        while len(p) > 0 and len(q) > 0:
            if (p[0] == q[0]):
                score += p[0]*q[0]
                p.remove(p[0])
                q.remove(q[0])
            if p[0] < q[0]:
                p.remove(p[0])
            if p[0] > q[0]:
                q.remove(q[0])
        score_dic[i]=score

    score_dic = sorted(score_dic.items(), key=lambda x: x[1],reverse=True)
    return score_dic[0:num]



query=find('')
compute(Index,query,num=10)
