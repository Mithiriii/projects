#mamy klientów, chcemy by część z nich przeszła na plan premium
#posiadamy 9 strategii trzeba wybrać która strategia jest najlepsza dla tego zadania (współczeynnik konwersji)
#próbkowanie Thompsona
#strategia losowego wyboru
#porównać obie strategie

import numpy as np
import matplotlib.pyplot as plt
import random

conversionRates = [0.05, 0.13, 0.09, 0.16, 0.11, 0.04, 0.20, 0.08, 0.01] #służy sprawdzeniu czy model dobrze działa
N = 10000 #próbka klientów
d = len(conversionRates)

#tworzymy zbior danych
X = np.zeros((N,d))
for i in range(N):
    for j in range(d):
        if np.random.rand() <= conversionRates[j]:
            X[i][j] = 1

strategies_selected_rs = [] #strategie wybrane w rundach przez algorytm losowego wyboru
strategies_selected_ts = [] #strategie wybrane w rundach przez model AI
total_rewards_rs = 0 #łączna nagroda zgromadzona w trakcie rund przez algorytm losowego wyboru
total_rewards_ts = 0 #łączna nagroda zgromadzona przez próbkowanie Thompsona
number_of_rewards_1 = np.zeros(9) # lista dziewięciu elementów która zawiera liczbę oznaczającą ile razy otrzymała nagrodę 1
number_of_rewards_0 = np.zeros(9) # nagroda 0

for n in range(N):
    strategy_rs = random.randrange(d)
    strategies_selected_rs.append(strategy_rs)
    reward_rs = X[n, strategy_rs]
    total_rewards_rs = total_rewards_rs + reward_rs
    strategy_ts = 0
    max_random = 0
    for i in range(d):
        random_beta = random.betavariate(number_of_rewards_1[i] + 1, number_of_rewards_0[i] + 1)
        if random_beta > max_random:
            max_random = random_beta
            strategy_ts = i
    reward_ts = X[n,strategy_ts]
    if reward_ts == 1:
        number_of_rewards_1[strategy_ts] += 1
    else:
        number_of_rewards_0[strategy_ts] += 1
    strategies_selected_ts.append(strategy_ts)
    total_rewards_ts = total_rewards_ts + reward_ts

relative_return = (total_rewards_ts - total_rewards_rs) / total_rewards_rs * 100 #obliczenie wydajnosci procentowej probkowania thomsona
print("Relative return: {:.0f} %".format(relative_return))

plt.hist(strategies_selected_ts)
plt.title('Histogram of Selections')
plt.xlabel('Strategy')
plt.ylabel('Number of times the strategy was selected')
plt.show()
