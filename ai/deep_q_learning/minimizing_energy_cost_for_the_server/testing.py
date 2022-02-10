import os
import numpy as np
import random as rn
from keras.models import load_model
import environment

number_actions = 5
direction_boundary = (number_actions - 1) / 2
temperature_steep = 1.5

env = environment.Environment(optimal_temperature=(18.0, 24.0), initial_month=0, initial_number_users=20, initial_rate_data=30)

#załadowanie wyszkolornego mózgu
model = load_model("model.h5")

#wybór trybu
train = False

#Uruchomienie rocznej symulacji w trybie wnioskowania
env.train = train
current_state, _, _ = env.observe()
for timestep in range(0, 12 * 30 * 24 * 60):
    q_values = model.predict(current_state)
    action = np.argmax(q_values[0])
    if (action - direction_boundary < 0):
        direction = -1
    else:
        direction = 1
    energy_ai = abs(action - direction_boundary) * temperature_steep
    next_state, reward, game_over = env.update_env(direction, energy_ai, int(timestep / (30 * 24 * 60)))
    current_state = next_state
    #prezentacja wyników
    print("\n")
    print("Energia zużyta dla AI: {:.0f}".format(env.total_energy_ai))
    print("Energia zużyta bez AI: {:.0f}".format(env.total_energy_noai))
    print("Zaoszczędzona energia: {:.0f}%".format((env.total_energy_noai - env.total_energy_ai) / env.total_energy_noai * 100))

