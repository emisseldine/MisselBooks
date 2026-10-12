import numpy as np

Q,R = np.linalg.qr([[0,-1],[1,3]])
print(Q)
print(R,'\n')


sign = np.sign(np.diag(R)) #Extract the signs of the diagonal entries of R
Q, R = Q*sign, R*sign      #Change the negative signs in Q,R
print(Q)
print(R,'\n')
