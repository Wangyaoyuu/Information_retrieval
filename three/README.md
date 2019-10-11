## Homework1.3：IR Evaluation
---
## 任务：
- 在Homework1.1的基础上实现最基本的Ranked retrieval model;
- Use SMART notation: lnc.ltc 
- 实现以下指标评价，并对HW1.2检索结果进行评价 
   + Mean Average Precision (MAP)
   + Mean Reciprocal Rank (MRR)
   + Normalized Discounted Cumulative Gain (NDCG)
## 过程：
- 实际上根据已有的代码，只需要编程MRR评价
- result.txt为标准结果，并且已经通过process.py的筛选（筛选掉多余文本的tweetid）
- qrels.txt为待测试的结果，并且MAP与NDCG的程序框架已有
- 修改MAP与NDCG的程序框架，得到MRR的评测结果
