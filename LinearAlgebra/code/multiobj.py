import numpy as np
import matplotlib.pyplot as plt

def multi_lstsq(As, bs, lambdas):
    k = len(lambdas)
    A = np.concatenate([np.sqrt(lambdas[i])*np.array(As[i]) for i in range(k)])
    b = np.concatenate([np.sqrt(lambdas[i])*np.array(bs[i]) for i in range(k)])
    return np.linalg.lstsq(A,b, rcond=None)[0]

As = np.array([np.random.normal(size = (10,5)),
np.random.normal(size = (10,5))])
bs = np.vstack([np.random.normal(size = 10),
np.random.normal(size = 10)])
N = 200
lambdas = np.power(10, np.linspace(-4, 4, 200))
x = np.zeros((5,N))
J1 = np.zeros(N)
J2 = np.zeros(N)
for k in range(N):
    x[:,k] = multi_lstsq(As, bs, [1, lambdas[k]])
    J1[k] = np.linalg.norm(As[0]@x[:,k] - bs[0])**2
    J2[k] = np.linalg.norm(As[1]@x[:,k] - bs[1])**2
    

plt.ion()
# plot solution versus lambda
plt.plot(lambdas, x.T)
plt.xscale('log')
plt.xlabel('lambda')
plt.xlim((1e-4, 1e+4))
plt.legend(['y_1', 'y_2', 'y_3', 'y_4', 'y_5'], loc= 'upper right')
plt.show()

# plot two objectives versus lambda
plt.plot(lambdas, J1)
plt.plot(lambdas, J2)
plt.xscale('log')
plt.xlabel('lambda')
plt.xlim((1e-4, 1e+4))
plt.legend(['J_1','J_2'])
plt.show()

# plot tradeoff curve
plt.plot(J1,J2)
plt.xlabel('J_1')
plt.ylabel('J_2')

# add (single objective) end points to trade-off curve
x1 = np.linalg.lstsq(As[0], bs[0], rcond=None)[0]
x2 = np.linalg.lstsq(As[1], bs[1], rcond=None)[0]
J1 = [np.linalg.norm(As[0]@x1 - bs[0])**2,
np.linalg.norm(As[0]@x2 - bs[0])**2]
J2 = [np.linalg.norm(As[1]@x1 - bs[1])**2,
np.linalg.norm(As[1]@x2 - bs[1])**2]
plt.scatter(J1, J2)
plt.show()
