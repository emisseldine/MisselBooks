import numpy as np

A = np.array([[0, 1, -3, -1, -2],# 4x5 matrix called A, which is implemented as an array of arrays;
              [1, 1, 2, 4, 3],   # each array represents a row of A;
              [3, 7, -6, 8, 1],  # each entry corresponds to a scalar in that row.
              [0, -1, 3, 4, -4]])
print(A)

m,n = A.shape                    # shape returns (m, n), where m = rows, n = columns
print(A.shape)
print('m =', m)
print('n =', n)

print("The 2nd row: ", A[1])     # A[i] return i-th row, so A[1] grabs the second row
print("The 3rd column: ", A[:,2])# the colon grabs all rows, hence grabs column 3 (index 2)
print("a_(1,3) = ", A[0,2])      # A[i, j] grabs single entry at row i, column j. 

# Each list inside np.column_stack is treates as a column vector.
# This is the counter-wise counterpart to np.array, which stacks rows.
B = np.column_stack([[0,1,3,0], [1,1,7,-1], [-3,2,-6,3], [-1,4,8,4], [-2, 3, 1, -4]])
print(B)
