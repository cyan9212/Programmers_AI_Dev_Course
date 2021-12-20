import numpy as np

np.random.seed(42)

# 1 이상 3 이하 정수로 이루어진 2 x 3 모양의 배열 A를 np.random.randint()을 이용하여 만들어 주세요.
A = 
np.random.randint(1, 4, size=(2,3))

print(A)

# 1 이상 3 이하 정수로 이루어진 3 x 2 모양의 배열 B를 np.random.randint()을 이용하여 만들어 주세요.
B = 
np.random.randint(1, 4, size=(3,2))

print(B)

# A와 B의 행렬 곱 연산 결과를 변수 C에 담아주세요.
C = 
A.dot(B)

print(C)
