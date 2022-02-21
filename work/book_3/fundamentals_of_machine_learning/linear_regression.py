import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mlt
from sklearn.linear_model import LinearRegression

X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.randn(100, 1)     # 4 + 3x1 + szum


def plot():
    plt.plot(X, y, "b.")
    plt.xlabel("$x_1$", fontsize=18)
    plt.ylabel("$y$", rotation=0, fontsize=18)
    plt.axis([0, 2, 0, 15])
    # save_fig("generated_data_plot")
    plt.show()


X_b = np.c_[np.ones((100, 1)), X]           # dodaje x0 = 1 do każdej próbki
theta_best = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)    # wynik jest bliski optymalnemu, ale zaszumiony
print(theta_best)
print("\n")

# liczymy prognozy
X_new = np.array([[0], [2]])
X_new_b = np.c_[np.ones((2, 1)), X_new]     # dodaje x0 = 1 do każdej próbki
y_predict = X_new_b.dot(theta_best)
print(y_predict)


def plot2():
    plt.plot(X_new, y_predict, "r-")
    plt.plot(X, y, "b.")
    plt.axis([0, 2, 0, 15])
    plt.show()


# odpowiednik kodu wyżej w sckit-learn
def equivalent():
    lin_reg = LinearRegression()
    lin_reg.fit(X, y)
    print(lin_reg.intercept_, lin_reg.coef_)
    print("\n")
    print(lin_reg.predict(X_new))


# implementacja wsadowego gradientu prostego
eta = 0.1       # współczynnik uczenia
n_iterations = 1000
m = 100

theta = np.random.randn(2, 1)       #losowa inicjacja

for iteration in range(n_iterations):
    gradients = 2/m * X_b.T.dot(X_b.dot(theta) - y)
    theta = theta - eta * gradients

print("\n")
print(theta)