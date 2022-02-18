import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import hashlib
from sklearn.model_selection import StratifiedShuffleSplit, cross_val_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV


#############################################################POBIERANIE DANYCH#############################################################
#ścieżka do danych
HOUSING_PATH = os.path.join("datasets", "housing")


    #ładowanie pliku csv
def load_housing_data(housing_path=HOUSING_PATH):
    csv_path = os.path.join(housing_path, "housing.csv")
    return pd.read_csv(csv_path)


housing = load_housing_data()
#housing.hist(bins=50, figsize=(20, 15))
#plt.show()


#############################################################DZIELENIE ZBIORU NA TESTOWY I TRENINGOWY#############################################################
    #dzielenie zbioru w celu stworzenia zbioru testowego
def split_train_test(data, test_ratio):
    shuffled_indices = np.random.permutation(len(data))
    test_set_size = int(len(data) * test_ratio)
    test_indices = shuffled_indices[:test_set_size]
    train_indices = shuffled_indices[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]


#train_set, test_set = split_train_test(housing, 0.2)

    #takie rozwiązanie wiąże się z problemami:
    #przy kolejnych uruchomieniach programu zostanie wygenerowany inny zbiór testowy
    #rozwiązania:
    #zapisanie zestawu i wczytywanie go przy kolejnych okazjach
    #użycie seed(x) w celu wygenerowania takiego samego seedu dla każdego uruchomienia programu

    #oba te rozwiązania zawiodą gdy dostarczymy nowe dane, należy użyć funkcji hashującej


def test_set_check(identifier, test_ratio, hash):
    return hash(np.int64(identifier)).digest()[-1] < 256 * test_ratio


def split_train_test_by_id(data, test_ratio, id_column, hash=hashlib.md5):
    ids = data[id_column]
    in_test_set = ids.apply(lambda id_: test_set_check(id_, test_ratio, hash))
    return data.loc[~in_test_set], data.loc[in_test_set]
    #do hashowania należy używać stabilnych danych
    #w tym wypadku jako, że nie mamy id dobre będą współrzędne geograficzne


housing_with_id = housing.reset_index()     #dodaje kolumne index [id]
housing_with_id["id"] = housing["longitude"] * 1000 + housing["latitude"]
#train_set, test_set = split_train_test_by_id(housing_with_id, 0.2, "id")
    #takie rozwiązanie przy dodaniu nowych danych przeniesie 20% z nich do starego zbioru treningowego a stary zbiór danych zostanie nienaruszony
    #jednak losowe próbkowanie spisuje się dobrze w wypadku dużych zbiorów danych, inaczej ryzykujemy obciążenie próbkowania
    #np. jeżeli A stanowi 73%B i 27%C to podobna ilość przykładów powinna pochodzi z B i C, w losowym często tak nie będzie
    #należy użyć losowania warstwowego


    #wyznaczamy kategorię dochodów w celu użycia losowania warstwowego
housing["income_cat"] = np.ceil(housing["median_income"] / 1.5)
housing["income_cat"].where(housing["income_cat"] < 5, 5.0, inplace=True)
    #kod generujący atrybut kategorii dochodów poprzez podzielanie wartości mediany przez 1,5
    #i zaokrąglenie wyników za pomocą funkcji ceil (aby wyodrębnić poszczególne kategorie)

#housing["income_cat"].hist()
#plt.show()

split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)

for train_index, test_index in split.split(housing, housing["income_cat"]):
    start_train_set = housing.loc[train_index]
    start_test_set = housing.loc[test_index]

    #usunięcie atrybutu income_cat dzięki czemu dane powracają do pierwotnego stanu
for set_ in (start_train_set, start_test_set):
    set_.drop("income_cat", axis=1, inplace=True)

#############################################################WIZUALIZACJA I ODKRYWANIE DANCYH W CELU ZDOBYWANIA NOWYCH INFORMACJI#############################################################
housing = start_train_set.copy()
#housing.plot(kind="scatter", x="longitude", y="latitude", alpha=0.4,
#             s=housing["population"]/100, label="Population", figsize=(10, 7),
#             c="median_house_value", cmap=plt.get_cmap("jet"), colorbar=True,
#             )
#plt.legend()
#plt.show()


#wyliczenie korelacji liniowej
#corr_matrix = housing.corr()

#print(corr_matrix["median_house_value"].sort_values(ascending=False))
    #przed przygotwaniem danych do użytku ml należy wypróbowac różne kombinacje atrybutów
    #np. pokoje na rodzine, sypialnie na rodzine, populacja na rodzinę i zobaczyć jak odnosza się one do koleracji z ceną mieszkań

