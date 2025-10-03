"""
SVM with Gaussian kernel (using scikit-learn)
"""
from sklearn import svm
import numpy as np

X = np.array([[0, 0], [1, 1], [0, 1], [1, 0]])
y = [0, 0, 1, 1]
clf = svm.SVC(kernel='rbf', gamma=1.0)
clf.fit(X, y)
print("Support vectors:\n", clf.support_vectors_)
print("Predictions:", clf.predict([[0.5, 0.5], [1, 1]]))
