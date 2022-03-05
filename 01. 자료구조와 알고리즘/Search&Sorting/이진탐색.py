def solution(L, x):
    answer = 0
    left = 0; right = len(L)-1
    mid = -1
    while left <= right:
        mid = (left+right)//2
        if L[mid] == x:
            return mid
        elif L[mid] < x:
            left = mid+1
        else:
            right = mid-1 
    return -1
