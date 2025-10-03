"""
Gaussian kernel and kernel matrix example
"""
import numpy as np

def gaussian_kernel(x, y, sigma=1.0):
    return np.exp(-np.linalg.norm(x-y)**2 / (2*sigma**2))

X = np.array([[1, 2], [2, 3], [3, 4]])
K = np.zeros((len(X), len(X)))
for i in range(len(X)):
    for j in range(len(X)):
        K[i, j] = gaussian_kernel(X[i], X[j], sigma=1.0)
print("Kernel matrix:\n", K)
