import numpy as np
from sklearn.datasets import load_iris

iris_data = np.array(load_iris()['data'])

z = np.array([iris_data[0], iris_data[50], iris_data[100]])
k = len(z)
x = np.array([5.5,2.3,4.,1.3])

distances = np.zeros(k)

for i in range(k):
    distances[i] = np.linalg.norm(x-z[i])
    
print(np.argmin(distances)) 
#Solution is z[1], that is x is likely a versicolor
