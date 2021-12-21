import numpy as np

np.random.seed(42)

A = np.random.randint(0, 100, size=(3, 3, 3))

# A안에 52 또는 1인 요소와 같은 위치에는 True, 다른 곳에는 False인 배열을 result에 넣어주세요.
result = ((A.reshape(-1) == 52) | (A.reshape(-1) == 1)).reshape(3,3,3)

print(result)
