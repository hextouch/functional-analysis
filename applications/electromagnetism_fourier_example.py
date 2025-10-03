"""
Application: Fourier analysis in electromagnetism (solving Maxwell's equations)
"""
import numpy as np
import matplotlib.pyplot as plt

# Plane wave solution: E(x, t) = E0 * cos(kx - wt)
E0 = 1.0
k = 2 * np.pi / 1.0  # wavelength = 1
w = 2 * np.pi * 1.0   # frequency = 1
x = np.linspace(0, 2, 500)
t = 0
E = E0 * np.cos(k * x - w * t)
plt.plot(x, E)
plt.title('Plane Wave Solution (Maxwell Equations)')
plt.xlabel('x')
plt.ylabel('E(x, t=0)')
plt.show()
