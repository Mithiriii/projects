from matplotlib import pyplot as plt
from collections import Counter

movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

xs = [i for i, _ in enumerate(movies)]

#słupki o współrzędnych x[xs] i wysokości [num_oscars]
plt.bar(xs, num_oscars)
plt.ylabel("Number of awards")
plt.title("Favorite movie")
#etykieta na osi x w postaci tytułów filmów, wyśrodkowana
plt.xticks([i for i, _ in enumerate(movies)], movies)
plt.show()


grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]
decile = lambda grade: grade // 10 * 10
histogram = Counter(decile(grade) for grade in grades)

plt.bar([x for x in histogram.keys()], #wyśrodkuj słupki
        histogram.values(), #nadanie słupkom wartości
        8) #szerokość słupków
plt.axis([-5, 105, 0, 5]) #zakresy osi x od -5 do 105 i y od 0 do 5
plt.xticks([10 * i for i in range(11)]) #etykiety osi x w punktach 0,10... 100
plt.xlabel("Decyl")
plt.ylabel("Number of students")
plt.title("Examination grade distribution")
plt.show()