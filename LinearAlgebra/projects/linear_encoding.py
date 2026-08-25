import numpy as np

### TASK 1 ###
def linear_code(A):
    #Write code here
    #will output canonical parity check matrix
    #and generator matrix associated to A

### TASK 2 ###
def linear_encode(G,message):
    #write code here
    #will output the encoded message for
    #the linear code associated to generator matrix G

### VERIFICATION ############################
### TASK 1 ###
A = np.array([[0,1,1],[1,1,0],[1,0,1]])
H,G = linear_code(A)
print(H,"\n",G,"\n")

### TASK 2 ###
A = np.array([[1,1],[1,0],[1,1]])
H,G = linear_code(A)
for w in [[0,0],[0,1],[1,0],[1,1]]:
    print(linear_encode(G,w))
print("\n")
