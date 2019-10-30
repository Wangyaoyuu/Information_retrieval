## Homework1.3：IR Evaluation
---
## 任务：
- 实现以下指标评价，并对HW1.2检索结果进行评价 
   + Mean Average Precision (MAP)
   + Mean Reciprocal Rank (MRR)
   + Normalized Discounted Cumulative Gain (NDCG)
## 过程：
- 实际上根据已有的代码，只需要编程MRR评价
- result.txt为标准结果，并且已经通过process.py的筛选（筛选掉多余文本的tweetid）
- qrels.txt为待测试的结果，并且MAP与NDCG的程序框架已有
- 修改MAP与NDCG的程序框架，得到MRR的评测结果
## 注：
- qrels.txt和result.txt文件略大，由于网络问题，无法上传
## 报告部分：
MRR (Mean Reciprocal Rank, 平均倒数排名)

是一个国际上通用的对搜索算法进行评价的机制，即第一个结果匹配，分数为1，第二个匹配分数为0.5，第n个匹配分数为1/n，如果没有匹配的句子分数为0。最终的分数为所有得分之和。

MAP（Maximum A Posteriori）

统计学中，MAP为最大后验概率（Maximum a posteriori）的缩写。估计方法根据经验数据获得对难以观察的量的点估计。它与最大似然估计中的 Fisher方法有密切关系，但是它使用了一个增大的优化目标，这种方法将被估计量的先验分布融合到其中。所以最大后验估计可以看作是规则化（regularization）的最大似然估计。

DCG （Discounted Cumulative Gain)

DCG的英文全称是Discounted cumulative gain，它是一个衡量搜索引擎算法的指标。
搜索引擎一般采用PI（per item）的方式进行评测，简单地说就是逐条对搜索结果进行分等级的打分。假设我们现在在Google上搜索一个词，然后得到5个结果。我们对这些结果进行3个等级的区分：Good（好）、Fair（一般）、Bad（差），然后赋予他们分值分别为3、2、1，假定通过逐条打分后，得到这5个结果的分值分别为3、2 、1 、3、 2。
使用DCG这个统计方法有两个前提：
1.在搜索结果页面，越相关的结果排在越前面越好
2.在PI标注时，等级高的结果比等级低的结果好，即Good要比Fair好、Fair要比Bad好。

## 代码实现具体细节：

- 搜索倒数结构的实现

def MRR_eval(qrels_dict, test_dict, k = 100):

    MRR_result = []
    
    for query in qrels_dict:
    
        test_result = test_dict[query]
        
        true_list = set(qrels_dict[query].keys())
        
        # print(len(true_list))
        
        # length_use = min(k, len(test_result), len(true_list))
        
        length_use = min(k, len(test_result))
        
        if length_use <= 0:
        
            print('query ', query, ' not found test list')
            
            return []

        i=0
        
        for doc_id in test_result[0: length_use]:
        
            i += 1
            
            if doc_id in true_list:
            
                MRR=1/i
                
                MRR_result.append(1/i)
                
                print('query', query, ', MRR: ',MRR )
                
                break
                
    return np.mean(MRR_result)
## 结果：

# AP
query: 171 ,AP: 0.9498040597601832
query: 172 ,AP: 0.3412969283276451
query: 173 ,AP: 0.9978136200716846
query: 174 ,AP: 0.5675347800347801
query: 175 ,AP: 0.38910505836575876
query: 176 ,AP: 0.8274129338771129
query: 177 ,AP: 0.1135214393434572
query: 178 ,AP: 0.46296296296296297
query: 179 ,AP: 0.9711632590609263
query: 180 ,AP: 0.07688990983214608
query: 181 ,AP: 1.0

query: 182 ,AP: 0.19305019305019305
query: 183 ,AP: 0.425531914893617
query: 184 ,AP: 0.5847126267573457
query: 185 ,AP: 0.5654754181248164
query: 186 ,AP: 0.9866600790513834
query: 187 ,AP: 0.9092983086630102
query: 188 ,AP: 0.8035238199833755
query: 189 ,AP: 0.3757153614704371
query: 190 ,AP: 0.9351466010296691
query: 191 ,AP: 0.7974447915680067
query: 192 ,AP: 1.0
query: 193 ,AP: 1.0

query: 194 ,AP: 0.9770716619981326
query: 195 ,AP: 0.2695417789757412
query: 196 ,AP: 0.9615384615384616
query: 197 ,AP: 0.9989192038173244
query: 198 ,AP: 1.0
query: 199 ,AP: 0.2375296912114014
query: 200 ,AP: 0.3731378521601115
query: 201 ,AP: 0.37037037037037035
query: 202 ,AP: 0.5954593161482736
query: 203 ,AP: 0.7136992484156964
query: 204 ,AP: 0.8990918268187825
query: 205 ,AP: 0.5676666645725785
query: 206 ,AP: 0.9103122265208956
query: 207 ,AP: 0.9607505734124471
query: 208 ,AP: 0.303951367781155
query: 209 ,AP: 0.16447368421052633
query: 210 ,AP: 0.9635344674818358
query: 211 ,AP: 0.25226035126159885
query: 212 ,AP: 0.5650377539391153
query: 213 ,AP: 0.398406374501992
query: 214 ,AP: 0.530280317997534
query: 215 ,AP: 0.30120481927710846
query: 216 ,AP: 0.4269032815167319
query: 217 ,AP: 0.625

