import numpy as np

def solution(info):
    height = np.array(info[0])
    weight = np.array(info[1])
    answer = []
    for i in range(len(height)):
        flag = True
        if height[i]<150 or height[i]>195:
            flag  = False
        if weight[i]>140:
            flag = False
        if flag == False: answer.append(i)
    return answer
