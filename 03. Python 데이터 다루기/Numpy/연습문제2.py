import numpy as np

def solution(x, w, b):
    x = np.array(x)
    w = np.array(w)
    return x.dot(w)+b