housing["rooms_to_families"] = housing["total_rooms"]/housing["households"]
housing["bedrooms_to_rooms"] = housing["total_bedrooms"]/housing["total_rooms"]
housing["population_to_family"] = housing["population"]/housing["households"]

corr_matrix = housing.corr()
#print(corr_matrix["median_house_value"].sort_values(ascending=False))
    #sypialnie na pokoje okazały się bardziej skorelowane z medianą cen mieszkań niż liczba pomieszczeń czy liczba sypialni osobno
    #mieszkania o mniejszym współczynniku liczby sypialni do liczby pomieszczeń okazują się droższe
    #liczba pokojów na rodzinę również ma korelację, wraz z powierzchnią domu rośnie jego cena
    #wyłapywanie takich korelacji pozwoli zbudować lepszy model

#############################################################PRZYGOTYWYWANIE DANYCH POD ML#############################################################

    #rozdzielamy czynniki prognostyczne od etykiet
housing = start_train_set.drop("median_house_value", axis=1)        #funkcja dorp tworzy kopie danych
housing_labels = start_train_set["median_house_value"].copy()

#w atrybucie total_bedrooms brakuje kilku wartości
#są trzy możliwości rozwiązania tego problemu
#-pozbyć się dystryktów zawierających brakujące dane
#-pozbyć się atrybutu
#-uzupełnić dane określoną wartością (zero, średnia, mediana itd.)

#housing.dropna(subset=["total_bedrooms"])       #opcja 1
#housing.drop("total_bedrooms", axis=1)          #opcja 2
#median = housing["total_bedrooms"].median()     #opcja 3
#housing["total_bedrooms"].fillna(median, inplace=True)

    #z modułu scki-learn można użyć modułu simpleimputer zajmujący się brakującymi wartościami
imp_mean = SimpleImputer(missing_values=np.nan, strategy='mean')
housing_num = housing.drop("ocean_proximity", axis=1)   #ocen_proximity nie jest wartością numeryczną
imp_mean.fit(housing_num)
    #najbezpieczniej będzie użyć tego do wszystkich wartości numerycznych
X = imp_mean.transform(housing_num)
housing_tr = pd.DataFrame(X, columns=housing_num.columns)

#praca z danymi tekstowymi i atrybutami kategorialnymi
encoder = LabelEncoder()
housing_cat = housing["ocean_proximity"]
housing_cat_encoded = encoder.fit_transform(housing_cat)
#problem w tym, że ml będzie uznawało, że 0 i 1 są do siebie bardziej zbliżone niż 0 i 4
#trzeba zastosować kodowanie gorącojedynkowe
encoder = OneHotEncoder()
housing_cat_1hot = encoder.fit_transform(housing_cat_encoded.reshape(-1, 1))
#funkcja reshape umożliwa wprowadzenie jednego wymiaru o wartości -1 co oznacza, że jest on niesprecyzowany, wartość zostaje wywnioskowana z długości macierzy i pozostałych wymiarów
#print(housing_cat_1hot.toarray())
#SKALOWANIE CECH#
#nie jest wymagane skalowanie wartości docelowych
#dwa rodzaje skalowania wykorzysytwane są najczęściej min-max scaling i standaryzacja

rooms_ix, bedrooms_ix, population_ix, household_ix = 3, 4, 5, 6


class CombinedAttributesAdder(BaseEstimator, TransformerMixin):
    def __init__(self, add_bedrooms_per_room=True):
        self.add_bedrooms_per_room = add_bedrooms_per_room

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        rooms_to_families = X[:, rooms_ix] / X[:, household_ix]
        population_to_family = X[:, population_ix] / X[:, household_ix]
        if self.add_bedrooms_per_room:
            bedrooms_to_room = X[:, bedrooms_ix] / X[:, rooms_ix]
            return np.c_[X, rooms_to_families, population_to_family, bedrooms_to_room]
        else:
            return np.c_[X, rooms_to_families, population_to_family]


#potok pomagający wyznaczyć właściwą sekwencję transformacji
num_pipeline = Pipeline([
    ('imputer', SimpleImputer(missing_values=np.nan, strategy='mean')),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler()),           #standaryzacja
])
housing_num_tr = num_pipeline.fit_transform(housing_num)


#bezoiśrednie przekazywanie obiektu DataFrame do potoku
class DataFrameSelector(BaseEstimator, TransformerMixin):
    def __init__(self, attribute_names):
        self.attribute_names = attribute_names

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        return X[self.attribute_names].values


#uporządkowane
num_attribs = list(housing_num)
cat_attribs = ["ocean_proximity"]

