import numpy as np

a = np.array([1, 2, 3])                     # default cast as int
a_float = a.astype(float)                   # recast as float
print(a_float)
print(np.array([1.1,2.7,3.14]).astype(int)) # cast as int initially
