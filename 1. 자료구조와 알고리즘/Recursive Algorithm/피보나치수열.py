def fibo(n):
    if n == 0:
        return 0
    elif n in [1,2]:
        return 1
    else:
        return fibo(n-1) + fibo(n-2)
    
def solution(x):
    return fibo(x)