num_pipeline = Pipeline([
    ('selector', DataFrameSelector(num_attribs)),
    ('imputer', SimpleImputer(missing_values=np.nan, strategy='mean')),
    ('attribs_adder', CombinedAttributesAdder()),
    ('std_scaler', StandardScaler()),           #standaryzacja
])

cat_pipeline = Pipeline([
    ('selector', DataFrameSelector(cat_attribs)),
    ('cat_encoder', OneHotEncoder())
])

full_pipeline = FeatureUnion(transformer_list=[
    ("num_pipeline", num_pipeline),
    ("cat_pipeline", cat_pipeline),
])

housing_prepared = full_pipeline.fit_transform(housing)

#############################################################WYBÓR I UCZENIE MODELU#############################################################

#model regresji liniowej
#lin_reg = LinearRegression()
#lin_reg.fit(housing_prepared, housing_labels)

#housing_predictions = lin_reg.predict(housing_prepared)
#lin_mse = mean_squared_error(housing_labels, housing_predictions)
#lin_rmse = np.sqrt(lin_mse)
#print(lin_rmse)
#błąd predykcji rzędu 68 628 dolarów nie jest zbytnio satysfakcjonujący
#przykład niedotrenowania modelu
#należy albok wybrać potężniejszy algorytm, albo wprowadzić lepsze cechy, albo zmniejszyć ograniczenie modelu


#model drzew decyzyjnych
#tree_reg = DecisionTreeRegressor()
#tree_reg.fit(housing_prepared, housing_labels)

#housing_predictions = tree_reg.predict(housing_prepared)
#tree_mse = mean_squared_error(housing_labels, housing_predictions)
#tree_rmse = np.sqrt(tree_mse)
#print(tree_rmse)
#brak błędu prawdopodobnie wynika w przetrenowania modelu - sytuacja odwrotna jak wyżej
#sprawdźmy błąd przez użycie sprawdzianu krzyżowego(kroswalidacji)

#scores = cross_val_score(tree_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)   #10 podzbiorów
#tree_rmse_scores = np.sqrt(-scores) #-scores dlatego, że funkcja sprawdzianu krzyżowego oczekuje funkcji użyteczności a nie funkcji koszut, jest to przeciwieństwo mse dlatego obliczamy -scores


def display_scores(scores):
    print("Score: ", scores)
    print("Mean: ", scores.mean())
    print("Standard wariation:", scores.std())


#display_scores(tree_rmse_scores)
#daje nam to wynik 71786 +- 2447 co jest gorsze niż regresja liniowa
#sprawdzian krzyżowy dla regresji liniowej

#lin_score = cross_val_score(lin_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)
#lin_rmse_scores = np.sqrt(-lin_score)
#display_scores(lin_rmse_scores)
#średnia 69277 +- 2968 odchylenie standardowe


#model losowego lasu
#forest_reg = RandomForestRegressor()
#forest_reg.fit(housing_prepared, housing_labels)

#housing_predictions = forest_reg.predict(housing_prepared)
#forest_mse = mean_squared_error(housing_labels, housing_predictions)
#forest_rmse = np.sqrt(forest_mse)
#print(forest_rmse)

#forest_score = cross_val_score(forest_reg, housing_prepared, housing_labels, scoring="neg_mean_squared_error", cv=10)
#forest_rmse_scores = np.sqrt(-forest_score)
#display_scores(forest_rmse_scores)
#18760 rmse
#50091 +- 2279
#wynik zestawu uczącego jest mniejszy niż dla zbiorów walidacyjnych, oznacza to, ze model ulega przetrenowaniu

#############################################################REGULACJA MODELU#############################################################
#po wybraniu jakiegoś modelu należy go dostroić
####metoda przeszukiwania siatki


param_grid = [
    {'n_estimators': [3, 10, 30], 'max_features': [2, 4, 6, 8]},
    {'bootstrap': [False], 'n_estimators': [3, 10], 'max_features': [2, 3, 4]},
]

forest_reg = RandomForestRegressor()

grid_search = GridSearchCV(forest_reg, param_grid, cv=5, scoring='neg_mean_squared_error', return_train_score=True)

grid_search.fit(housing_prepared, housing_labels)

#print(grid_search.best_params_)
#max_feature = 6, n_estimators 30

#cvres = grid_search.cv_results_
#for mean_score, params in zip(cvres["mean_test_score"], cvres["params"]):
#    print(np.sqrt(-mean_score), params)


#metode przeszukiwania siatki stujemy gdy chcemy sprawdzić względnie niewielką liczbę kombinacji,
#jeżeli przestrzeń poszikawnia hiperparametrów jest bardzo duża lepiej skorzystać z metody losowego przeszukiwania
#metody RandomizedSearchCV używa się bardzo podobnie jak GridSearchCV

