import numpy as np

x = np.array([2,-1,2])
print(np.linalg.norm(x))            #compute the norm of x

u = np.array([1.8, 2.0, -3.7, 4.7])
v = np.array([0.6, 2.1, 1.9, -1.4])
w = np.array([2.0, 1.9, -4.0, 4.6])
print(np.linalg.norm(u-v))          #compute the distance between u and v
print(np.linalg.norm(u-w))          #compute the distance between u and w
print(np.linalg.norm(v-w))          #compute the distance between v and w
