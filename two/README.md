## Homework1.2：Ranked retrieval model 

（IR.py为简单实现，newIR.py为倒排索引实现，

该实验实现了两种方式的代码，

运行过程当中 原代码 与 优化后的代码 运算速度的差距较大能人为感受出来）

---
## 任务：
- 在Homework1.1的基础上实现最基本的Ranked retrieval model;
- Use SMART notation: lnc.ltc 
- 改进Inverted index
   + Input：a query (like Ron Weasley birthday) 
   + Output: Return the top K (e.g., K = 10) relevant tweets. 
## 注意：
- 对于tweets与queries使用相同的预处理
## 过程：
- 对tweets文档进行预处理（包括split、lower操作）
- 生成score矩阵（tf，idf依次对统计的词频进行处理）
## 关于nltk and jieba（仅测试不建议使用nltk）：
- 英文nltk and 中文jieba
- import nltk
- 引入nltk运行速度会很慢
- 对于string的预处理更优秀
   + 大小写转换
   + 标点符号的处理
   + 去除停用词（在英语中会有很多的词语不表达实际的意思，比如in/on/for等介词。）
   + 提取词干（在英文中有很多变形，比如cleaning/cleans/cleaned -> clean）
## 实现过程：
- tf-idf weighting
- 对数量的对数化，词的数量对检索的影响并不是成线性增长，而是根据信息熵的对数增长
- 根据出现词的文档的数量占所有文档的比例来确定该词的重要程度，例如"is"出现在所有文档中，其比重接近于0.而"science"出现在某几个文档中，比重非常高
- 对词的数量的向量空间的标准化，确保每个文档所有词的等比例影响，而不会因为一篇文档的内容重复出现两遍而影响最后索引的结果
## Weighting may differ in queries vs documents（处理方式在查询与文档中的差别）
-  lnc.ltc 
- Document: logarithmic tf (l as first character), no idf and cosine normalization 
- Query: logarithmic tf (l in leftmost column), idf (t in second column), no normalization 
## 代码实现具体细节：

- from collections import Counter 
- import collections 引入collections函数，目前已知的实现统计单词数量时间复杂度最低的函数，减少时间成本
- import json 引入json函数，实现text文本的分词功能，直接产生一个json形式的字典数组存储于python中
## 建立倒排索引结构
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
## 实现search查找函数的具体实现过程
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

## 输入：

"some"

## 输出：

{'28994302659006464': 0.5905702651118488, '29064561537585152': 0.6590986468703581, '29088769479016448': 0.36228806271957753, '29250575958810624': 0.36228806271957753, '29287792064339968': 0.8024951962617161..........................}


