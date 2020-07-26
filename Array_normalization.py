import numpy as np
import matplotlib.pyplot as plt

X = np.random.random((10, 3))
Xmean = X.mean(0)
X_centered = X - Xmean

print(Xmean, '\n', X_centered)

print(X_centered.mean(0))

x = np.linspace(0, 5, 50)
y = np.linspace(0, 5, 50)[:, np.newaxis]
z = np.sin(x) ** 10 + np.cos(10 + y * x) * np.cos(x)

plt.imshow(z, origin='lower', extent=[0, 5, 0, 5], cmap='viridis')

plt.colorbar()

plt.show()
