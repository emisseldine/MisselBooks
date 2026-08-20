import numpy as np
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid') #Use 'seaborn-whitegrid' if error occurs.

dilate = lambda a, b: np.array([[a, 0], [0, b]])

rotate = lambda theta: np.array([[np.cos(theta), -np.sin(theta)],
[np.sin(theta), np.cos(theta)]])

reflect = lambda theta: np.array([[np.cos(2*theta), np.sin(2*theta)],
[np.sin(2*theta), -np.cos(2*theta)]])

project = lambda theta: 1/2*np.array([[1+np.cos(2*theta), np.sin(2*theta)],
[np.sin(2*theta), 1-np.cos(2*theta)]])

#create a scatter plot for the unit square
points = np.concatenate([[[i*0.01,j*0.01] for i in range(101)] for j in range(101)])

transform = "dilate"
n=3
n_it = n            #The number of iterations you want to rotate; set to 2 for single rotate
theta= 2*np.pi/n    #Controls angle of rotation, reflection, and projection
a, b = 2, 0.5       #Controls horizontal and vertical scalars for dilation
scal = 2            #Controls the scale of the gridlines

plt.figure(figsize=(8, 8), dpi=80)
plt.ion()
plt.axis([-1*scal,scal,-1*scal,scal])

if transform == "dilate":
    T = dilate(a,b)
    #Now rotate them
    tpoints = np.array([T @ p for p in points])
    
    #Show the two sets of points
    plt.scatter([c[0] for c in points], [c[1] for c in points])
    plt.scatter([c[0] for c in tpoints],[c[1] for c in tpoints], alpha=0.1)

if transform == "rotate":
    T = [rotate(k*theta) for k in range(n_it)]
    
    #Now rotate them
    tpoints = [np.array([T[k] @ p for p in points]) for k in range(n_it)]
    
    #Show the two sets of points

    #plt.scatter([c[0] for c in points], [c[1] for c in points])
    for k in range(n_it):
        plt.scatter([c[0] for c in tpoints[k]],[c[1] for c in tpoints[k]], alpha=0.1)

if transform == "reflect":
    T = reflect(theta)
    
    #Now rotate them
    tpoints = np.array([T @ p for p in points])
    
    #Show the two sets of points
    plt.scatter([c[0] for c in points], [c[1] for c in points])
    plt.scatter([c[0] for c in tpoints],[c[1] for c in tpoints], alpha=0.1)
    
    t = np.linspace(-2, 2, 100)
    plt.plot(t,t*np.tan(theta), "-.r")
    
if transform == "project":
    T = project(theta)
    
    #Now rotate them
    tpoints = np.array([T @ p for p in points])
    
    #Show the two sets of points
    plt.scatter([c[0] for c in points], [c[1] for c in points])
    plt.scatter([c[0] for c in tpoints],[c[1] for c in tpoints], alpha=0.1)
    
    t = np.linspace(-2, 2, 100)
    plt.plot(t,t*np.tan(theta), "-.r")
    
plt.show()
