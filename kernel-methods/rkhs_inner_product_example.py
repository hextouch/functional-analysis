"""
RKHS inner product and evaluation functional
"""
import numpy as np

def linear_kernel(x, y):
    return np.dot(x, y)

x = np.array([1.0, 2.0])
y = np.array([2.0, 3.0])
print("Linear kernel (inner product):", linear_kernel(x, y))
# In RKHS, evaluation at a point is an inner product with a kernel function
