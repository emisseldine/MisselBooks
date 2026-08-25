import numpy as np

def linear_code(A):
    #reuse your code here from https://github.com/emisseldine/OpenLinear/blob/main/BackMatter/correct/project/Linear_Encoding

def linear_decode(H,message):
    #write code here
    #will return the decoded message if no errors
    #correct the error if possible, then decode
    #return "Error uncorrectable" if cannot be corrected

### VERIFICATION ############################
A = np.array([[1,1,1,0,0],
              [1,0,1,1,1],
              [1,1,0,1,0],
              [0,0,1,1,1],
              [0,1,0,0,1]])
H,G = linear_code(A)
words = [[1,0,0,1,0,1,1,1,0,0],
         [0,1,1,0,1,0,0,1,0,0],
         [1,1,0,0,0,0,0,0,1,1],
         [1,1,0,0,1,0,1,0,1,0],
         [1,1,1,0,1,1,1,0,0,0]]
for w in words:
    print(linear_decode(H,w))
