"""
Application: Light propagation as a linear operator (convolution)
"""
import numpy as np
from scipy.signal import convolve
import matplotlib.pyplot as plt

# Simulate a light pulse and a medium's impulse response
pulse = np.zeros(100)
pulse[50] = 1
medium = np.exp(-np.linspace(-2, 2, 21)**2)
output = convolve(pulse, medium, mode='same')
plt.plot(pulse, label='Input Pulse')
plt.plot(output, label='After Medium')
plt.legend()
plt.title('Light Propagation as Convolution Operator')
plt.show()
