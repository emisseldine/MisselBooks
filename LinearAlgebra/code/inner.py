import numpy as np

x = np.array([1,2,3])
y = np.array([0,-3,5])
print(x @ y, np.inner(x,y), "\n")


# Create two small boolean vectors.
bool_x = np.array([0, 1, 1, 1, 0, 1, 0, 0, 0])
bool_y = np.array([0, 1, 1, 0, 0, 0, 1, 0, 1])

# Taking the dot product allows you to see the number of enabled features common between them.
print("Common Features (small):", bool_x @ bool_y)

# Create two 1000-vectors of random boolean values.
large_bool_x = np.array([np.random.choice([0, 1]) for i in range(1000)])
large_bool_y = np.array([np.random.choice([0, 1]) for i in range(1000)])
# print("large_bool_x =", large_bool_x) #Uncomment if you want to see the vectors,
# print("large_bool_y =", large_bool_y) #but they are too big to fit here.

# A dot product is used once again, not any harder then on the much smaller vectors.
print("Common Features (large):", large_bool_x @ large_bool_y, '\n')
