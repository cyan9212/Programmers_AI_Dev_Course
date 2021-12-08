def solution(brown, red):
    dic = {}
    for i in range(1,red//2+2):
        if red%i == 0:
            dic[i] = red/i
    
    for key in dic:
        if (key+2)*(dic[key]+2) - red == brown:
            return [dic[key]+2, key+2]
