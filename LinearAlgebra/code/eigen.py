import numpy as np

A = np.array([[-2,4,-2,1],
              [-15,29,-13,23],
              [-30,44,-19,34],
              [0,-4,2,-3]])
print(np.linalg.eigvals(A))
