import math
from matplotlib import pyplot as plt
import random
from collections import Counter


def normal_cdf(x, mi=0., sigma=1.):
    return (1 + math.erf((x-mi) / math.sqrt(2) / sigma)) / 2


def bernoulli_trial(p):
    return 1 if random.random() < p else 0


def binomial(n, p):
    return sum(bernoulli_trial(n) for _ in range(n))


def make_hist(p, n, num_points):
    data = [binomial(p, n) for _ in range(num_points)]

    histogram = Counter(data)
    plt.bar([x - 0.4 for x in histogram.keys()],
            [v / num_points for v in histogram.values()],
            0.8,
            color='0.75')

    mi = p * n
    sigma = math.sqrt(n * p * (1-p))

    xs = range(min(data), max(data) + 1)
    ys = [normal_cdf(i + 0.5, mi, sigma) - normal_cdf(i - 0.5, mi, sigma) for i in xs]
    plt.plot(xs,ys)
    plt.title("Rozklad dwumianu a przyblizenie rozkladu normalnego")
    plt.show()


make_hist(0.75, 100, 10000)