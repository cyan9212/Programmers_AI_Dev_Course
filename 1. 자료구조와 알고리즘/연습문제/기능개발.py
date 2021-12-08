from collections import deque
def solution(progresses, speeds):
    answer = []
    progQ = deque(progresses)
    speedQ = deque(speeds)
    while progQ:
        cnt = 0
        day = (100 - progQ[0])//speedQ[0]
        if (100 - progQ[0])%speedQ[0] != 0:
            day+=1
        while progQ and progQ[0] + day*speedQ[0] >= 100:
            progQ.popleft()
            speedQ.popleft()
            cnt+=1
        answer.append(cnt)
    return answer
