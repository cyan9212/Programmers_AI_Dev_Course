def solution(L, x):
    length = len(L)
    for i in range(length):
        if L[i]>x:
            L.insert(i,x)
            break
    if len(L) == length:
        L.append(x)
    return L
