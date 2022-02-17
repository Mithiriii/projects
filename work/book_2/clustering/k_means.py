#metoda grupowania k średnich
import random


def squared_distance(v, w):
    return sum_of_squares(vector_substract(v, w))


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    return dot(v, v)


def vector_substract(v, w):
    return [v_i - w_i for v_i, w_i in zip(v, w)]


def scalar_multiply(c, v):
    return [c*v_i for v_i, in v]


def vector_sum(vectors):
    result = vectors[0]
    for vector in vectors[1:]:
        result = vector_add(result, vector)
    return result


def vector_add(v, w):
    return [v_i + w_i for v_i, w_i in zip(v, w)]


def vector_mean(vectors):
    n = len(vectors)
    return scalar_multiply(1/n, vector_sum(vectors))


class KMeans:
    def __init__(self, k):
        self.k = k          #liczba grup
        self.means = None   #średnia klastrów

    def classify(self, input):
        return min(range(self.k),
                   key=lambda i: squared_distance(input, self.means[i]))

    def train(self, inputs):
        #wybierz k losowych punktów i przypisz je do początkowych wartości średnich
        self.means = random.sample(inputs, self.k)
        assignments = None

        while True:
            #znajdź nowe przypisania
            new_assignments = map(self.classify, inputs)

            #jeżeli przypisania do grup nie uległy zmianie, zakończ pracę
            if assignments == new_assignments:
                return

            #w przeciwnym wypadku zachowaj przypisania
            assignments = new_assignments

            #Oblicz nowe średnie na podstawie nowych przyporządkowań do grup
            for i in range(self.k):
                i_points = [p for p, a in zip(inputs, assignments) if a == i]

                #upewnij się że i_points nie jest pustym zbiorem
                if i_points:
                    self.means[i] = vector_mean(i_points)
