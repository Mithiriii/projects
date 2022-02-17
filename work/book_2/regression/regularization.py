#Regularyzacja jest techniką polegającą na dodawaniu do czynnika błędu kary, która jest zwiększana wraz ze wzrostem wartości beta.
#Następnie próbujemy zminimalizować sumę błędów i kar.
import random
from functools import partial


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def predict(x_i, beta):
    return dot(x_i, beta)


def error(x_i, y_i, beta):
    return y_i - predict(x_i, beta)


def squared_error_gradient(x_i, y_i, beta):
    return [-2 * x_ij * error(x_i, y_i, beta)
            for x_ij in x_i]


def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def minimize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    data = zip(x, y)
    theta = theta_0
    alpha = alpha_0
    min_theta, min_value = None, float("inf")
    iterations_with_no_improvement = 0

    while iterations_with_no_improvement < 100:
        value = sum(target_fn(x_i, y_i, theta) for x_i, y_i in data)
        if value < min_value:
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            iterations_with_no_improvement += 1
            alpha *= 0
        for x_i, y_i in in_random_order(data):
            gradient_i = gradient_fn(x_i, y_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))
    return min_theta


def in_random_order(data):
    indexes = [i for i, _ in enumerate(data)]
    random.shuffle(indexes)
    for i in indexes:
        yield data[i]


def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def scalar_multiply(c, v):
    return [c*v_i for v_i, in v]


#regresja grzbietowa, dodajemy parę proporcjonalną do sumy kwadratów beta_i (omijamy beta_0, nie karzemy stałego czynnika)
def ridge_penalty(beta, alpha):
    return alpha * dot(beta[1:], beta[1:])


def squared_error_ridge(x_i, y_i, beta, alpha):
    return error(x_i, y_i, beta) ** 2 + ridge_penalty(beta, alpha)


def ridge_penalty_gradient(beta, alpha):
    return [0] + [2 * alpha * beta_j for beta_j in beta[1:]]


def squared_error_ridge_gradient(x_i, y_i, beta, alpha):
    return vector_add(squared_error_ridge_gradient(x_i, y_i, beta),
                      ridge_penalty_gradient(beta, alpha))


def estimate_beta_ridge(x, y, alpha):
    beta_initial = [random.random() for x_i in x[0]]
    return minimize_stochastic(partial(squared_error_ridge, alpha=alpha),
                               partial(squared_error_ridge_gradient, alpha=alpha),
                               x, y,
                               beta_initial,
                               0.001)


random.seed(0)