import numpy as np

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

def Eigenspace(matrix,eigenvalue):
    #write your code here
    #returns eigenspace, that is, 
    #returns a basis for the eigenspace of matrix with respect to eigenvalue

def Diagonalize(matrix,eigenvalues):
    #write your code here
    #returns diagonalization, that is, 
    #returns three matrices P, D, P^-1 such that matrix = PDP^-1 and D is diagonal
    #If a diagonalization is not possible, it will report the error, "No diagonalization possible."
   
### VERIFY ############################
print("Task 1")
A = np.array([[17,5,5],
              [-41,-12,-14],
              [-19,-6,-4]])
lambdas = np.round(np.linalg.eigvals(A),6)
for lamb in set(lambdas):
    print(lamb, Eigenspace(A,lamb))
print("\n")  

B = np.array([[6,10,0,-4],
              [3,5,0,-2],
              [12,24,-1,-8],
              [15,30,0,-11]])
lambdas = np.round(np.linalg.eigvals(B),6)
for lamb in set(lambdas):
    print(lamb, Eigenspace(B,lamb))
print("\n")  

print("Task 2")
C = np.array([[8,20,10],
              [5,-12,5],
              [5,10,3]])

lambdas = np.round(np.linalg.eigvals(C),6)
print(Diagonalize(C,lambdas))            
