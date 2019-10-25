Homework2：Clustering with sklearn 
---
## Datasets:
- sklearn.datasets.load_di gits
- sklearn.datasets.fetch_2 0newsgroups
## 任务：
- 测试sklearn中的多种聚类算法在两个数据集上的聚类效果
## Evaluation：
- Normalized Mutual Information (NMI) 
- Homogeneity: each cluster contains only members of a single class 
- Completeness: all members of a given class are assigned to the same cluster
## 过程：
- 运行sklearn中的两个样例
- A demo of K-Means clustering on the handwritten digits data 
- Clustering text documents using kmeans 
- 运行结果：


## K-means：

在这个例子中，我们比较了k-means在运行时和结果质量方面的各种初始化策略。应用不同的聚类质量度量来判断聚类标签与基本真实的拟合优度。 

n_digits: 10, 	 n_samples 1797, 	 n_features 64
__________________________________________________________________________________
init		time	inertia	homo	compl	v-meas	ARI	AMI	silhouette

k-means++	0.38s	69432	0.602	0.650	0.625	0.465	0.621	0.146

random   	0.23s	69694	0.669	0.710	0.689	0.553	0.686	0.147

PCA-based	0.04s	70804	0.671	0.698	0.684	0.561	0.681	0.118
__________________________________________________________________________________

## document_clustering:

这是一个展示了如何使用scikit learn使用一个单词包方法按主题对文档进行聚类的示例。使用scipy.sparse矩阵来存储特性，而不是标准的numpy数组。

可以使用两种特征提取方法：

1.使用内存词汇表（python dict）将最频繁的单词映射到特征索引，从而计算单词出现频率（稀疏）矩阵。然后，使用逆文档频率（idf）向量在语料库上逐个收集特征来重新加权单词频率。

2.将单词出现的次数散列到一个固定的可能有冲突的维度空间。然后将字数向量规范化为每个向量的l2范数等于1

k-means（和minibatch k-means）对特征缩放非常敏感，在这种情况下，idf权重有助于通过与20个新闻组数据集的类标签分配所提供的“基本事实”进行比较，提高聚类质量。k-means优化一个非凸目标函数，很可能会陷入局部最优。为了获得良好的收敛性，需要使用独立随机init进行多次运行。

n_samples: 3387, n_features: 10000

Homogeneity: 0.422

Completeness: 0.433

V-measure: 0.428

Adjusted Rand-Index: 0.311

Silhouette Coefficient: 0.006

Top terms per cluster:

Cluster 0: space alaska nasa moon launch shuttle sky just gov aurora

Cluster 1: graphics image henry toronto software images file files gif gov

Cluster 2: com access posting nntp host digex university article net sandvik

Cluster 3: god com people jesus don say morality think sgi article.
