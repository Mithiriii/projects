from __future__ import division

import math

from matplotlib import pyplot as plt
from collections import Counter
import random as rd


def dot(v, w):
    return sum(v_i * w_i for v_i, w_i in zip(v, w))


def sum_of_squares(v):
    return dot(v, v)



num_friends = []
daily_minutes = []

for i in range(1000):
    num_friends.append(rd.randint(0, 100))
    daily_minutes.append(rd.randint(0, 100))

friend_counts = Counter(num_friends)
xs = range(101) #najwyższa wartość to 100
ys = [friend_counts[x] for x in xs] #wysokość słupków = liczba znajomych
plt.bar(xs, ys)
plt.axis([0, 101, 0, 25])
plt.title("Histogram liczby znajomych")
plt.xlabel("Liczba znajomych")
plt.ylabel("Liczba uzytkownikow")
plt.show()

num_points = len(num_friends)
largest_value = max(num_friends)
smallest_value = min(num_friends)
sorted_value = sorted(num_friends)
smallest_value = sorted_value[0]
second_smallest_value = sorted_value[1]
largest_value = sorted_value[-1]


#ŚREDNIA
def mean(x):
    return sum(x) / len(x)


print(mean(num_friends))


#MEDIANA
def median(v):
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        return  sorted_v[midpoint]
    else:
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


print(median(num_friends))


#KWANTYL
def quantile(x, p):
    p_index = int(p * len(x))
    return sorted(x)[p_index]


print('\nQuantile')
print(quantile(num_friends, 0.10))
print(quantile(num_friends, 0.25))
print(quantile(num_friends, 0.50))
print(quantile(num_friends, 0.90))


#DOMINATA
def mode(x):
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i, count in iter(counts.items()) if count == max_count]


print("\nDominanta:")
print(mode(num_friends))


#ZAKRES
def data_range(x):
    return max(x) - min(x)


print("\nData range:")
print(data_range(num_friends))


#WARIANCJA
def de_mean(x):
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def variance(x):
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)

print("\nVariance:")
print(variance(num_friends))


#ODCHYLENIE STANDARDOWE
def standard_deviation(x):
    return math.sqrt(variance(x))


print("\nStandard deviation:")
print(standard_deviation(num_friends))


#Bardziej niezawodną miarą jest obliczenie różnicy wartości pomiędzy 75 i 25 percentylem żeby wyeliminować wartości odstające
def interquartile_range(x):
    return quantile(x, 0.75) - quantile(x, 0.25)


print("\nInterquartile_range:")
print(interquartile_range(num_friends))


#KAWARIANCJA - określa jak dwie zmienne różnią się łącznie od swoich średnich
def covariance(x, y):
    n = len(x)
    return dot(de_mean(x), de_mean(y)) / (n - 1)


print("\nCovariance:")
print(covariance(num_friends, daily_minutes))


#KORELACJA
def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_y > 0 and stdev_x > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0


print("\nCorrelation:")
print(correlation(num_friends, daily_minutes))