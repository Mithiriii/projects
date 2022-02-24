import numpy as np
from sklearn.decomposition import PCA


np.random.seed(4)
m = 60
w1, w2 = 0.1, 0.3
noise = 0.1

angles = np.random.rand(m) * 3 * np.pi / 2 - 0.5
X = np.empty((m, 3))
X[:, 0] = np.cos(angles) + np.sin(angles)/2 + noise * np.random.randn(m) / 2
X[:, 1] = np.sin(angles) * 0.7 + noise * np.random.randn(m) / 2
X[:, 2] = X[:, 0] * w1 + X[:, 1] * w2 + noise * np.random.randn(m)


# algorytm pca
pca = PCA(n_components=2)       # można n_components = 0.95 - odsetek wariancji jaki chcemy zachować
X2D = pca.fit_transform(X)
print(pca.explained_variance_ratio_)