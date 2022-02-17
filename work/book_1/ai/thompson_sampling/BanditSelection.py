import numpy as np

#ustawianie współczynników konwersji i liczby próbek
conversionRates = [0.15, 0.04, 0.11, 0.19, 0.05]
N = 10000
d = len(conversionRates)

#tworzenie zbioru danych
X = np.zeros((N, d))
for i in range(N):
    for j in range(d):
        if np.random.rand() < conversionRates[j]:
            X[i][j] = 1

#tworzenie tablicz do liczenia strat i zwycięstw
nPosReward = np.zeros(d)
nNegReward = np.zeros(d)

for i in range(N):
    selected = 0
    maxRandom = 0
    for j in range(d):
        randomBeta = np.random.beta(nPosReward[j] + 1, nNegReward[j] + 1)
        if randomBeta > maxRandom:
            maxRandom = randomBeta
            selected = j
    if X[i][selected] == 1:
        nPosReward[selected] += 1
    else:
        nNegReward[selected] +=1

nSelected = nPosReward + nNegReward
for i in range(d):
    print("Maszyna numer: " + str(i+1) + " zostala wybrana "  + str(nSelected[i]) +  " razy")

print("Najlepsza maszyna to maszyna nr " + str(np.argmax(nSelected)+1))
