from environment import Environment
from brain import Brain
from dqn import Dqn
import numpy as np
import matplotlib.pyplot as plt
import os

#os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

memory_size = 60000
batch_size = 32
learning_rate = 0.0001
gamma = 0.9
n_last_states = 4
epsilon = 1.  # początkowa szans wykonania losowej akcji (100%)
epsilonDecayRate = 0.0002  # o ile zmniejszy się epsilon po każdej epoce uczenia
minEpsilon = 0.05  # minimalny epsilon
filepath_to_save = 'model.h5'

# tworzenie środowiska, mózgu i pamięci doświadczeń
env = Environment(0)
brain = Brain((env.n_rows, env.n_columns, n_last_states), learning_rate)
model = brain.model
dqn = Dqn(memory_size, gamma)


# funkcja inicjalizująca stanyg ry
def reset_states():
    # 4d dlatego, że pierwszy wymiar jest rozmiarem grupy
    current_state = np.zeros((1, env.n_rows, env.n_columns, n_last_states))
    for i in range(n_last_states):
        current_state[:, :, :, i] = env.screen_map
    return current_state, current_state


epoch = 0
scores = list()
max_n_collected = 0
n_collected = 0.
tot_n_collected = 0

#pętla nieskończona, sami możemy przerwać trening w dowolnym momencie
while True:
    env.reset()
    current_state, next_state = reset_states()
    epoch += 1
    game_over = False
    #rozpoczęcie pętli w której gramy i uczymy si
    while not game_over:
        if np.random.rand() < epsilon:
            action = np.random.randint(0, 4)
        else:
            q_values = model.predict(current_state)[0]
            action = np.argmax(q_values)
        #aktualizacja środowiska
        state, reward, game_over = env.step(action)
        #dodanie nowej klatki gry do następnego stanu i usunięcie najstarszej klatki z następnego stanu
        state = np.reshape(state, (1, env.n_rows, env.n_columns, 1))
        next_state = np.append(next_state, state, axis=3)
        next_state = np.delete(next_state, 0, axis=3)
        #zapamiętywanie przejścia i szkolenie ai
        dqn.remember([current_state, action, reward, next_state], game_over)
        inputs, targets = dqn.get_batch(model, batch_size)
        model.train_on_batch(inputs, targets)
        #sprawdzenie czy zebraliśmy jabłko i aktualizacja obecnego stanu
        if env.collected:
            n_collected += 1
        current_state = next_state
    #sprawdzenie czy rekord jabłek zjedzonych w rudnzie został pobity, jeśli tak, zapisanie modelu
    if n_collected > max_n_collected and n_collected > 2:
        max_n_collected = n_collected
        model.save(filepath_to_save)
    tot_n_collected += n_collected
    n_collected = 0
    #wyświetlanie wyników co 100 gier
    if epoch % 100 == 0 and epoch != 0:
        scores.append(tot_n_collected / 100)
        tot_n_collected = 0
        plt.plot(scores)
        plt.xlabel('Epoch / 100')
        plt.ylabel('Avarage Score')
        plt.savefig('stats.png')
        plt.close()
    #zmniejszanie wartości epsilon
    if epsilon > minEpsilon:
        epsilon -= epsilonDecayRate

    print('Epoch: ' + str(epoch) + ' Current best: ' + str(max_n_collected) + 'Epsilon: {:.5f}'.format(epsilon))

