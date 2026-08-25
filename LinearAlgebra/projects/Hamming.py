import numpy as np

### TASK 1 #########
def Hamming_dist(x,y):
    #write your code here
    
def Hamming_norm(x):
    #write your code here

### TASK 2 #########
C = np.array([[0,0,0,0,0],[1,1,1,1,0],[1,0,1,0,1],[0,1,0,1,1]])
def decode_C(w):
    #write your code here

### VERIFICATION ############################
### TASK 1 #########
#Compute Hamming Distances
Words = np.array([[1,0,1,0,1],[1,1,0,1,0],[0,0,0,1,1]])

for i in range(len(Words)):
    for j in range(i+1,len(Words)):
        print(f"Hamming distance between {Words[i]} and {Words[j]} is {Hamming_dist(Words[i], Words[j])}.")
        
#Compute Hamming Norms
for w in Words:
    print(f"Hamming norm of {w} is {Hamming_norm(w)}.")
print("\n")

### TASK 2 #########
Words = np.array([[0,1,0,1,1],[1,1,1,0,0],[1,0,0,0,1]])
for w in Words:
    print(f"{w} decodes as {decode_C(w)}.")
print("\n")
