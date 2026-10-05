import numpy as np

A = np.column_stack([[1,2,3],
              [3,1,-2],
              [-3,4,13]])
if len(A[0])==np.linalg.matrix_rank(A): #does number of pivots equal columns?
  print('linearly independent')
else:
  print('linearly dependent')

Asub = A[:,:-1] # Is v[2] a linear combination of v[0] and v[1]?
x = np.linalg.lstsq(Asub,A[:,2],rcond=None)[0] #solve the linear system
print(Asub@x)                       #notice this product is 1*v[2]
print(np.round(x,0),'\n')           #3*v[0] - 2*v[1] = 1*v[0]
