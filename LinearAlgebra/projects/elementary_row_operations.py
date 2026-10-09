import numpy as np

def row_scaling(coefficient_matrix, augmented_matrix, scalar, i):
    #write your code here
    #returns scaled_coefficient_matrix, scaled_constant_matrix 

def row_replacement(coefficient_matrix, augmented_matrix, scalar, i, j):
    #write your code here
    #returns replaced_coefficient_matrix, replaced_constant_matrix

def row_interchange(coefficient_matrix, augmented_matrix, i, j):
    #write your code here
    #returns interchanged_coefficient_matrix, interchanged_constant_matrix

###VERIFY ############################
A = np.array([[1,2,3],[5,6,7], [9,10,11]])
b = np.array([4, 8, 12])
print(np.c_[A,b], "\n")  #np.c_[A,b] concatenates the two arrays forming the augmented matrix

#scale Row 2 by 3
scaled_A, scaled_b = row_scaling(A,b,3,1) 
print(np.c_[scaled_A, scaled_b], "\n")

#replace Row 3 with Row 3 - 9*Row 1
replaced_A, replaced_b = row_replacement(A,b,-9,2,0)
print(np.c_[replaced_A, replaced_b], "\n")

#interchange Row 2 and Row 3
interchanged_A, interchanged_b = row_interchange(A,b,1,2)
print(np.c_[interchanged_A, interchanged_b], "\n")
