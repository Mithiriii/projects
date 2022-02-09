# AI dla pojazdu automatycznego z pliku map.py

import os
import random
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.autograd import Variable


class Network(nn.Module): #dziedziczenie po nn.Module

    def __init__(self, input_size, nb_action): #liczba wejść, liczba możliwych działań
        super(Network, self).__init__() #aktyowanie dziedziczenia
        self.nb_action = nb_action
        self.input_size = input_size
        self.fc1 = nn.Linear(input_size, 30) #połączenie pomiędzy wastwą wejściową i warstwą ukrytą (30 ukrytych neuronów)
        self.fc2 = nn.Linear(30, nb_action) #połączenie pomiędzy warstwą ukrytą a warstwą wyjściową
        #jeżeli model tego wymaga można zrobić więcej warstw ukrytych

    def forward(self, state): #state - orientacja + 3 sygnały
        x = F.relu(self.fc1(state)) #relu - funkcja wywołania prostownika (rectified linear unit)
        q_values = self.fc2(x) #q_values przewidywane wartości q
        return q_values


class ReplayMemory(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.memory = []

    def push(self, event): #event - przejście, dodawane do pamięci
        self.memory.append(event)
        if len(self.memory) > self.capacity:
            del self.memory[0]

    def sample(self, batch_size): #propagowanie małych grup stanów wejściowych
        #po propagowaniu wstecz całych grup używając schodzenia po gradiencie małymi grupami aktualizujemy wagi
        samples = zip(*random.sample(self.memory, batch_size))
        return map(lambda x: Variable(torch.cat(x, 0)), samples) #opakowanie każdej póbki w obiekt torch Variable tak aby każdy tensor wewnątrz próbki był powiązany z gradientem
        #przy używaniu PyTorch zawsze używamy obiektów torch Variable

class Dqn(object):

    def __init__(self, input_size, nb_action, gamma): #gamma - współczynnik dyskontowy we wzorze na róznicę czasową
        self.gamma = gamma
        self.model = Network(input_size, nb_action) #model - obiekt klasy network, inaczej nasza siec neuronowa
        self.memory = ReplayMemory(capacity=100000) #si pamięta ostatnie x przejść
        self.optimizer = optim.Adam(params=self.model.parameters()) #optymalizator wag schodzenia po gradiencie minigrupami
        self.last_state = torch.Tensor(input_size).unsqueeze(0) #ostatni stan w każdym przejściu, unsqueeze - dodatkowy wymiar o indeksie 0 który będzie odpowiadał grupie
        self.last_action = 0
        self.last_reward = 0

    def select_action(self, state): #funkcja wykorzystująca softmaxa wybierająca akcje
        probs = F.softmax(self.model(Variable(state))*100) #normalnie wywoływalibyśmy to self.model.forward(Variable(state)) ale forward jest jedyną metodą klasy Network możemy zrobić to w taki sposób
        actions = probs.multinomial(len(probs)) #*100 na górze to eskploracja w stosunku do eksploatacji (czyt. im niższa tym dłużej zajmie zoptymalizowanie działania)
        return actions.data[0, 0]

    def learn(self, batch_states, batch_actions, batch_rewards, batch_next_states): #po kolei: grupa stanów wejściowych, grupa wykonanych akcji, grupa otrzymanych nagród, grupa osiągniętych następnyuch stanów
        batch_outputs = self.model(batch_states).gather(1, batch_actions.unsqueeze(1)).squeeze(1) #zbieramy grupę progrnoz Q(Stb, Atb)
        batch_next_outputs = self.model(batch_next_states).detach().max(1)[0] #obliczamy max z Q(Stb+1, A)
        batch_targets = batch_rewards + self.gamma * batch_next_outputs #otrzymujemy grupę celów
        td_loss = F.smooth_l1_loss(batch_outputs, batch_targets) #obliczamy stratę temporal difference loss
        self.optimizer.zero_grad() #inicjalizacja optymalizera
        td_loss.backward() #propagowanie wsteczne błędy straty
        self.optimizer.step() #aktualizacja wag

    def update(self, new_state, new_reward):
        new_state = torch.Tensor(new_state).float().unsqueeze(0)
        self.memory.push((self.last_state, torch.LongTensor([int(self.last_action)]), torch.Tensor([self.last_reward]), new_state))
        new_action = self.select_action(new_state)
        if len(self.memory.memory) > 100:
            batch_states, batch_actions, batch_rewards, batch_next_states = self.memory.sample(100) #próbkowanie 100 przejść z pamięci
            self.learn(batch_states, batch_actions, batch_rewards, batch_next_states)
        self.last_state = new_state
        self.last_action = new_action
        self.last_reward = new_reward
        return new_action

    def save(self):
        torch.save({'state_dict' : self.model.state_dict(),
                    'optimizer' : self.optimizer.state_dict(),
                    }, 'last_brain.pth')

    def load(self):
        if os.path.isfile('last_brain.pth'):
            print("=> loading brain...")
            checkpoint = torch.load('last_brain.pth')
            self.model.load_state_dict(checkpoint['state_dict'])
            self.optimizer.load_state_dict(checkpoint['optimizer'])
            print("done")
        else:
            print("brain no found")