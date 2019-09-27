Homework1.2：Ranked retrieval model
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
-   
