"""
Application: Fourier series as an orthonormal basis in Hilbert space
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 1000)
f = np.sin(x) + 0.5*np.sin(2*x)

# Fourier coefficients
c1 = (2/np.pi) * np.trapz(f * np.sin(x), x)
c2 = (2/np.pi) * np.trapz(f * np.sin(2*x), x)

approx = c1*np.sin(x) + c2*np.sin(2*x)
plt.plot(x, f, label='Original')
plt.plot(x, approx, label='Fourier Approximation')
plt.legend()
plt.show()
