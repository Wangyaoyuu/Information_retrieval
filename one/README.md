Homework1.1：Inverted index and Boolean Retrieval Model
---
## 任务：
- 使用我们介绍的方法，在tweets数据集上构建inverted index; 
- 实现Boolean Retrieval Model，使用TREC 2014 test topics进行测试； 
- Boolean Retrieval Model： 
   + Input：a query (like Ron and Weasley) 
   + Output: print the qualified tweets. 
   + 支持and, or ,not 
## 注意：
- 对于tweets与queries使用相同的预处理
## 过程：
- 对tweets文档进行预处理（包括split、lower操作）
- 倒排索引（生成索引的字典，并记录下索引的长度）
- 查询优化（实现两个word的and、or 和 多个word的and、or优化查询）
