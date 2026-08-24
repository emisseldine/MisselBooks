import numpy as np

### Parity Check Code ###
def encode_paritycheck(message):
    #write your code here
    #returns message with appended check bit

def detect_paritycheck(codeword):
    #write your code here
    #returns True or False

decode_paritycheck = lambda codeword : #write your code here, removes check bit
        
### VERIFICATION ############################
print(encode_paritycheck([1,1,0,1]), "\n")

#The last bit is a parity-check bit.
Words = np.array([[0,0,1,1,0,1,1],
                  [1,1,1,0,1,1,0],
                  [1,0,0,1,0,1,1],
                  [1,1,0,0,1,1,1],
                  [1,1,1,1,1,1,0]])
for w in Words:
    if detect_paritycheck(w):
        print("Error: ", w)
    else:
        print(decode_paritycheck(w))
 
