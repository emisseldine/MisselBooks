import numpy as np

def row_scaling(coefficient_matrix, augmented_matrix, scalar, i):
    #your code from Project: Elementary Row Operations

def row_replacement(coefficient_matrix, augmented_matrix, scalar, i, j):
    #your code from Project: Elementary Row Operations

def row_interchange(coefficient_matrix, augmented_matrix, i, j):
    #your code from Project: Elementary Row Operations

def zero_below(coefficient_matrix, constant_matrix, pivot):
    #write your code here
    #returns reduced_coefficient_matrix, reduced_constant_matrix

def zero_above(coefficient_matrix, constant_matrix, pivot):
    #write your code here
    #returns reduced_coefficient_matrix, reduced_constant_matrix

### VERIFICATION ############################
###VERIFY ############################

A = np.array([[0,2,3],[5,6,7], [9,10,11]])
b = np.array([4, 8, 12])
print(np.c_[A,b], "\n") #np.c_[A,b] concatenates the two arrays forming the augmented matrix

#row reduce below using (1,1) pivot
A, b = zero_below(A,b,(0,0))
print(np.c_[A, b], "\n")

#row reduce below using (3,3) pivot
A, b = zero_above(A, b,(2,2))
print(np.c_[A, b])
