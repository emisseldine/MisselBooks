from sympy import pprint
import sympy as sp

A = sp.Matrix([[0, 1, -3, -1, -2], [1, 1, 2, 4, 3], [3, 7, -6, 8, 1], [0, -1, 3, 4, -4]])

pprint(A.rref()[0])
