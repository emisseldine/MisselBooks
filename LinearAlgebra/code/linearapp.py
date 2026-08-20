import numpy as np

points = np.array([[-1,3],        # points to be interpolated
                  [-0.5, 0.5625],
                  [0,1],
                  [0.5,3.5625],
                  [1,15]])
x = points[:,0]                   # just the x-coordinates
y= points[:,1]                    # just the y-coordinates

print("x = ",x)
print("y = ", y, "\n")

V = np.vander(x)          # create the Vandermonde matrix, that only depends on the x-coordinates     
print("V = ", V, "\n")

c = np.linalg.solve(V,y)  # solve the linear system associated to this polynomial-data-fit
print("c = ", c)               

f = np.poly1d(c)          # np.poly1d does all the work of solving a polynomial-data-fit
print(f)

import matplotlib.pyplot as plt # matplotlib to print out our results in a graphic form
plt.style.use("seaborn-v0_8-whitegrid")

plt.ion()
domain = np.linspace(-3, 3, 100)
plt.xlim(-3,3)
plt.ylim(-1,25)
plt.scatter(x, y)
plt.plot(domain,f(domain))
plt.show()
