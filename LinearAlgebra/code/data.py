import numpy as np

x = np.array([1,2,3,4])   # create a np.array, aka a vector
print(x)
print(x[0],x[3])          # retrieve specific entries from a vector
print(x[1:2])             # retrieve a slice of the vector
print(x[1:])              # omitting the last bound implies slice all the way to the end
subset = [0,2,3]          # create a list
print(x[subset])          # retrieve the slice associated to a subset of indices

x[0] = -5                 # individual entries of the vector can be redefined
x[1] = 6
print(x)

x[-1] = 0                 # negative indices retrieve from the end of the vector
x[-4] = 10
print(x,"\n")

x = np.array([1,2])
y = np.array([3,4,5])
 # puts together any number of np.arrays of the same shape, in the order they appear
z = np.concatenate((x,y,[6,8,9,10]))  
print(z)
 # create an all-zeros or all-ones np.array, where the input is the shape of the np.array
print(np.zeros(5),np.ones(3)) 
