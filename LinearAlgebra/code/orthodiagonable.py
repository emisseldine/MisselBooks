import numpy as np

A = np.array([[3,-2,4],		# Define matrix A
              [-2,6,2],
              [4,2,3]])
D, P = np.linalg.eigh(A)	# Calculate eigenvalues (D) and eigenvectors (P) of matrix A
print(P,"\n",							# Print the results
      np.diag(D),"\n",
      P.T,"\n=",
      P @ np.diag(D) @ P.T,"\n")
