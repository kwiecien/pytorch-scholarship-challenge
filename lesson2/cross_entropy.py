import numpy as np


# Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.
def cross_entropy1(Y, P):
    return -np.sum(np.multiply(Y, np.log(P)) + np.multiply(np.subtract(1, Y), np.log(np.subtract(1, P))))

def cross_entropy2(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))