import math

def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_substract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result


def scalar_multiply(c, v):
    return [c*v_i for v_i, in v]


#średnia wektorów o tych samych wymiarach
def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


#iloczyn skalarny
def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    return dot(v, v)


#moduł(długość) wektora
def magnitude(v):
    return math.sqrt(sum_of_squares(v))


def distance(v, w):
    return magnitude(vector_substract(v, w))


def squared_distance(v, w):
    return sum_of_squares(vector_substract(v, w))