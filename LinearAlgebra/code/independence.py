import numpy as np

A = np.array([[1,3,-3],
              [2,1,4],
              [3,-2,13]])
Asub = A[:,:-1] # Is v[2] a linear combination of v[0] and v[1]?
x = np.linalg.lstsq(Asub,A[:,2])[0] #solve the linear system
print(Asub@x)                       #notice this product is 1*v[2]
print(np.round(x,0),'\n')           #3*v[0] - 2*v[1] = 1*v[0]
