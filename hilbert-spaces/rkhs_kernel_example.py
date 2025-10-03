"""
RKHS: Gaussian kernel and feature map
"""
import numpy as np

def gaussian_kernel(x, y, sigma=1.0):
    return np.exp(-np.linalg.norm(x-y)**2 / (2*sigma**2))

x = np.array([1.0, 2.0])
y = np.array([2.0, 3.0])
print("Gaussian kernel:", gaussian_kernel(x, y))
