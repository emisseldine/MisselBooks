import numpy as np

### Task 1 ################
print("~Task 1~")
A =  #Let A denote the adjacency matrix for this graph Γ
print(f"Adjacency Matrix\n {A}\n")

### Task 2 ###############################
print("~Task 2~")
k=100
T = #The transition matrix T will be time-invariant and can be considered a modification of the adjacency matrix A for Γ
print(f"Transition Matrix\n {T}\n")
print() #What is the relationship between these two matrices?

print("Starting at vertex A")
X = np.zeros((k+1,6))
X[0] = np.array([1,0,0,0,0,0])

#Create a linear dynamical system X such that X[t] is the 6-vector of probabilities that a person following a random walk will be at vertex A after t steps.

print(f"x_3 = {X[3]}\nx_10 = {X[10]}\nx_100 = {X[100]}")
print() #What pattern do you see emerging? 

### Task 3 ###############################
print("~Task 3~")
print("Starting at vertex B")

#Create a linear dynamical system X such that X[t] is the 6-vector of probabilities that a person following a random walk will be at vertex B after t steps.

print(f"x_3 = {X[3]}\nx_10 = {X[10]}\nx_100 = {X[100]}")
print() #What pattern do you see emerging? 

#What happens if another vertex is the starting location? 
#Make a conjecture about X[t] as t -> infinity. 
#How could this information had been gleaned from the original graph in retrospect?
print()
