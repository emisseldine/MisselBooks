import numpy as np

T = 200
A = np.array([[0.95,0.04,0,0],
              [0.05,0.85,0,0],
              [0,0.1,1,0],
              [0,0.01,0,1]])
x = np.zeros((T,4))
x[0] = np.array([1,0,0,0])

for t in range(T-1):
    x[t+1] = A @ x[t]

import matplotlib.pyplot as plt
# Define line styles and colors for each time series
styles = ['-', '--', ':', '-.']
colors = ['#aa1bdd', '#00aae6', '#cc0000', '#fc9403']
lnwth = [1,1.5,2,2.5]

for i in range(len(x[0])): 
    plt.plot(np.arange(T),x[:,i],styles[i],c=colors[i],linewidth=lnwth[i])
plt.xlabel('Time t')
plt.legend(['Susceptible','Infected','Recovered','Deceased'])
plt.show()
