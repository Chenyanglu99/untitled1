import numpy as np

array = np.array([[1, 2, 3],
                  [2, 3, 4],
                  [3, 4, 5]])

print(array)
print('number of  dim:', array.ndim)
print('shape:', array.shape)
print('size:', array.size)

a = np.array([2, 23, 4], dtype=np.float)
print(a)

a = np.array([[1, 2], [2, 3], [3, 4]])
print(a)

a = np.zeros((3, 4), dtype=np.int16)
print(a)

a = np.empty((3, 4))
print(a)

a = np.arange(10, 20, 2)

print(a)

a = np.arange(12).reshape((3, 4))
print(a)

a = np.linspace(1, 10, 6).reshape((2, 3))
print(a)

a = np.array([10, 20, 30, 40])
b = np.arange(4)

print(a, b)
# c = a + b
c = b ** 2 * np.sin(a)
# print(c)
print(c)
print(c < 0)

a = np.array([[1, 2], [2, 3]])
b = np.arange(4).reshape((2, 2))
print(a)
print(b)
# 逐个相乘
c = a * b
# 矩阵的乘法
c_dot = np.dot(a, b)
print('c', c)
print('c_dot', c_dot)
c_dot_2 = a.dot(b)
print('c_dot_2', c_dot_2)

a = np.random.random((2, 4))
print(a)

print(np.sum(a, axis=0))
print(np.min(a, axis=1))
print(np.max(a, axis=1))

A = np.arange(14, 2, -1).reshape((3, 4))
print(A)

print(np.argmin(A))
print(np.argmax(A))

print(np.mean(A))
print(A.mean())

print(A)
print(np.cumsum(A))
print(np.diff(A))

print(np.nonzero(A))
print(np.sort(A))
print(A)
print(np.transpose(A))

print(A.T.dot(A))

print(np.clip(A, 5, 9))

A = np.arange(3, 15).reshape((3, 4))

print(A)

# print(A[2])
print(A[2][1])
print(A[2, 1])

print(A)

print(A[:, 1])
print('A.T', A.T)

for column in A.T:
    print(column)

print(A.flatten())
for item in A.flat:
    print(item)
