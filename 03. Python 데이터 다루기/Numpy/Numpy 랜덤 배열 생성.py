import numpy as np

np.random.seed(42)

# np.random.randn()을 사용하여 4 x 3 x 3 모양을 가진 배열을 만들어줍니다.
A = np.random.randn(4,3,3)


# np.random.normal()을 사용하여 평균 1.56, 표준편차 0.67의 5 x 6 모양을 가진 배열을 만들어줍니다.
B = np.random.normal(loc=1.56, scale=0.67, size=(5,6))


# np.random.randint()을 사용하여 10부터 20까지 임의의 정수로 채워진 3 x 4 모양의 배열을 만들어줍니다.
C = np.random.randint(10, 21, size=(3,4))


print('-------------A의 출력-------------')
print(A)
print('-------------B의 출력-------------')
print(B)
print('-------------C의 출력-------------')
print(C)