query: 218 ,AP: 0.30303030303030304
query: 219 ,AP: 0.25524197520567754
query: 220 ,AP: 0.6138226621145667
query: 221 ,AP: 0.1988071570576541
query: 222 ,AP: 0.30126376980342995
query: 223 ,AP: 0.9940746736049804
query: 224 ,AP: 0.5178732378732379
query: 225 ,AP: 0.9920063553263518
MAP = 0.6148422817122279

# NDCG
query 171 , NDCG:  0.9398543518229351
query 172 , NDCG:  0.9522319284335552
query 173 , NDCG:  0.8787194969898994
query 174 , NDCG:  0.4307012038436227
query 175 , NDCG:  0.7551540943184635
query 176 , NDCG:  0.7642638365304593
query 177 , NDCG:  0.32326557235468056
query 178 , NDCG:  0.7937060310666214
query 179 , NDCG:  0.9092261961802077
query 180 , NDCG:  0.384578000794295
query 181 , NDCG:  0.9083280342057781
query 182 , NDCG:  0.877578756577689
query 183 , NDCG:  0.9016059435415619
query 184 , NDCG:  0.7456215828590065
query 185 , NDCG:  0.5651704753561145
query 186 , NDCG:  0.9174314725664987
query 187 , NDCG:  0.8568815395907531
query 188 , NDCG:  0.834462410887587
query 189 , NDCG:  0.11401721726142679
query 190 , NDCG:  0.9087219839232467

query 191 , NDCG:  0.8333343147042753
query 192 , NDCG:  0.8691210155951211
query 193 , NDCG:  0.870741244990849
query 194 , NDCG:  0.9169177532845512
query 195 , NDCG:  0.7066199310564784
query 196 , NDCG:  0.9661544464181389
query 197 , NDCG:  0.9366145863919296
query 198 , NDCG:  0.8656740779203047
query 199 , NDCG:  0.8150900615927696
query 200 , NDCG:  0.8347275757365947
query 201 , NDCG:  0.8802919036981388
query 202 , NDCG:  0.8455666016685564
query 203 , NDCG:  0.5568543671092813
query 204 , NDCG:  0.8819018257589796
query 205 , NDCG:  0.8851402460821168
query 206 , NDCG:  0.8077691566644618
query 207 , NDCG:  0.8228677166265421
query 208 , NDCG:  0.795113510490801
query 209 , NDCG:  0.6682277350065139
query 210 , NDCG:  0.9144104200186212
query 211 , NDCG:  0.046597135518310455
query 212 , NDCG:  0.8308594376764563
query 213 , NDCG:  1.0

query 214 , NDCG:  0.6916266592407506
query 215 , NDCG:  0.5070939854213776
query 216 , NDCG:  0.7612721037995507
query 217 , NDCG:  0.7675078383310092
query 218 , NDCG:  0.8302203434012001
query 219 , NDCG:  0.498155912259978
query 220 , NDCG:  0.5674800702438964
query 221 , NDCG:  0.9266372064962487
query 222 , NDCG:  0.5087328728028815
query 223 , NDCG:  0.9063275712084274
query 224 , NDCG:  0.3773185814513307
query 225 , NDCG:  0.9706077927297266
NDCG = 0.756819929645465

# MRR
query 171 , MRR:  0.5
query 172 , MRR:  1.0
query 173 , MRR:  1.0
query 174 , MRR:  0.2
query 175 , MRR:  1.0
query 176 , MRR:  0.16666666666666666
query 177 , MRR:  1.0
query 178 , MRR:  1.0
query 179 , MRR:  1.0
query 180 , MRR:  0.14285714285714285
query 181 , MRR:  1.0
query 182 , MRR:  1.0

query 183 , MRR:  1.0
query 184 , MRR:  1.0
query 185 , MRR:  0.3333333333333333
query 186 , MRR:  1.0
query 187 , MRR:  0.5
query 188 , MRR:  1.0
query 189 , MRR:  0.16666666666666666
query 190 , MRR:  0.5
query 191 , MRR:  1.0
query 192 , MRR:  1.0
query 193 , MRR:  1.0
query 194 , MRR:  1.0
query 195 , MRR:  1.0
query 196 , MRR:  1.0
query 197 , MRR:  1.0
query 198 , MRR:  1.0
query 199 , MRR:  1.0
query 200 , MRR:  1.0
query 201 , MRR:  1.0
query 202 , MRR:  1.0
query 203 , MRR:  1.0
query 204 , MRR:  0.5
query 205 , MRR:  1.0

query 206 , MRR:  0.3333333333333333
query 207 , MRR:  1.0
query 208 , MRR:  1.0
query 209 , MRR:  1.0
query 210 , MRR:  1.0
query 211 , MRR:  0.0625
query 212 , MRR:  1.0
query 213 , MRR:  1.0
query 214 , MRR:  0.25
query 215 , MRR:  1.0
query 216 , MRR:  1.0
query 217 , MRR:  1.0
query 218 , MRR:  1.0
query 219 , MRR:  0.3333333333333333
query 220 , MRR:  0.3333333333333333
query 221 , MRR:  1.0
query 222 , MRR:  0.3333333333333333
query 223 , MRR:  1.0
query 224 , MRR:  0.2
query 225 , MRR:  1.0
MRR = 0.79737012987013
