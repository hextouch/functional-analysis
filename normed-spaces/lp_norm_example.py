"""
Lp norm example for p=1,2,inf
"""
import numpy as np

x = np.array([1, -2, 3])
print("L1 norm:", np.linalg.norm(x, 1))
print("L2 norm:", np.linalg.norm(x, 2))
print("Linf norm:", np.linalg.norm(x, np.inf))
