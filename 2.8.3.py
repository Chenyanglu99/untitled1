import numpy as np
import matplotlib.pyplot as plt
import seaborn

seaborn.set()

X = np.random.random((10, 2))

print('X[:, np.newaxis, :] \n', X[:, np.newaxis, :])
print('X[np.newaxis, :, :] \n', X[np.newaxis, :, :])

# 在坐标系中计算每对点的坐标差值，并存放在（10,10,2）的数组中
differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
sq_differences = differences ** 2
dist_sq = sq_differences.sum(-1)
print(dist_sq)

nearest = np.argsort(dist_sq, axis=1)
print(nearest)

K = 2

nearest_argpartition = np.argpartition(dist_sq, K + 1, axis=1)

# 根据k的值找出（由小到大排序）第k个值的索引，然后先向左，再向右依次比对，小的索引值放左边，大的索引值放右边，左边序列会有k个；

print('nearest_argpartition\n', nearest_argpartition)

plt.scatter(X[:, 0], X[:, 1], s=300)

for i in range(X.shape[0]):
    for j in nearest_argpartition[i, :K + 1]:
        # 画一条从X[i]到X[j]的线段
        plt.plot(*zip(X[j], X[i]), color='black')

plt.show()
print(X)
