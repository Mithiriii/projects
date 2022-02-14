#dwie ukryte warstwy z neuronami 64 i 32 jest używane w większości przypadków
#learning rate - czym wyższy współczynnik tym szybciej sieć neuronowa się uczy kosztem jakości
from keras.layers import Input, Dense, Dropout
from keras.models import Model
from tensorflow.keras.optimizers import Adam


#dropout zapobiega nadmiernemu dopasowaniu
#czyli sytuacji w której model AI działa dobrze na zbiorze uczącym ale słabo na zbiorzę testowym
#w uproszczeniu polega na dezaktywacji losowo wybranej częsci neuronów(tutaj 10%) podczas propagacji w przód i wstecz
#zapobiega nadmiernemu dopasowaniu danych szkoleniowych przez sieć neuronową

#BUDOWANIE MÓZGU
class Brain(object):
    def __init__(self, learning_rate=0.001, number_actions=5):
        self.learning_rate = learning_rate
        states = Input(shape=(3, ))
        x = Dense(units=64, activation='sigmoid')(states)
        x = Dropout(rate=0.1)(x)
        y = Dense(units=32, activation='sigmoid')(x)
        y = Dropout(rate=0.1)(y)
        q_values = Dense(units=number_actions, activation='softmax')(y)
        self.model = Model(inputs=states, outputs=q_values)
        self.model.compile(loss='mse', optimizer=Adam(learning_rate=learning_rate))
