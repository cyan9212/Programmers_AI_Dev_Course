import numpy as np

np.random.seed(42)

arr = np.random.randint(0, 100, size=(5, 6, 3))

# arr에서 10보다 크고 20보다 작거나 같은 요소들만 추출해봅시다.
result = 
arr.reshape(-1)[(arr.reshape(-1)>10) & (arr.reshape(-1)<=20)]

print(result)
