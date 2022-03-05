import numpy as np

def solution(img):
    answer = []
    length  = len(img)
    for i in range(length):
        temp = []
        for j in range(length):
            gray = img[i,j,0]*0.3 + img[i,j,1]*0.5 + img[i,j,2]*0.2
            temp.append(np.round(gray,1))
        answer.append(temp)
    return np.array(answer)
