import numpy as np

x_0 = np.array([800000,500000]) # Initial state vector [Population_A,Population_B]
A = np.array([[0.8,0.1],        # Define the state transition matrix A
              [0.2,0.9]])

# Simulate the population dynamics for T years
T = 10                       #number of years
x = np.zeros((T+1,len(x_0))) #initialize linear dynamical system
x[0] = x_0
print(f"Year 0: Population A = {x[0,0]:.0f}, Population B = {x[0,1]:.0f}")
for t in range(T):
    x[t+1] = A @ x[t]       #the dynamic equation
    print(f"Year {t + 1}: Population A = {x[t+1,0]:.0f}, Population B = {x[t+1,1]:.0f}")
