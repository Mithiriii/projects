import numpy as np
import environment
import  brain_nodropout
import dqn

#USTAWIENIE PARAMETRÓW
epsilon = .3 #współczynnik eksploracji (30% losowych działań)
number_actions = 5
direction_boundary = (number_actions - 1) / 2
number_epochs = 100
max_memory = 3000
batch_size = 512
temperature_step = 1.5

#ZBUDOWANIE ŚRODOWISKA
env = environment.Environment(optimal_temperature=(18.0, 24.0), initial_month=0, initial_number_users=20, initial_rate_data=30)

#ZBUDOWANIE MÓZGU
brain = brain_nodropout.Brain(learning_rate=0.00001, number_actions=number_actions)

#ZBUDOWANIE MODEL DQN
dqn = dqn.DQN(max_memory=max_memory, discount=0.9)

#WYBÓR TRYBU PRACY
train = True

#SZKOLENIE AI
env.train = train
model = brain.model
if(env.train):
    #ROZPOCZĘCIE PĘTLI NA WSZYSTKICH EPOKACH UCZENIA (1 epoka = 5 miesiecy)
    for epoch in range(1, number_epochs): #INICJALIZACJA WSZYSTKICH ZMIENNYCH ZARÓWNO ŚRODOWISKA JAK I PĘTLI TRENINGOWEJ
        total_reward = 0
        loss = 0.
        new_month = np.random.randint(0, 12)
        env.reset(new_month=new_month)
        game_over = False
        current_state, _, _ = env.observe()
        timestep = 0
        #ROZPOCZĘCIE PĘTLI DLA KAŻDEGO KROKU (1krok = 1 minuta) W JEDNEJ EPOCE UCZENIA
        while ((not game_over) and timestep <= 5 * 30 * 24 * 60):
            #ODTWARZANIE NASTEPNEJ AKCJI PRZEZ EKSPLORACJE
            if np.random.rand() <= epsilon:
                action = np.random.randint(0, number_actions)
                if (action - direction_boundary < 0):
                    direction = -1
                else:
                    direction = 1
                energy_ai =  abs(action - direction_boundary) * temperature_step
            #ODTWARZANIE AKCJE NA PODSTAWIE WNIOSKOWANIA
            else:
                q_values = model.predict(current_state)
                action = np.argmax(q_values[0])
                if (action - direction_boundary < 0):
                    direction = -1
                else:
                    direction = 1
                energy_ai = abs(action - direction_boundary) * temperature_step
            #AKTUALIZACJA ŚRODOWISKA I PRZEJŚCIE DO NASTĘPNEGO STANU
            next_state, reward, game_over = env.update_env(direction, energy_ai, (new_month + int(timestep/(30*24*60))) % 12)
            total_reward += reward
            #ZAPISANIE NOWEGO PRZEJŚCIA W PAMIĘCI
            dqn.remember([current_state, action, reward, next_state], game_over)
            #GROMADZENIE DANYCH W DWÓCH ODDZIELNYCH GRUPACH WEJŚC I CELÓW
            inputs, targets = dqn.get_batch(model, batch_size=batch_size)
            #OBLICZANIE STRAT W DWÓCH CALYCH GRUPACH WEJSC I CELÓW
            loss += model.train_on_batch(inputs, targets)
            timestep += 1
            current_state = next_state
        #PREZENTACJA WYNIKOW SZKOLENIA DLA KAZDEJ EPOKI UCZENIA
        print("\n")
        print("Epoka uczenia: {:03d}/{:03d}".format(epoch, number_epochs))
        print("Energia zużyta dla działającego AI: {:.0f}".format(env.total_energy_ai))
        print("Energia zużyta bez AI: {:.0f}".format(env.total_energy_noai))
        #ZAPIS MODEL
        model.save("model.h5")
