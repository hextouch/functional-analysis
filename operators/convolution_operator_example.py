"""
Convolution operator on functions
"""
import numpy as np
from scipy.signal import convolve

f = np.array([1, 2, 3, 4])
g = np.array([0, 1, 0.5])
conv = convolve(f, g, mode='full')
print("Convolution result:", conv)
