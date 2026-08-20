import numpy as np

A = np.array([[1,3,3],	#  Define matrix A
              [-3,-5,-3],
              [3,3,1]])
D, P = np.linalg.eig(A)	# Calculate eigenvalues (D) and eigenvectors (P) of matrix A              
Pinv = np.linalg.inv(P)	# Calculate the inverse of matrix P
print(P,"\n",						# Print the results
      np.diag(D),"\n",
      Pinv,"\n=",
      P @ np.diag(D) @ Pinv,"\n")

B = np.array([[3,0,0],	# Define matrix B
		   [0,2,1],
		   [0,0,2]])
D, P = np.linalg.eig(B)	# Calculate eigenvalues (D) and eigenvectors (P) of matrix B
Pinv = np.linalg.inv(P)	# Calculate the inverse of matrix P
print(P,"\n",						# Print the results
      np.diag(D),"\n",
      Pinv,"\n=",
      P @ np.diag(D) @ Pinv,"\n!=",
      B)
