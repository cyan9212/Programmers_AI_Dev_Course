import numpy as np

def solution(arr_list):
    A = np.array([[0]])
    for arr in arr_list:
        if A.shape[1] == arr.shape[0]:
            A = (A+1).dot(arr*2)
    return A
