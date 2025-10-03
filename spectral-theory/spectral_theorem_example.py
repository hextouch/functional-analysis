"""
Spectral theorem: diagonalization of a symmetric operator
"""
import numpy as np

A = np.array([[2, 1], [1, 2]])
evals, evecs = np.linalg.eigh(A)
print("Eigenvalues:", evals)
print("Eigenvectors:\n", evecs)
