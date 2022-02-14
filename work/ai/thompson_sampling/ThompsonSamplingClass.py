import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random


class ThompsonSampling:
    def __init__(self, path, N, d):
        self.N = N
        self.d = d
        self.machine_selected = []
        self.number_of_rewards_1 = np.zeros(d)
        self.number_of_rewards_0 = np.zeros(d)
        self.total_rewards = 0
        self.dataset = pd.read_csv(path)

    def thompson_sampling_implement(self):
        for i in range(self.N):
            selected = 0
            max_random = 0
            for j in range(self.d):
                random_beta = random.betavariate(self.number_of_rewards_1[i] + 1, self.number_of_rewards_0[i] + 1)
                if random_beta > max_random:
                    max_random = random_beta
                    selected = j
            self.machine_selected.append(selected)
            reward = self.dataset.values[i, selected]
            if reward == 1:
                self.number_of_rewards_1[selected] += 1
            else:
                self.number_of_rewards_0[selected] += 1
            self.total_rewards += reward

    def visualize(self):
        plt.hist(self.machine_selected)
        plt.title("Histogram of machines selected")
        plt.xlabel("Machines")
        plt.ylabel("Number of times each machine was selected")
        plt.plot()
