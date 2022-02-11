import numpy as np
from environment import Environment
from brain import Brain

n_last_states = 4
filepatch_to_open = 'model.h5'
slowdown = 75

env = Environment(slowdown)
brain = Brain((env.n_rows, env.n_columns, n_last_states))
model = brain.load_model(filepatch_to_open)

def reset_states():
    current_state = np.zeros((1, env.n_rows, env.n_columns, n_last_states))
    for i in range(n_last_states):
        current_state[:, :, :, i] = env.screen_map
    return current_state, current_state

while True:
    env.reset()
    current_state, next_state = reset_states()
    game_over = False
    while not game_over:
        q_values = model.predict(current_state)[0]
        action = np.argmax(q_values)
        state, _, game_over = env.step(action)
        state = np.reshape(state, (1, env.n_rows, env.n_columns, 1))
        next_state = np.append(next_state, state, axis=3)
        next_state = np.delete(next_state, 0, axis=3)
        current_state = next_state