import numpy as np


# Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.
def softmax1(L):
    denominator = 0.0
    for val in L:
        denominator += np.exp(val)
    result = []
    for val in L:
        result.append(np.exp(val) / denominator)
    return result


def softmax2(L):
    expL = np.exp(L)
    sumExpL = sum(expL)
    result = []
    for i in expL:
        result.append(i * 1.0 / sumExpL)
    return result


def softmax3(L):
    expL = np.exp(L)
    return np.divide(expL, expL.sum())
