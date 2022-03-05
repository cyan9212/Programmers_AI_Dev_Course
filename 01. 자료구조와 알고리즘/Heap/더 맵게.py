import heapq
def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while True:
        if len(scoville) == 1:
            if heapq.heappop(scoville) < K:
                return -1
            else:
                return answer
        min1 = heapq.heappop(scoville)
        if min1>=K:
            return answer
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + min2*2)
        answer+=1
