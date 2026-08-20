import numpy as np

X = [10]                                # initialize X

# add 99 more random points weighted near to the last point with a mild amount of randomness.
# this is so that we can create a "simulated trend" on a graph without needing to rely on real data.
for i in range(99):
    X.append(X[i]+np.random.random()*(np.random.randint(3)-1))

# convolve the data to make it softer by probability vector [1/3, 1/3, 1/3]
# 'same' changes the mode of np.convolve(a,b), which returns output of length max(len(a),len(b)) 
# by default, the mode is 'full', which gives the full convolution of length len(a)+len(b)-1
# 'same' trims off positions from the start and end of 'full' where points do not overlap
# since the probability vector is length 3, 'same' trims off index 0 and -1
Y = np.convolve(X,[1/3, 1/3, 1/3],'same') 

# when using 'same', boundary effects are still visible. 
# We can correct these boundary effects by anchoring to X[0] and X[-1]
Y[0],Y[-1] = X[0],X[-1]

import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-whitegrid') # use 'seaborn-whitegrid' if error with plt

fig, axs = plt.subplots(2, 1, figsize=(8, 6))# 2 rows, 1 column, makes it so we can see both graphs at once 

# First (pre-convolved) plot
axs[0].plot(range(100), X)
axs[0].set_title("Original Graph (paramter 1 'X')") 

# Second (convolved) plot
axs[1].plot(range(100),Y)                    
axs[1].set_title("Smoothed Graph")

plt.tight_layout()
plt.show()
