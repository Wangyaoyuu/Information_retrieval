## Homework1.2：Ranked retrieval model 

（IR.py为简单实现，newIR.py为倒排索引实现）
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

