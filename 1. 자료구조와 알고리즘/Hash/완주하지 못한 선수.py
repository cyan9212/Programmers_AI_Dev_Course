def solution(participant, completion):
    dic = {}
    for p in participant:
        dic[p] = dic.get(p, 0) + 1
    for c in completion:
        dic[c]-=1
    for key in dic:
        if dic[key]!=0:
            return key
