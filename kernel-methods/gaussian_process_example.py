"""
Gaussian Process regression with RBF kernel (using scikit-learn)
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF

X = np.linspace(0, 5, 10)[:, None]
y = np.sin(X).ravel()
X_pred = np.linspace(0, 5, 100)[:, None]

kernel = RBF(length_scale=1.0)
gp = GaussianProcessRegressor(kernel=kernel)
gp.fit(X, y)
y_pred, sigma = gp.predict(X_pred, return_std=True)

plt.plot(X, y, 'o', label='Data')
plt.plot(X_pred, y_pred, label='GP mean')
plt.fill_between(X_pred.ravel(), y_pred - sigma, y_pred + sigma, alpha=0.2)
plt.legend()
plt.title('Gaussian Process Regression')
plt.show()
