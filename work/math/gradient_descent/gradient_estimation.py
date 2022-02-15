import random
import math


def scalar_multiply(c, v):
    return [c*v_i for v_i, in v]


def sum_of_squares_gradient(v):
    return [2 * v_i for v_i in v]


def sum_of_squares(v):
    return sum(v_i ** 2 for v_i in v)


def vector_subtract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def squared_distance(v, w):
    return sum_of_squares(vector_subtract(v, w))


def distance(v, w):
    return math.sqrt(squared_distance(v, w))


def step(v, direction, step_size):
    return [v_i + step_size * direction_i for v_i, direction_i in zip(v, direction)]


v = [random.randint(-10, 10) for i in range(3)]

tolerance = 0.0000001

while True:
    gradient = sum_of_squares_gradient(v)
    next_v = step(v, gradient, -0.01)
    if distance(next_v, v) < tolerance:
        break
    v = next_v

print(v)


def safe(f):
    def safe_f(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except:
            return float('inf')
    return safe_f


#dla każdego kroku gradientu analizowany jest cały zbiór danych (w tej funckji)
def minimize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    step_sizes = [100, 10, 1, 0.1, 0.01, 0.001, 0.0001, 0.00001]
    theta = theta_0
    target_fn = safe(target_fn)
    value = target_fn(theta)

    while True:
        gradient = gradient_fn(theta)
        next_thetas = [step(theta, gradient, -step_sizes) for step_size in step_sizes]

        #wybierz wartość minimalizującą funkcję błedu
        next_theta = min(next_thetas, key=target_fn)
        next_value = target_fn(next_theta)

        #zatrzymaj w wypadku osiągnięciu punktu zbieżności
        if abs(value - next_value) < tolerance:
            return theta
        else:
            theta, value = next_value, next_value


def negate(f):
    return lambda *args, **kwargs: -f(*args, **kwargs)


def negate_all(f):
    return lambda *args, **kwargs: [-y for y in f(*args, **kwargs)]


def maximize_batch(target_fn, gradient_fn, theta_0, tolerance=0.000001):
    return minimize_batch(negate(target_fn), negate_all(gradient_fn), theta_0, tolerance)


#teraz stochastyczna metoda gradientu prostego (gradient jest obliczany dla pojedyńczego punktu a nie dla całych zbiorów danych

def in_random_order(data):
    indexes = [i for i, _ in enumerate(data)]
    random.shuffle(indexes)
    for i in indexes:
        yield data[i]


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

def maximize_stochastic(target_fn, gradient_fn, x, y, theta_0, alpha_0=0.01):
    return minimize_stochastic(negate(target_fn), negate_all(gradient_fn), x, y, theta_0, alpha_0)
