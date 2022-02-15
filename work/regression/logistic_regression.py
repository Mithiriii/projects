import math
from functools import reduce


def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def logistic(x):
    return 1.0 / (1 + math.exp(-x))


def logistic_prime(x):
    return logistic(x) * (1 - logistic(x))


def logistic_log_likelihood_i(x_i, y_i, beta):
    if y_i == 1:
        return math.log(logistic(dot(x_i, beta)))
    else:
        return math.log(1 - logistic(dot(x_i, beta)))


def logistic_log_likelihood(x, y, beta):
    return sum(logistic_log_likelihood_i(x_i, y_i, beta)
               for x_i, y_i in zip(x, y))


#wykonując obliczenia możemy policzyć gradient
def logistic_log_partial_ij(x_i, y_i, beta, j):
    return (y_i - logistic(dot(x_i, beta))) * x_i[j]


def logistic_log_gradient_i(x_i, y_i, beta):
    return [logistic_log_partial_ij(x_i, y_i, beta, j) for j, _ in enumerate(beta)]


def logistic_log_partial_ij(x, y, beta):
    return reduce(vector_add, [logistic_log_gradient_i(x_i, y_i, beta)
                               for x_i, y_i in zip(x, y)])