import numpy as np

print(list(range(5)))               # creates list [0,1,2,3,4]
print(np.arange(0, 1, 0.2))         # creates array [0. 0.2 0.4 0.6 0.8]
print(np.linspace(0, 1, 5), "\n")   # creates array [0. 0.25 0.5 0.75 1.]

for i in range(5):                  # use range to iterate for loop
    print(i)
