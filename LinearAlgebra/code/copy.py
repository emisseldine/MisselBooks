import numpy as np

a = np.array([1, 2, 3])
b = a        # b points to same array
b[0] = 0
print(a)     # changed
print(b)     

a = np.array([1, 2, 3])
b = a.copy() # To copy explicitly
b[0] = 0
print(a)     # unchanged
print(b)     
