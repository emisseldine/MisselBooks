import numpy as np

A = np.array([[-9,18,54],		# Define matrix A
              [-38,-49,-22]])

U,sigma,VT = np.linalg.svd(A)	# Perform Singular Value Decomposition (SVD)
print(U,"\n",							# Print the results
      np.diag(sigma),"\n",
      VT.T,"\n")
