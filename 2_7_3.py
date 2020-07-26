import numpy as np
import matplotlib.pyplot as plt
import seaborn
seaborn.set() # 设置绘图风格

mean = [0, 0]
cov = [[1, 2],
       [2, 5]]

X = np.random.multivariate_normal(mean, cov, 100)
# print(X)
plt.scatter(X[:, 0], X[:, 1],alpha=0.3)
# plt.show()

# print(X.shape[0])

indices = np.random.choice(X.shape[0], 20, replace=False)

# print(indices)

selections = X[indices]
# print(selections)

plt.scatter(selections[:, 0], selections[:, 1], facecolor='none',
            edgecolors='b', s=200)
plt.show()

x = np.random.randn(100)
print('x\n',x)
# 手动计算直方图
bins = np.linspace(-5, 5, 20)
counts = np.zeros_like(bins)
# 为每个x找到合适的区间
i = np.searchsorted(bins,x)
# 为每个区间加上1
np.add.at(counts,i,1)
# 画出结果
plt.plot(bins,counts,linestyle='--')
plt.show()

print("NumPy routine:")
counts, edges = np.histogram(x, bins)