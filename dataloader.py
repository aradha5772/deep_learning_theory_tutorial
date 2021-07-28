import numpy as np


def make_dataset(n=100, d=1, eps=1):
    X = np.random.randn(d, n)
    w = np.random.randn(1, d)
    y = w @ X
    y += np.random.randn(1, n) * eps

    X_test = np.linspace(X.min(), X.max(), num=1000).reshape(d, -1)
    y_test = w @ X_test

    return X, y, X_test, y_test, w
