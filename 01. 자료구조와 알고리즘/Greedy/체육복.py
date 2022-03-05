def solution(n, lost, reserve):
    s = set(lost) & set(reserve)
    lost_set = set(lost) - s
    reserve_set = set(reserve) - s
    for x in sorted(reserve_set):
        if x-1 in lost_set:
            lost_set.remove(x-1)
        elif x+1 in lost_set:
            lost_set.remove(x+1)
    return n - len(lost_set)
