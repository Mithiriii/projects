#ZBUDOWANIE SZTUCZNEJ SIECI NEURONOWEJ DLA PRZEWIDYWANIA CEN DOMÓW
import pandas as pd
import numpy as np
import keras
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from keras.layers import  Dense, Dropout
from keras.models import Sequential
from tensorflow.keras.optimizers import Adam

dataset = pd.read_csv('kc_house_data.csv')

#oddzielenie funckji i celów

X = dataset.iloc[:, 3:].values
X = X[:, np.r_[0:13, 14:18]]
y = dataset.iloc[:, 2].values

#dzielenie zbioru danych na zestaw testowy i uczący się
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

#skalowanie wartości
# Xscaled = (X - Xmin)/(Xmax - Xmin)

#skalowanie cech
xscaler = MinMaxScaler(feature_range=(0, 1))
X_train = xscaler.fit_transform(X_train)
X_test = xscaler.transform(X_test)

#skalowanie celu
yscaler = MinMaxScaler(feature_range=(0, 1))
y_train = yscaler.fit_transform(y_train.reshape(-1, 1))
y_test = yscaler.transform(y_test.reshape(-1, 1))

#budowanie sztucznej sieci neuronowej
model = Sequential()
model.add(Dense(units=64, kernel_initializer='uniform', activation='relu', input_dim=17))
model.add(Dense(units=16, kernel_initializer='uniform', activation='relu'))
model.add(Dense(units=1, kernel_initializer='uniform', activation='relu'))
model.compile(optimizer=Adam(learning_rate=0.001), loss='mse', metrics=['mean_absolute_error'])

#szkolenie sztucznej sieci neuronowej
model.fit(X_train, y_train, batch_size=32, epochs=100, validation_data= (X_test, y_test))

#wykonywanie prognoz na zbiorze testowym podczas obdwracania skalowania
y_test = yscaler.inverse_transform(y_test)
prediction = yscaler.inverse_transform(model.predict(X_test))

#obliczanie błędu
#error = (|prediction - actualValue|)/actualValue * 100%
error = abs(prediction - y_test)/y_test
print(np.mean(error))
