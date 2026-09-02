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
                  np.zeros((2*n, m*T))]])
    dblock = np.concatenate((np.zeros(n*T),a,b))
    z = lstsq_constraint(Ablock,np.zeros(len(Ablock)),Cblock,dblock)
    
    x = np.array([z[i*n:(i+1)*n] for i in range(T+1)])
    u = np.array([z[n*(T+1)+(i)*m: n*(T+1)+(i+1)*m] for i in range(T)])
    y = np.array([C @ xt for xt in x])
    return x, u, y 

A = np.array([
    [-0.62682592,  0.86754857, -0.77785297,  1.1847016 ],
    [ 0.53826718, -0.0222891,   0.22633482,  1.22321942],
    [ 0.04207144,  0.19602775,  0.72701903, -0.49410962],
    [ 0.18873804, -1.1783307,  -0.7322315,  -0.05291547]])
B = np.array([
    [ 0.92462685,  0.41120187,  1.90732642],
    [ 0.62059493,  0.09580603,  1.25624125],
    [-0.67694362, -0.5089959,  -0.23056128],
    [ 0.21934901, -1.25904487, -0.95703989]])
C = np.eye(4)
a = np.array([1,2,3,4])
b = np.zeros(4)
T = 40

import matplotlib.pyplot as plt
### Task 1 - No Control ###
      #calculate the dynamical system with no control
Xno = #Xno[t] is the state vector at time t without control

# Graphing #
for i in range(len(a)):
    plt.plot(range(T+1),Xno[:,i])
plt.legend(['(x_t)_1','(x_t)_2','(x_t)_3','(x_t)_4'],loc='lower right')
plt.xlabel("t\n No Control")
plt.ylabel("(x_t)_i")
plt.show()

### Task 2 - Linear Quadratic Control ###
rho = 100
    #calculate the dynamical system with linear quadratic control
X = #X[t] is the state vector at time t with linear quadratic control
U = #U[t] is the control vector at time t with linear quadratic control

# Graphing #
for i in range(len(a)):
    plt.plot(range(T+1), X[:,i])
plt.legend(['(x_t)_1','(x_t)_2','(x_t)_3','(x_t)_4'],loc='lower right')
plt.xlabel("t\n Linear Quadratic Control")
plt.show()
for i in range(len(B[0])):
    plt.plot(range(T),U[:,i])
plt.legend(['(u_t)_1','(u_t)_2','(u_t)_3'],loc='lower right')
plt.xlabel("t\n Linear Quadratic Control")
plt.show()

### Task 3 - Linear State Feedback Control ###
    #calculate the dynamical system with linear state feedback control
K = #the state feedback gain matrix   
print(K)

Xst = #Xst[t] is the state vector at time t with state feedback control
Ust = #Ust[t] is the control vector at time t with state feedback control

# Graphing #
for i in range(len(a)):
    plt.plot(range(T+1),Xst[:,i])
plt.legend(['(x_t)_1','(x_t)_2','(x_t)_3','(x_t)_4'],loc='lower right')
plt.xlabel("t\n State Feedback Control")
plt.show()
for i in range(len(B[0])):
    plt.plot(range(T),Ust[:,i])
plt.legend(['(u_t)_1','(u_t)_2','(u_t)_3'],loc='lower right')
plt.xlabel("t\n State Feedback Control")
plt.show()
