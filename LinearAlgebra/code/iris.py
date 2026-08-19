import numpy as np
from sklearn.datasets import load_iris

iris_names = load_iris()['target_names']
iris_types = load_iris()['target']

iris_feature = load_iris()['feature_names']
iris_data = np.array(load_iris()['data'])

print(iris_names)
print(iris_types)
print(iris_feature)
print(iris_data)
