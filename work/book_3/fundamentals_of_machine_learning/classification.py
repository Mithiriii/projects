import numpy as np
from sklearn.datasets import fetch_openml
import matplotlib
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.model_selection import cross_val_score, cross_val_predict
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, precision_recall_curve, \
    roc_curve, roc_auc_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.multiclass import OneVsOneClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier


def sort_by_target(mnist):
    reorder_train = np.array(sorted([(target, i) for i, target in enumerate(mnist.target[:60000])]))[:, 1]
    reorder_test = np.array(sorted([(target, i) for i, target in enumerate(mnist.target[60000:])]))[:, 1]
    mnist.data[:60000] = mnist.data[reorder_train]
    mnist.target[:60000] = mnist.target[reorder_train]
    mnist.data[60000:] = mnist.data[reorder_test + 60000]
    mnist.target[60000:] = mnist.target[reorder_test + 60000]


mnist = fetch_openml('mnist_784', version=1, cache=True, as_frame=False)
mnist.target = mnist.target.astype(np.int8)
sort_by_target(mnist)

X, y = mnist["data"], mnist["target"]

some_digit = X[36000]
some_digit_image = some_digit.reshape(28, 28)

# plt.imshow(some_digit_image, cmap=matplotlib.cm.binary, interpolation="nearest")
# plt.axis("off")
# plt.show()

X_train, X_test, y_train, y_test = X[:60000], X[60000], y[:60000], y[
                                                                   60000:]  # mnist jest już podzielony na zbiór uczący i testowy

shuffle_index = np.random.permutation(60000)  # przetasowanie zbioru danych uczących
X_train, y_train = X_train[shuffle_index], y_train[shuffle_index]  # dzięki czemu dane nie będą do siebie podobne

# Uczenie klasyfikatora binarnego
# upraszczając na razie problem rozpoznajemy piątki i inne liczby

y_train_5 = (y_train == 5)
y_test_5 = (y_test == 5)


# stworzenie klasyfikatora SGD (stochastyczny spadek wzdłuż gradientu) i wyszkolenie go
# sgd_clf = SGDClassifier()
# sgd_clf.fit(X_train, y_train_5)

# miary wydajności klasyfikatorów

# sprawdzian krzyżowy
# print(cross_val_score(sgd_clf, X_train, y_train_5, cv=3, scoring="accuracy"))
# mimo dokładności 95% należy brać pod uwagę, że przy zwykłym zgadywaniu że coś nie jest 5 również uzyskalibyśmy taki wynik
# 90% liczb to nie są piątki, więc 10% zostaje do sprawdzenie, przy czym dokładność 95% można również zgadnąć
# dlatego generalnie dokładność nie stanowi dobrej miary wydajności klasyfikatorów

# macierz pomyłek (ang. confusion matrix)
# y_train_pred = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3)
# print(confusion_matrix(y_train_5, y_train_pred))
# klasa prawdziwie negatywna 52621, próbki nie będące piątkami
# klasa fałszywie pozytywna 1958, próbki niewłaściwie uznane za piątki
# klasa fałszywie negatywna 942, próbki nieprawidłowo sklasyfikowane jako niebędące piątkami (a powinny być)
# klasa prawdziwie pozytywna 4479, próbki prawidłowo rozpoznane jako piątki

# print(precision_score(y_train_5, y_train_pred)) #gdy rozpoznaje cyfę 5 nie myli się w tylu % przypadków
# print(recall_score(y_train_5, y_train_pred)) #prawidłowo rozpoznaje tyle % piątek
# print(f1_score(y_train_5, y_train_pred)) #średnia harmoniczna
# dążymy do wskaźnika który chcemy najbardziej, jeżeli potrzebujemy precyzji i możemy odrzucić część wyników może warto się na niej skupić?

# próg decyzyjny
# y_scores = sgd_clf.decision_function([some_digit])
# threshold = 200000
# y_some_digit_pred = (y_scores > threshold) #dzięki temu możemy zwiększyć precyzję (domyślny próg = 0, tutaj 200000

# y_scores = cross_val_predict(sgd_clf, X_train, y_train_5, cv=3, method="decision_function")
# precision, recalls, thresholds = precision_recall_curve(y_train_5, y_scores)


