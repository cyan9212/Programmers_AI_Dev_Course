import numpy as np

arr = [[i * j for j in range(10)] for i in range(10)]
arr = np.array(arr)
# arr의 (2, 3)부터 (5, 7)까지 값을 0으로 변경해주세요.
arr[2:6, 3:8] = 0

print(arr)
