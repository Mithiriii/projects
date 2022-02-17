import math
from matplotlib import pyplot as plt


def normal_pdf(x, mi=0.0, sigma=1.0):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return math.exp(-(x - mi) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma)


xs = [x/10.0 for x in range(-50, 50)]
plt.plot(xs, [normal_pdf(x, sigma=1) for x in xs], '-', label='mi=0, sigma=1')
plt.plot(xs, [normal_pdf(x, sigma=2) for x in xs], '--', label='mi=0, sigma=2')
plt.plot(xs, [normal_pdf(x, sigma=0.5) for x in xs], ':', label='mi=0, sigma=0,5')
plt.plot(xs, [normal_pdf(x, mi=-1) for x in xs], '-.', label='mi=-1, sigma =1')
plt.legend()
plt.title("Wykresy roznych rozkladow normalnych")
plt.show()


def normal_cdf(x, mi=0, sigma=1.):
    return (1 + math.erf((x-mi) / math.sqrt(2) / sigma)) / 2


xs = [x / 10.0 for x in range (-50, 50)]
plt.plot(xs, [normal_cdf(x, sigma=1) for x in xs], '-', label='mi=0, sigma=1')
plt.plot(xs, [normal_cdf(x, sigma=2) for x in xs], '--', label='mi=0, sigma=2')
plt.plot(xs, [normal_cdf(x, sigma=0.5) for x in xs], ':', label='mi=0, sigma=0,5')
plt.plot(xs, [normal_cdf(x, mi=-1) for x in xs], '-.', label='mi=-1, sigma =1')
plt.legend()
plt.title("Dystrybuanty roznych rozkladow normalnych")
plt.show()


def inverse_normal_cdf(p, mi=0, sigma=1, tolerance=0.00001):
    #jeżeli rozkład nie jest standardowy to oblicz jego standardową postać i przeskaluj
    if mi != 0 or sigma != 1:
        return mi + sigma * inverse_normal_cdf(p, tolerance=tolerance)

    low_z, low_p = -10.0, 0
    hi_z, hi_p = 10.0, 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2
        mid_p = normal_cdf(mid_z)
        if mid_p < p:
            low_z,  low_p = mid_z, mid_p
        elif mid_p > p:
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z