def plot_precision_recal_vs_threshold(precisions, recalls, thresholds):
    plt.plot(thresholds, precisions[:-1], "b--", label="Precyzja")
    plt.plot(thresholds, recalls[:-1], "g-", label="Pelnosc")
    plt.xlabel("Prog")
    plt.legend(loc="center left")
    plt.ylim([0, 1])


# plot_precision_recal_vs_threshold(precision, recalls, thresholds)
# plt.show()

# y_train_pred_90 = (y_scores > 70000)
# print(precision_score(y_train_5, y_train_pred_90))

# fpr, tpr, thresholds = roc_curve(y_train_5, y_scores)


def plot_roc_curve(fpr, tpr, label=None):
    plt.plot(fpr, tpr, linewidth=2, label=label)
    plt.plot([0, 1], [0, 1], 'k--')
    plt.axis([0, 1, 0, 1])
    plt.xlabel('Odsetek falszywie pozytywnych')
    plt.ylabel('Odsetek prawdziwie pozytywnych')


# plot_roc_curve(fpr, tpr)
# plt.show()

# print('\n')
# print(roc_auc_score(y_train_5, y_scores))

# forest_clf = RandomForestClassifier()
# y_probas_forest = cross_val_predict(forest_clf, X_train, y_train_5, cv=3, method="predict_proba")
# y_scores_forest = y_probas_forest[:, 1] #wynik przynależności do klasy pozytywnej
# fpr_forest, tpr_forest, thresholds_forest = roc_curve(y_train_5, y_scores_forest)

# plt.plot(fpr, tpr, "b:", label="SGD")
# plot_roc_curve(fpr_forest, tpr_forest, "Random forest")
# plt.legend(loc="lower right")
# plt.show()


# KLASYFIKACJA WIELOKLASOWA
# ovo - one versus one, ova - one versus all

# sgd_clf.fit(X_train, y_train)
# print(sgd_clf.predict([some_digit]))

# ovo_clf = OneVsOneClassifier(SGDClassifier())
# ovo_clf.fit(X_train, y_train)
# print(ovo_clf.predict([some_digit]))
# print("\n")

# forest_clf.fit(X_train, y_train)
# print(forest_clf.predict([some_digit]))

# print(forest_clf.predict_proba([some_digit]))

# print(cross_val_score(sgd_clf, X_train, y_train, cv=3, scoring="accuracy"))

# print("aaa")
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train.astype(np.float64))
# print(cross_val_score(sgd_clf, X_train, y_train, cv=3, scoring="accuracy"))


# ANALIZA BLEDOW
# y_train_pred = cross_val_predict(sgd_clf, X_train_scaled, y_train, cv=3)
# conf_mx = confusion_matrix(y_train, y_train_pred)
# print(conf_mx)
# plt.matshow(conf_mx, cmap=plt.cm.gray)
# plt.show()

# KLASYFIKACJA WIELOETYKIETOWA
def knn():
    y_train_large = (y_train >= 7)  # etykieta >=7
    y_train_old = (y_train % 2 == 1)  # etykieta nieparzystości
    y_multilabel = np.c_[y_train_large, y_train_old]

    knn_clf = KNeighborsClassifier()  # najbliżsi sąsiedzi obsługują klasyfikację wieloetykietową
    knn_clf.fit(X_train, y_multilabel)

    print(knn_clf.predict([some_digit]))

    y_train_knn_pred = cross_val_predict(knn_clf, X_train, y_multilabel, cv=3)
    print(f1_score(y_multilabel, y_train_knn_pred, average="macro"))


# KLASYFIKACJA WIELOWYJSCIOWA
noise = np.random.randint(0, 100, (len(X_train), 784))
X_train_mod = X_train + noise
noise = np.random.randint(0, 100, (len(X_test), 784))
X_test_mod = X_test + noise
y_train_mod = X_train
y_test_mod = X_test

knn_clf = KNeighborsClassifier()
knn_clf.fit(X_train_mod, y_train_mod)
# clean_digit = knn_clf.predict([X_test_mod[some_index]])
# plot_digit(clean_digit)