import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.linear_model import LogisticRegression


iris = datasets.load_iris()
X = iris["data"][:, 3:]                         # szerokość płatka
y = (iris["target"] == 2).astype(np.int_)       # 1 jeżeli wykryje Iris-Virginica

log_reg = LogisticRegression()
log_reg.fit(X, y)

X_new = np.linspace(0, 3, 1000).reshape(-1, 1)
y_proba = log_reg.predict_proba(X_new)
'''
plt.plot(X_new, y_proba[:, 1], "g-", label="Iris-Virginica")
plt.plot(X_new, y_proba[:, 0], "b--", label="Pozostale")
plt.show()
'''

# softmax

X = iris["data"][:, (2, 3)]             # długość płatka, szerokość płatka
y = iris["target"]

softmax_reg = LogisticRegression(multi_class="multinomial", solver="lbfgs", C=10)
softmax_reg.fit(X, y)