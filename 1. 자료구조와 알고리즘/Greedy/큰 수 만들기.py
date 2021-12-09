def solution(number, k):
    collections = []
    for num in number:
        while collections and collections[-1] < num and k>0:
            collections.pop()
            k-=1
        else:
            collections.append(num)
    if k!=0:
        collections = collections[:-k]
    return ''.join(collections)
