import numpy as np

np.random.seed(42)

# 2 x 1 x 3 모양의 배열 A
A = np.array(
    [[[4, 3, 1]],
     [[3, 2, 2]]]
)
print(A)

### np.random.randint 함수를 사용하여 아래 주어진 크기의 랜덤 배열을 생성해 봅시다. 단, 정수 범위는 0부터 5까지로 지정합니다.
# a. 1 x 3 모양의 배열
# b. 3 모양의 배열
# c. 2 x 3 모양의 배열
B = np.random.randint(0, 6, size=(2,3))

print(B)

# A와 B 사이의 덧셈 연산 결과를 result에 담아주세요.
result = A+B

print(result)
