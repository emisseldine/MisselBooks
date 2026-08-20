import numpy as np

def lstsq_constraint(A, b, C, d):   #|Ax-b|^2 is the objective to minimize
    ATA = A.T @ A                   #subject to the constraint Cx=d
    CT = (C.T).reshape((len(ATA), -1))
    p = len(CT[0])
    KKT = np.block([[2*ATA, CT], [CT.T, np.zeros((p, p))]])
    KKTb = np.hstack((2*A.T @ b, d))
    return np.linalg.solve(KKT, KKTb)[:-p]

#Linear Quadratic Regulator
def lqr(A, B, C, a, b, T, rho):     
    n = len(A)
    Bmtx,Cmtx = B.reshape((n,-1)),C.reshape((-1,n))
    m,p = len(Bmtx[0]),len(Cmtx)
    Ablock = np.block([
        [np.kron(np.eye(T+1),Cmtx),np.zeros((p*(T+1),m*T))], 
        [np.zeros((m*T,n*(T+1))),np.sqrt(rho)*np.eye(m*T)]])
    Cblock = np.block([
            [np.kron(np.eye(T,T+1),A) - np.kron(np.eye(T,T+1,1),np.eye(n)),
                  np.kron(np.eye(T),Bmtx)], 
            [np.kron(np.vstack([np.eye(1,T+1,0),np.eye(1,T+1,T)]),np.eye(n)),
                  np.zeros((2*n,m*T))]])
    dblock = np.concatenate((np.zeros(n*T),a,b))
    z = lstsq_constraint(Ablock,np.zeros(len(Ablock)),Cblock,dblock)
    
    x = np.array([z[i*n:(i+1)*n] for i in range(T+1)])
    u = np.array([z[n*(T+1)+(i)*m: n*(T+1)+(i+1)*m] for i in range(T)])
    y = np.array([C @ xt for xt in x])
    return x, u, y 

A = np.array([
    [0.855, 1.161, 0.667],
    [0.015, 1.073, 0.053],
    [-0.084, 0.059, 1.022]])
B = np.array([-0.076, -0.139, 0.342])
C = np.array([0.218, -3.597, -1.683])
a = np.array([0.496, -0.745, 1.394])
b = np.zeros(3)
T = 100

import matplotlib.pyplot as plt
## No Control ##
Xno = np.zeros((T+1, len(a)))  #initialize Xno
Xno[0] = a
for k in range(T):             #simulation without control 
    Xno[k+1] = A @ Xno[k]
# plot output vector y_t (there is no control vector u_t)
Yno = C @ Xno.T
plt.plot(np.arange(T+1),Yno)
plt.xlabel("t\n No Control")
plt.ylabel("y_t")
plt.ylim(-0.1,0.5)
plt.show()

## Linear Quadratic Control ##
rhos = [1, 0.2, 0.05]
#initialize sequences X (states), U (input/control), Y (output)
X,U,Y = np.zeros((len(rhos),T+1,3)),np.zeros((len(rhos),T,1)),np.zeros((len(rhos),T+1))
for k in range(len(rhos)):
    X[k],U[k],Y[k] = lqr(A,B,C,a,b,T,rhos[k])
    # plot input vectors u_t
    plt.plot(np.arange(T),U[k])
    plt.xlabel('t\n rho = ' + str(rhos[k]))
    plt.ylabel('u_t')
    plt.ylim(-0.5,0.6)
    plt.show()
    # plot output vectors y_t
    plt.plot(np.arange(T+1),Y[k])
    plt.xlabel('t\n rho = ' + str(rhos[k]))
    plt.ylabel('y_t')
    plt.ylim(-0.1,0.5)
    plt.show()

#Linear State Feedback Control
K = np.zeros(3)             #initialize/compute state-feedback gain matrix
for  i in range(3):
    X,U,Y = lqr(A,B,C,np.eye(1,3,i)[0],b,T,1)
    K[i] = U[0]
print(K)

ABK = A + np.outer(B,K)    #form matrix A + BK, outer product used to avoid having to reshape vectors as matrices
Xst = np.zeros((T+1, 3))   #initialize Xst
Xst[0] = a
for k in range(T):         #simulation with state-feedback control
    Xst[k+1] = ABK @ Xst[k]
yst = C @ Xst.T
# plot input vectors u_t
plt.plot(np.arange(T), [K @ x for x in Xst[:-1]])
plt.xlabel("t\n State Feedback Control")
plt.ylabel('u_t')
plt.ylim(-0.5,0.6)
plt.show()
 # plot output vectors y_t   
plt.plot(np.arange(T+1), yst)
plt.xlabel("t\n State Feedback Control")
plt.ylabel("y_t")
plt.ylim(-0.1,0.5)
plt.show()
