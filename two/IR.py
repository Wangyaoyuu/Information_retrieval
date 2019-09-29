import json
from collections import Counter
import collections
import math
import copy
import nltk
from nltk.corpus import stopwords
import nltk.stem
import string

Index={}          #    总索引
Paper_number=0    #标记文章总数量
Word_frequency={} #“有该词”文章的数量

for i in open('tweets.txt'):
    Paper_number=Paper_number+1
    index={}      #针对每个tweets单独的索引
    dict = json.loads(i)

    lower= (dict['text']).lower()
    remove = str.maketrans('','',string.punctuation)
    without_punctuation = lower.translate(remove)
    tokens = nltk.word_tokenize(without_punctuation)
    without_stopwords = [w for w in tokens if not w in stopwords.words('english')]
    s = nltk.stem.SnowballStemmer('english')  # 参数是选择的语言
    cleaned_text = [s.stem(ws) for ws in without_stopwords]

    '''array_username=dict['userName'].lower().split(" ")
    array=array_text+array_username
    '''
    res = Counter(cleaned_text)
    res = sorted(res.items(), key=lambda x: x[0])
    #print(res)
    indexed={}
    for i in res:
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
        if(i[0] not in Word_frequency.keys()):
            query[i[0]]=0
        else:
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

    score_dic={}
    for i in paper.keys():
        q = copy.deepcopy(query)
        p = copy.deepcopy(paper[i])
        score=0
        while len(p) > 0 and len(q) > 0:
            key1=list(p.keys())[0]
            key2=list(q.keys())[0]
            if (key1 == key2):
                score =score + p[key1]*q[key2]
                del p[key1]
                del q[key2]
                #p.remove(p[key1])
                #q.remove(q[key2])
            if key1 < key2:
                del p[key1]
            if key1 > key2:
                del q[key2]
        score_dic[i]=score

    score_dic = sorted(score_dic.items(), key=lambda x: x[1],reverse=True)
    ans=score_dic[0:num]
    print(ans)
    return ans



print(Index)
query=find('some')
print(query)
compute(Index,query,num=10)
