import numpy as np

x_1 = np.array([2,0,-2])           # initial vector of dynamic system
n = len(x_1)                       # this will be 3
T = 30                             # total time (displayed on the x-axis)
A = np.array([[0.87, 0.2, -0.09],  # transition matrix
              [-0.1, 0.75, 0.31], 
              [0.06,-0.21, 0.81]])
x = np.zeros((T,len(x_1)))         # initialize dynamical system, starts with all zeros 
x[0] = x_1                         # set the first vector of dynamical system 

for t in range(T-1):
    x[t+1] = A @ x[t]              # the dynamic equation x_{t+1} = Ax_t

import matplotlib.pyplot as plt    # See Appendix for explanation of plt
# Define line styles and colors for each time series
styles = ['-', '--', ':']
colors = ['#00aae6', '#cc0000', '#fc9403']
lnwth = [1,1.5,2]

for i in range(len(x[0])): 
    plt.plot(np.arange(T),x[:,i],styles[i],c=colors[i],linewidth=lnwth[i])
plt.legend(['(x_t)_1','(x_t)_2','(x_t)_3'])
plt.xlabel('t')
