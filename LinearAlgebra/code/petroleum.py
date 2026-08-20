import numpy as np

#A 34-vector of the world annual petroleum consumption between 
#1980 and 2013, in thousand barrels/day.
petroleum_data = np.array([ 
    63122, 60953, 59551, 58785, 59795, 60083, 61819, 63107, 64978, 66090, 
    66541, 67186, 67396, 67619, 69006, 70258, 71880, 73597, 74274, 75975, 
    76928, 77732, 78457, 80089, 83063, 84558, 85566, 86724, 86046, 84972, 
    88157, 89105, 90340, 91195 ])

n = len(petroleum_data)
A = np.array([[1,k] for k in range(n)])

x = np.linalg.lstsq(A,petroleum_data, rcond=None)[0]

import matplotlib.pyplot as plt
plt.scatter(np.arange(1980,2014), petroleum_data)
plt.plot(np.arange(1980,2014), A @ x, 'r')
plt.show()
