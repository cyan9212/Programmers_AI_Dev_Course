from itertools import product
def solution(m, weights):
    put_or_not = zip([0]*len(weights), weights)
    combination = product(*put_or_not)
    return list(map(sum,combination)).count(m)
