import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')

plt.axis([-10,10,-3,3])
x = np.linspace(-10, 10, 1000)

f = np.piecewise(x, [((-4*np.pi <= x) & (x < -3*np.pi)),  
                     ((-3*np.pi <= x) & (x < -2*np.pi)),
                     ((-2*np.pi <= x) & (x < -1*np.pi)), 
                     ((-1*np.pi <= x) & (x < 0)), 
                     ((0 <= x) & (x < np.pi)),
                     ((np.pi <= x) & (x < 2*np.pi)),
                     ((2*np.pi <= x) & (x < 3*np.pi))], 
                 [1,0,1,0,1,0,1])
plt.plot(x,f)

#create and solve your linear system here. You will need a coefficient matrix A and an augmented column b
#Recall that np.sin(x) gives the sine function in Python, where the angle is measured in radians.

c = np.linalg.solve(A,b)
plt.plot(x,1/2+sum([c[j]*np.sin((2*j+1)*x) for j in range(25)]))

plt.show()
