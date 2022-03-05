import numpy as np

np.random.seed(42)
arr = np.random.randint(0, 100, size=(3, 3, 3))
print(arr)

# arr에 52 또는 1이 있는지 확인해봅시다.
result1 = (arr.any() == 52) | (arr.any() == 1)

print(result1)

# arr[0, :, :]에 요소들이 모두 20 이상의 수를 가지고 있는지 확인해봅시다.
result2 = (arr.all() >=20)

print(result2)
