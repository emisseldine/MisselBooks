import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid')#replace with 'seaborn-whitegrid' if error occurs

dilate = lambda a, b: np.array([[a, 0], [0, b]])

rotate = lambda theta: np.array([[np.cos(theta), -np.sin(theta)],[np.sin(theta), np.cos(theta)]])

reflect = lambda theta: np.array([[np.cos(2*theta), np.sin(2*theta)],[np.sin(2*theta), -np.cos(2*theta)]])

project = lambda theta: 1/2*np.array([[1+np.cos(2*theta), np.sin(2*theta)],[np.sin(2*theta), 1-np.cos(2*theta)]])

#create a scatter plot for "J"
points = np.concatenate([[[1+(0.1+0.01*i),1] for i in range(81)], 
                       [[1+0.5, 1-0.01*j] for j in range(76)],
                       [[1+0.25+0.25*np.cos(np.pi*(1+0.01*k)), 0.25+0.25*np.sin(np.pi*(1+0.01*k))] for k in range(101)]]) #np.concatenate([[[i*0.01,j*0.01] for i in range(101)] for j in range(101)])


plt.figure(figsize=(8, 8), dpi=80)
plt.ion()
plt.axis([-9,3,-7,7])

#Transform the set of points   


#Show the sets of points
plt.scatter([c[0] for c in points], [c[1] for c in points])
t = np.linspace(-10, 10, 100)
plt.plot(t,t*np.tan(5*np.pi/6), "-.r")
plt.show()
