import numpy as np

def encode_triplerep(message):
    #write your code here
    #returns triple_repeated_message

def decode_triplerep(codeword):
    #write your code here
    #returns decoded_message (with errors corrected)
        
### VERIFICATION ############################
Words = np.array([[1,1,0,0],
                  [0,0,1,1],
                  [0,1,1,0]])
for w in Words:
    print(encode_triplerep(w))
print("\n")

Codewords = np.array([[0,0,1,1,0,1,0,0,1,0,0,1,0,0,1,1,0,1],
                      [0,1,0,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1],
                      [1,0,0,0,1,1,1,0,1,1,0,1,0,0,0,1,1,1],
                      [0,1,0,0,1,1,1,1,0,0,1,1,1,1,0,0,0,1],
                      [1,1,1,1,1,1,1,0,0,1,0,0,1,0,1,1,1,1]])
for c in Codewords:
    print(decode_triplerep(c))
