import numpy as np


# DUŻYMI literami komentarze dla stałych elementów, normalnie dla tego specyficznego przypadku

# TWORZENIE ŚRODOWISKA
class Environment(object):
    def __init__(self, optimal_temperature=(18.0, 24.0), initial_month=0, initial_number_users=10,
                 initial_rate_data=60):
        # tutaj stałe temperatury, normalnie dane generowane
        self.monthly_atmospheric_temperatures = [1.0, 5.0, 7.0, 10.0, 11.0, 20.0, 23.0, 24.0, 22.0, 10.0, 5.0, 1.0]
        self.initial_month = initial_month
        self.atmospheric_temperatures = self.monthly_atmospheric_temperatures[initial_month]
        self.optimal_temperature = optimal_temperature
        self.min_temperature = -20
        self.max_temperature = 80
        self.min_number_users = 10
        self.max_number_users = 100
        self.max_update_users = 5
        self.min_rate_data = 20
        self.max_rate_data = 300
        self.max_update_data = 10
        self.initial_number_users = initial_number_users
        self.current_number_users = initial_number_users
        self.initial_rate_data = initial_rate_data
        self.current_rate_data = initial_rate_data
        # temperatura serwera = b0 + b1*temperatura atmosferyczna + b2*liczba użytkowników + b3*szybkość transmisji danych
        # nomralnie  wyliczylibyśmy b0, b1 itp. z otrzymanych danych, tutaj przyjąłem stałe
        # do temperatury serwera zastosowałem korelację liniową, można logarytmiczną, kwadratową itd.
        self.intrinsic_temperature = self.atmospheric_temperatures + 1.25 * self.current_number_users + 1.25 * self.current_rate_data
        self.temperature_ai = self.intrinsic_temperature
        self.temperature_noai = (self.optimal_temperature[0] + self.optimal_temperature[1]) / 2.0
        self.total_energy_ai = 0.0
        self.total_energy_noai = 0.0
        self.reward = 0.0
        self.game_over = 0  # czy temperatura przekroczyła -20 80
        self.train = 1  # tryb uczenia = 1, tryb wnioskowania = 0

    # METODA, która aktualizuje środowisko po wykonaniu akcji przez ai
    def update_env(self, direction, energy_ai,
                   month):  # direction == 1 ai nagrzewa serwer, direction == -1 ai chłodzi serwer
        # OBLICZANIE NAGRODY
        energy_noai = 0
        if (self.temperature_noai < self.optimal_temperature[0]):
            energy_noai = self.optimal_temperature[0] - self.temperature_noai
            self.temperature_noai = self.optimal_temperature[0]
        elif (self.temperature_noai > self.optimal_temperature[1]):
            energy_noai = self.temperature_noai = self.optimal_temperature[1]
            self.temperature_noai = self.optimal_temperature[1]
        self.reward = energy_noai - energy_ai  # obliczanie nagrody
        self.reward = 1e-3 * self.reward  # skalowanie nagrody
        # skalowanie do małych wartości stabilizuje trening i poprawia wydajność sztucznej inteligencji
        # POBIERANIE NASTĘPNEGO STANU
        # aktualizacja temperatury atmosferycznej
        self.atmospheric_temperatures = self.monthly_atmospheric_temperatures[month]
        # aktualizacja liczby użytkowników
        self.current_number_users += np.random.randint(-self.max_update_users, self.max_update_users)
        if (self.current_number_users > self.max_number_users):
            self.current_number_users = self.max_number_users
        elif (self.current_number_users < self.min_number_users):
            self.current_number_users = self.min_number_users
        # aktualizacja częstotliwości danych
        self.current_rate_data += np.random.randint(-self.max_update_data, self.max_update_data)
        if (self.current_rate_data > self.max_rate_data):
            self.current_rate_data = self.max_rate_data
        elif (self.current_rate_data < self.min_rate_data):
            self.current_rate_data = self.min_rate_data
        # obliczanie delty temperatury wewnętrznej
        past_intrinsic_temperature = self.intrinsic_temperature
        self.intrinsic_temperature = self.atmospheric_temperatures + 1.25 * self.current_number_users + 1.25 * self.current_rate_data
        delta_intrinsic_temperature = self.intrinsic_temperature - past_intrinsic_temperature
        # obliczanie delty temperatury w wyniku działania AI
        if (direction == -1):
            delta_temperature_ai = -energy_ai
        elif (direction == 1):
            delta_temperature_ai = energy_ai
        # aktualizacja temperatury serwera ai i noai
        self.temperature_ai += delta_intrinsic_temperature + delta_temperature_ai
        self.temperature_noai += delta_intrinsic_temperature
        # zmienna gameover
        if (self.temperature_ai < self.min_temperature):
            if (self.train == 1):
                self.game_over = 1
            else:
                self.total_energy_ai += self.optimal_temperature[0] - self.temperature_ai
                self.temperature_ai = self.optimal_temperature[0]
        elif (self.temperature_ai > self.max_temperature):
            if (self.train == 1):
                self.game_over = 1
            else:
                self.total_energy_ai += self.temperature_ai - self.optimal_temperature[1]
                self.temperature_ai = self.optimal_temperature[1]
                # system uproszczony, normalnie system chłodzenia nie jest w stanie tak szybko zredukować/zwiększyć temperatury
        # AKTUALIZACJA WYNIKÓW
        # aktualizacja całkowitej energii dla ai i noai
        self.total_energy_ai += energy_ai
        self.total_energy_noai += energy_noai
        # SKALOWANIE NASTĘPNEGO STANU (poprawa wydajności)
        # metoda standaryzacji (odjęcie minimalnej wartości zmiennej i podzieleniu tego przez różnicę max - min
        scaled_temperature_ai = (self.temperature_ai - self.min_temperature) / (
                self.max_temperature - self.min_temperature)
        scaled_number_users = (self.current_number_users - self.min_number_users) / (
                self.max_number_users - self.min_number_users)
        scaled_rate_data = (self.current_rate_data - self.min_rate_data) / (self.max_rate_data - self.min_rate_data)
        next_state = np.matrix([scaled_temperature_ai, scaled_number_users, scaled_rate_data])
        # ZWRÓCENIE NASTĘPNEGO STANU, NAGRODY I STATUSU
        return next_state, self.reward, self.game_over

    # METODA, KTÓRA RESETUJE ŚRODOWISKO
    def reset(self, new_month):
        self.atmospheric_temperatures = self.monthly_atmospheric_temperatures[new_month]
        self.initial_month = new_month
        self.current_number_users = self.initial_number_users
        self.current_rate_data = self.initial_rate_data
        self.intrinsic_temperature = self.atmospheric_temperatures + 1.25 * self.current_number_users + 1.25 * self.current_rate_data
        self.temperature_ai = self.intrinsic_temperature
        self.temperature_noai = (self.optimal_temperature[0] + self.optimal_temperature[1]) / 2.0
        self.total_energy_ai = 0
        self.total_energy_noai = 0
        self.reward = 0.0
        self.game_over = 0
        self.train = 1

    # METODA POZWALJĄCA POZNAC BIERZĄCY STAN, OSTATNIĄ NAGRODĘ I STATUS
    def observe(self):
        scaled_temperature_ai = (self.temperature_ai - self.min_temperature) / (
                self.max_temperature - self.min_temperature)
        scaled_number_users = (self.current_number_users - self.min_number_users) / (
                self.max_number_users - self.min_number_users)
        scaled_rate_data = (self.current_rate_data - self.min_rate_data) / (self.max_rate_data - self.min_rate_data)
        current_state = np.matrix([scaled_temperature_ai, scaled_number_users, scaled_rate_data])
        return current_state, self.reward, self.game_over
