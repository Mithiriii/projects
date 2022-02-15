import math

#ocena przewidywań
def predict(alpha, beta, x_i):
    return beta * x_i + alpha


#wartość błędu dla każdej pary
def error(alpha, beta, x_i, y_i):
    return y_i - predict(alpha, beta, x_i)


#suma wartości błędów podniesionych do kwadratu
def sum_of_squared_errors(alpha, beta, x, y):
    return sum(error(alpha, beta, x_i, y_i) ** 2
               for x_i, y_i in zip(x, y))


def mean(x):
    return sum(x) / len(x)


def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


def sum_of_squares(v):
    return dot(v, v)


def standard_deviation(x):
    return math.sqrt(variance(x))


def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_y > 0 and stdev_x > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0


#metoda najmniejszych kwadratów
def least_squares_fit(x, y):
    beta = correlation(x, y) * standard_deviation(y) / standard_deviation(y)
    alpha = mean(y) - beta * mean(x)
    return alpha, beta


def total_sum_of_squares(y):
    return sum(v ** 2 for v in de_mean(y))


#współczynnik determinacji
def r_squared(alpha, beta, x, y):
    return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) / total_sum_of_squares(y))