import json
from collections import Counter
import collections
import math
import copy
import string

Index={}
num=0
length={}
for i in open('tweets.txt'):
    num=num+1
    dict = json.loads(i)
    array_text=(dict['text']).lower().split(" ")
    #array_username=dict['userName'].lower().split(" ")
    array=array_text#+array_username
    res = Counter(array)
    length[dict["tweetId"]]=0
    for j in res.keys():
        length[dict["tweetId"]]=+res[j] ** 2
    for j in res.keys():
        if(j not in Index.keys()):
            Index[j]=[]
        new={"tweetId":dict["tweetId"],"frequency":res[j]}
        Index[j].append(new)
#print(Index)

def search(str):
    score={}
    text=str.lower().split(" ")
    text=Counter(array)
    for i in text.keys():
        Wtq=math.log(num/len(Index[i]),10)*text[i]
        for j in Index[i]:
            if(j["tweetId"] not in score.keys()):
                score[j["tweetId"]]=0
            Wtd=math.log(1+j["frequency"], 10)
            score[j["tweetId"]]=score[j["tweetId"]]+Wtq*Wtd
    for i in score.keys():
        score[i]=score[i]/length[i]
    return score
print(search("some"))

