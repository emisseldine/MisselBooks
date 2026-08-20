import numpy as np

B = np.array([[1,2,3,4],[5,6,7,8]]) #2x4 block
C = np.array([[9,10],[11,12]]) #2x2 block
D = np.array([[13,14,15,16],[17,18,19,20],[21,22,23,24]]) #3x4 block
E = np.array([[25,26],[27,28],[29,30]]) #3x2 block

# 2x2 block matrix
A = np.block([[B,C],[D,E]])
print(A.shape,"\n", A, "\n")
print(A.T.shape,"\n", A.T, "\n")
print("Main Diagonal = ", np.diag(A), "\n")

A_2x15 = np.reshape(A,(2,15))
print(A_2x15.shape,"\n", A_2x15, "\n")
