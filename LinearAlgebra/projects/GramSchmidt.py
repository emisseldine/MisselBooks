import numpy as np

### TASK 1 ###
def gram_schmidt(vectors):
    #write your code here
    #it inputs a set of vectors
    #it outputs their orthonormalization, that is, 
    #all vectors are pairwise orthogonal, 
    #all vectors have unit length, 
    #and there are no zero vectors among them

### VERIFICATION ############################
A = np.array([[1,1,1,1],[0,1,1,1],[0,0,1,1]]) 
print(gram_schmidt(A))   

### TASK 2 ###
def IsIndependent_gs(vectors):
    #write you code here
    #return True if vectors is linearly independent
    #return False if vectors is linearly dependent
    #determine this using orthogonality

### VERIFICATION ############################
A = np.array([[ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
              [ 3, 2, 1, 6, 0, 0, 0, 3, 2, 1],
              [ 0, 0, 4, 2, -1, 2, 0, 0, 8, -9],
              [ 0, 0, 0, 0, 0, 1, 2, 3, 4, 5],
              [ 6, 1, -5, 6, -5, -5, 1, 8, -6, 9],
              [ 2, 3, 3, 3, 3, 2, 1, 0, 0, 0],
              [ 0, -2, -2, 4, -1, 3, 7, 14, 15, 16],
              [ 7, 7, 6, 6, 5, 5, 4, 4, 3, 3],
              [ 7, -2, -1, 2, 10, 8, -3, -2, 1, 19],
              [ 3, -2, 0, 0, 2, 2, -5, -5, 0, 0],
              [ 3, -4, -3, 2, 1, 1, 0, 3, 3, 2],
              [ 1, 1, -1, -1, 2, 0, 2, 2, 1, 1]])
print(IsIndependent_gs(A))
