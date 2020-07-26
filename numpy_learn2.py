import numpy as np

A = np.array([1, 1, 1])
B = np.array([2, 2, 2])
C = np.vstack((A, B))
D = np.hstack((A, B))

print('A\n', A)
print('A.shape', A.shape)

print('B\n', B)
print('B.shape', B.shape)

print('C\n', C)
print('C.shape', C.shape)

print('D\n', D)
print('D.shape\n', D.shape)

print('A.T\n', A.T)
print('A.T.shape', A.T.shape)

print(A[:, np.newaxis])
