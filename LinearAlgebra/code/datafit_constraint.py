import numpy as np

def lstsq_constraint(A, b, C, d):
    ATA = A.T @ A
    CT = (C.T).reshape((len(ATA), -1))
    n = len(CT[0])
    KKT = np.block([[2*ATA, CT], [CT.T, np.zeros((n, n))]])
    KKTb = np.hstack((2*A.T @ b, d))
    return np.linalg.lstsq(KKT, KKTb, rcond=None)[0][:-n]

n = 3 #degree of polyonmial
M = 100 #number of data points per half
xleft = np.random.random(M) - 1
xright = np.random.random(M)
x = np.hstack([xleft, xright])
y = np.power(x,3) - x + 0.4/(1+25*np.power(x,2)) + 0.05*np.random.normal(size = 2*M)

A = np.block([[np.vander(xleft,n+1), np.zeros((M,n+1))], 
                [np.zeros((M,n+1)), np.vander(xright,n+1)]])
D = np.block([[np.zeros(n), 1, np.zeros(n), -1], 
                [np.zeros(n-1), 1, 0, np.zeros(n-1), -1, 0]])
coeffs = lstsq_constraint(A,y,D,np.zeros(2))

# Graphing
import matplotlib.pyplot as plt
xpl_left = np.linspace(-1, 0, 2*M)
ypl_left = np.vander(xpl_left, n+1) @ coeffs[:n+1]
xpl_right = np.linspace(0, 1, 2*M)
ypl_right = np.vander(xpl_right, n+1) @ coeffs[n+1:]
plt.scatter(x, y)
plt.plot(xpl_left, ypl_left, 'red')
plt.plot(xpl_right, ypl_right, 'green')
plt.show()
