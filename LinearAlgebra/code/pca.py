import numpy as np
from sklearn.datasets import load_iris

# iris_names = load_iris()['target_names']
# iris_types = load_iris()['target']
# iris_feature = load_iris()['feature_names']
iris_data = np.array(load_iris()['data'])

# print(iris_names)
# print(iris_types)
# print(iris_feature)
# print(iris_data)
#%%
X = iris_data
Z = np.array([(x-np.mean(x))/np.std(x) for x in X]) #The iris data is standardized

_,sigma,VT = np.linalg.svd(Z)                       #PCA of X is found by computing SVD of Z
print(sigma)
#%%
k = 2                                               #rank-2 singular reduction is selected
PCA = Z @ VT[:k]                                #projection onto rank-2 principal components
print(PCA)
