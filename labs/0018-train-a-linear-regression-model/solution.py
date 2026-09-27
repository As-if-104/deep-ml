import numpy as np

def train(X, y, W, b):
    
    lr = 0.01
    epochs = 1000
    n_samples = X.shape[0]

    for _ in range(epochs):
        y_pred = X @ W + b

        error = y_pred - y

        dw = (2/n_samples) * (X.T @ error)
        db = (2/n_samples) * np.sum(error)

        W -= lr * dw
        b -= lr * db
    
    return W, b
