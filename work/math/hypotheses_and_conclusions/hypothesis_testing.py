#Przykład, sprawdzenie czy moneta jest "uczciwa" p - prawdopodobieństwo wyrzucenia orła
#moneta uczciwa p = 0.5, moneta nieuczciwa p != 0.5

import math
import random


def normal_cdf(x, mi=0., sigma=1.):
    return (1 + math.erf((x-mi) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p, mi=0, sigma=1, tolerance=0.00001):
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


def normal_approximation_to_bionmial(n, p):
    mu = p*n
    sigma = math.sqrt(p * (1 - p) * n)
    return mu, sigma


normal_probability_below = normal_cdf


def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)


def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)


def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)


def normal_upper_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(probability, mu, sigma)


def normal_lower_bound(probability, mu=0, sigma=1):
    return inverse_normal_cdf(1 - probability, mu, sigma)


def normal_two_sided_bounds(probability, mu=0, sigma=1):
    tail_probability = (1 - probability) / 2
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)
    return lower_bound, upper_bound


mu_0, sigma_0 = normal_approximation_to_bionmial(1000, 0.5)

#ograniczenie 95% na podstawie założenia, że p jest równe 0,5
lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)
#rzeczywiste wartości mu i sigma przy założeniu że p = 0,55
mu_1, sigma_1 = normal_approximation_to_bionmial(1000, 0.55)
#blad typu 2
type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
power = 1 - type_2_probability

hi = normal_upper_bound(0.95, mu_0, sigma_0)
type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type_2_probability


def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        return 2 * normal_probability_below(x, mu, sigma)


print(two_sided_p_value(529.5, mu_0, sigma_0)) #529.5, korekta ciągłości

extreme_value_count = 0
for _ in range(100000):
    num_heads = sum(1 if random.random() < 0.5 else 0 for _ in range(1000))
    if num_heads >= 530  or num_heads <=470:
        extreme_value_count += 1

print(extreme_value_count / 100000)


