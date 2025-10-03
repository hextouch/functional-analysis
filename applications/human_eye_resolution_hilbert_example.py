"""
Application: Human eye resolution limit using Hilbert space (L2 norm)
"""
import numpy as np

def l2_norm(f, x):
    return np.sqrt(np.trapz(f**2, x))

x = np.linspace(0, 1, 1000)
wavelength = 550e-9
pupil_diameter = 2e-3
# Airy disk radius (Rayleigh criterion)
theta = 1.22 * wavelength / pupil_diameter
# Simulate point spread function (PSF)
psf = np.sinc((x-0.5)/theta)
print(f"L2 norm of PSF: {l2_norm(psf, x):.3e}")
