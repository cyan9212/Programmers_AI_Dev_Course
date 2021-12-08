from collections import defaultdict
def solution(v):
    answer = []
    dicx = defaultdict(int)
    dicy = defaultdict(int)
    
    for num in v:
        dicx[num[0]]+=1
        dicy[num[1]]+=1
        
    for key in dicx:
        if dicx[key] == 1:
            answer.append(key)

    for key in dicy:
        if dicy[key] == 1:
            answer.append(key)
    return answer
