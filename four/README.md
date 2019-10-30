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

## 具体实现代码细节：
### plot_document_clustering （部分代码）
引入sklearn的库进行具体的实现
- from sklearn.datasets import fetch_20newsgroups
- from sklearn.decomposition import TruncatedSVD
- from sklearn.feature_extraction.text import TfidfVectorizer
- from sklearn.feature_extraction.text import HashingVectorizer
- from sklearn.feature_extraction.text import TfidfTransformer
- from sklearn.pipeline import make_pipeline
- from sklearn.preprocessing import Normalizer
- from sklearn import metrics

#引入数据集

from sklearn.cluster import KMeans, MiniBatchKMeans

import logging

from optparse import OptionParser

import sys

from time import time

import numpy as np


logging.basicConfig(level=logging.INFO,format='%(asctime)s %(levelname)s %(message)s')

op = OptionParser()

op.add_option("--lsa",dest="n_components", type="int",help="Preprocess documents with latent semantic analysis.")

op.add_option("--no-minibatch",action="store_false", dest="minibatch", default=True,help="Use ordinary k-means algorithm (in batch mode).")

op.add_option("--no-idf",action="store_false", dest="use_idf", default=True,help="Disable Inverse Document Frequency feature weighting.")

op.add_option("--use-hashing",action="store_true", default=False, help="Use a hashing feature vectorizer")

op.add_option("--n-features", type=int, default=10000,
              help="Maximum number of features (dimensions)"
                   " to extract from text.")
op.add_option("--verbose",
              action="store_true", dest="verbose", default=False,
              help="Print progress reports inside k-means algorithm.")


print(__doc__)

op.print_help()


def is_interactive():
    
    return not hasattr(sys.modules['__main__'], '__file__')


argv = [] if is_interactive() else sys.argv[1:]

(opts, args) = op.parse_args(argv)

if len(args) > 0:
    
    op.error("this script takes no arguments.")
    
    sys.exit(1)


categories = [
    'alt.atheism',
    'talk.religion.misc',
    'comp.graphics',
    'sci.space',
]

print("Loading 20 newsgroups dataset for categories:")

print(categories)

dataset = fetch_20newsgroups(subset='all', categories=categories,
                             shuffle=True, random_state=42)

print("%d documents" % len(dataset.data))

print("%d categories" % len(dataset.target_names))

print()

labels = dataset.target

true_k = np.unique(labels).shape[0]

print("Extracting features from the training dataset "
      "using a sparse vectorizer")

t0 = time()

if opts.use_hashing:
    
    if opts.use_idf:
        
        # Perform an IDF normalization on the output of HashingVectorizer
        
        hasher = HashingVectorizer(n_features=opts.n_features,
                                   stop_words='english', alternate_sign=False,
                                   norm=None, binary=False)
        
        vectorizer = make_pipeline(hasher, TfidfTransformer())
    
    else:
        
        vectorizer = HashingVectorizer(n_features=opts.n_features,
                                       stop_words='english',
                                       alternate_sign=False, norm='l2',
                                       binary=False)
else:
    
    vectorizer = TfidfVectorizer(max_df=0.5, max_features=opts.n_features,
                                 min_df=2, stop_words='english',
                                 use_idf=opts.use_idf)
X = vectorizer.fit_transform(dataset.data)

print("done in %fs" % (time() - t0))

print("n_samples: %d, n_features: %d" % X.shape)

print()

if opts.n_components:

print("Performing dimensionality reduction using LSA")

t0 = time()


svd = TruncatedSVD(opts.n_components)

normalizer = Normalizer(copy=False)

lsa = make_pipeline(svd, normalizer)

    X = lsa.fit_transform(X)

    print("done in %fs" % (time() - t0))

    explained_variance = svd.explained_variance_ratio_.sum()
   
    print("Explained variance of the SVD step: {}%".format(
        int(explained_variance * 100)))

    print()

if opts.minibatch:
    
    km = MiniBatchKMeans(n_clusters=true_k, init='k-means++', n_init=1,
                         init_size=1000, batch_size=1000, verbose=opts.verbose)
else:
    
    km = KMeans(n_clusters=true_k, init='k-means++', max_iter=100, n_init=1,
                verbose=opts.verbose)

print("Clustering sparse data with %s" % km)

t0 = time()

km.fit(X)

print("done in %0.3fs" % (time() - t0))

print()

print("Homogeneity: %0.3f" % metrics.homogeneity_score(labels, km.labels_))

print("Completeness: %0.3f" % metrics.completeness_score(labels, km.labels_))

print("V-measure: %0.3f" % metrics.v_measure_score(labels, km.labels_))

print("Adjusted Rand-Index: %.3f"
      % metrics.adjusted_rand_score(labels, km.labels_))

print("Silhouette Coefficient: %0.3f"
      % metrics.silhouette_score(X, km.labels_, sample_size=1000))

print()


if not opts.use_hashing:
    
    print("Top terms per cluster:")

    if opts.n_components:
        
        original_space_centroids = svd.inverse_transform(km.cluster_centers_)
        
        order_centroids = original_space_centroids.argsort()[:, ::-1]
    
    else:
        
        order_centroids = km.cluster_centers_.argsort()[:, ::-1]

    terms = vectorizer.get_feature_names()

for i in range(true_k):

print("Cluster %d:" % i, end='')

for ind in order_centroids[i, :10]:

print(' %s' % terms[ind], end='')

print()

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
