import numpy as np

# computes the rank-k singular reduction of the matrix A, namely A_k, given the SVD of A, parameters U, sigma (list of singular values), VT, and the desired rank k
reduced_svd = lambda U,sigma,VT,k : U[:,:k] @ np.diag(sigma[:k]) @ VT[:k,:]

A = np.array([[-9,18,54],		# Define matrix A
              [-38,-49,-22]])

U,sigma,VT = np.linalg.svd(A)	# Perform Singular Value Decomposition (SVD)
print(U,"\n",							# Print the results
      np.diag(sigma),"\n",
      VT.T,"\n")
for k in range(np.linalg.matrix_rank(A)+1):
    print(k, reduced_svd(U,sigma,VT,k),"\n")
