def solution(L, x):
    answer = []
    length  = len(L)
    for i in range(length):
        if L[i] == x:
            answer.append(i)
    if not answer:
        return [-1]
    return answer
