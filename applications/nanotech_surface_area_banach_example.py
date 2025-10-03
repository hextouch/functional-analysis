"""
Application: Nanotechnology - surface area calculation using Banach space (Lp norm)
"""
import numpy as np

def lp_norm(f, x, p):
    return (np.trapz(np.abs(f)**p, x))**(1/p)

x = np.linspace(0, 1, 1000)
f = np.sin(2 * np.pi * x) + 1.5
area = lp_norm(f, x, 1)
print(f"Surface area (L1 norm) of nanostructure profile: {area:.3f}")
