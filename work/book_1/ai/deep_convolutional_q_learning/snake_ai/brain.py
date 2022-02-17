import keras
from keras.models import Sequential, load_model
from keras.layers import Dense, Dropout, Conv2D, MaxPooling2D, Flatten
from tensorflow.keras.optimizers import Adam


class Brain():
    def __init__(self, input_shape=(100, 100, 3), learning_rate=0.0005):
        self.learning_rate = learning_rate
        self.input_shape = input_shape
        self.num_outputs = 4
        self.model = Sequential() # pusty model
        #warstwa konwolucyjna, 32 filtry 3x3 z funkcją aktywacji relu, kształt wejściowy
        self.model.add(Conv2D(32, (3, 3), activation='relu', input_shape=self.input_shape))
        #warstwa max pollingu, okno ma rozmiar 2x2 co powoduje zmniejszenie cech map o 2
        self.model.add(MaxPooling2D((2, 2)))
        #kolejna warstwa konwolucyjna, 64 filtry 2x2
        self.model.add(Conv2D(64, (2, 2), activation='relu'))
        #spłaszczenie wektora 2d do wektora 1d
        self.model.add(Flatten())
        #tradycyjna sieć ssn, 256 neuronów
        self.model.add(Dense(units=256, activation='relu'))
        #warstwa wyjściowa (jeśli nie ustawia się aktywacji będzie ona liniowa
        self.model.add(Dense(units=self.num_outputs))
        #kompilowanie modelu
        self.model.compile(loss='mean_squared_error', optimizer=Adam(learning_rate=self.learning_rate))

    def load_model(self, filepath):
        self.model = load_model(filepath)
        return self.model

