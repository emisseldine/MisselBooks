loimport numpy as np

def row_scaling(coefficient_matrix, augmented_matrix, scalar, i):
    #your code from Project: Elementary Row Operations

def row_replacement(coefficient_matrix, augmented_matrix, scalar, i, j):
    #your code from Project: Elementary Row Operations

def row_interchange(coefficient_matrix, augmented_matrix, i, j):
    #your code from Project: Elementary Row Operations

def zero_below(coefficient_matrix, constant_matrix, pivot):
    #your code from Project: Row Reduction

def zero_above(coefficient_matrix, constant_matrix, pivot):
    #your code from Project: Row Reduction

def forward_phase(coefficient_matrix, constant_matrix):
    #your code from Project: Echelon Form

def backward_phase(coefficient_matrix, constant_matrix, pivots):
    #your code from Project: RREF

def Null(matrix):
    #write your code here
    #returns null, that is, returns a basis for the null space of matrix
   
### VERIFY ############################
A = np.array([[6,5,4,3,2,1],
              [5,4,3,2,1,6],
              [2,4,6,8,2,4],
              [0,1,0,1,2,6]])
print(np.round(Null(A),12))
print(Null(np.zeros((4,5))),"\n")
