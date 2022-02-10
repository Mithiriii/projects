#dwie ukryte warstwy z neuronami 64 i 32 jest używane w większości przypadków
#learning rate - czym wyższy współczynnik tym szybciej sieć neuronowa się uczy kosztem jakości
from keras.layers import Input, Dense
from keras.models import Model
from tensorflow.keras.optimizers import Adam

#BUDOWANIE MÓZGU
class Brain(object):
    #BUDOWANIE W PELNI POLACZONEJ SIECI NEURONOWEJ WEWNATRZ INIT
    def __init__(self, learning_rate=0.001, number_actions=5):
        self.learning_rate = learning_rate
        #BUDOWANIE WARSTWY WEJŚCIOWEJ ZLOŻONEJ ZE STANÓW WEJŚCIOWYCH
        states = Input(shape=(3, ))
        #BUDOWANIE POLĄCZONYCH WARSTW UKRYTYCH
        #tutaj wybrałem sigmoid, relu też by działało
        x = Dense(units=64, activation='sigmoid')(states)
        y = Dense(units=32, activation='sigmoid')(x)
        #BUDOWANIE WARSTWY WYJŚCIOWEJ W PELNI POLACZONEJ Z OSTATNIĄ UKRYTĄ WARSTWĄ
        q_values = Dense(units=number_actions, activation='softmax')(y)
        #MONTAŻ PELNEJ ARCHITEKTURY WEWNĄTRZ OBIEKTU MODEL
        self.model = Model(inputs=states, outputs=q_values)
        #KOMPILACJA MODELU Z WYBRANYM BLEDEM STRATY I OPTYMALIZATOREM
        #tutaj średniokwadratowy błąd straty i optymalizator adam
        self.model.compile(loss='mse', optimizer=Adam(learning_rate=learning_rate))
