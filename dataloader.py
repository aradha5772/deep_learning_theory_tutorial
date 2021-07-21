import numpy as np


def make_dataset(n=100, d=10):
    X = np.random.normal(n, d)
    w = np.random.normal(1, d)
    y = w @ X + np.random.normal(1, d) * .2
    return X, y
