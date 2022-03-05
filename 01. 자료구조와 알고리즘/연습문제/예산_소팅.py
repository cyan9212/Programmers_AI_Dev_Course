def solution(d, budget):
    answer = 0
    temp = 0
    d.sort()
    for x in d:
        if temp + x <= budget:
            temp+=x
            answer+=1
    return answer
