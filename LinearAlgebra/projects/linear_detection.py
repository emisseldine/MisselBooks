import numpy as np

A = np.array([[0,0,0,1,1,1],[0,1,1,0,1,1],[1,0,1,0,0,1]])

def detect_A(w):
    #write your code here

### VERIFICATION ############################
Words = np.array([[1,1,1,0,0,0],[1,1,0,1,1,0],[1,1,1,1,0,1]])
for w in Words:
    print(f"{w} has error? {detect_A(w)}.")
print("\n")
