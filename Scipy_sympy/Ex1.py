import numpy as np
import sympy as sym

p, lyambda, mu = sym.symbols("p, l, m")
matrix = np.diag([-1 / p, -1 / p, -1 / p, 0, 0, 0], 3)
matrix[3, 0] = -(lyambda + 2 * mu)
matrix[6, 0] = -lyambda
matrix[8, 0] = -lyambda
matrix[4, 1] = -mu
matrix[5, 2] = -mu
matrix = sym.Matrix(matrix)

print('{value: кратность}', matrix.eigenvals(), sep='\n')
