import numpy as np

def solution(arr, y1, x1, y2, x2):
    arr[y1:y2+1, x1:x2+1] = arr[y1:y2+1, x1:x2+1]*2
    return arr
