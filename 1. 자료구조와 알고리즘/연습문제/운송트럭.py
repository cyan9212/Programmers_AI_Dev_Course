def solution(max_weight, specs, names):
    answer = 0
    dic = {x[0]:int(x[1]) for x in specs}
    names.reverse()
    temp = 0
    
    while names:
        cur = names.pop()
        if temp+dic[cur] > max_weight:
            answer+=1
            temp = dic[cur]
        else:
            temp+= dic[cur]
            
    return answer+1
