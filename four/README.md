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

n_digits: 10, 	 n_samples 1797, 	 n_features 64
__________________________________________________________________________________
init		time	inertia	homo	compl	v-meas	ARI	AMI	silhouette

k-means++	0.38s	69432	0.602	0.650	0.625	0.465	0.621	0.146

random   	0.23s	69694	0.669	0.710	0.689	0.553	0.686	0.147

PCA-based	0.04s	70804	0.671	0.698	0.684	0.561	0.681	0.118
__________________________________________________________________________________

## document_clustering:

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

Cluster 3: god com people jesus don say morality think sgi article
