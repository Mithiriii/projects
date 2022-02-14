#r oznacza tylko do odczytu
import re

file_for_reading = open('plik_odczytu.txt', 'r')

#w oznacza zapis, jeżeli istnieje zostanie nadpisany
file_for_writing = open('plik_do_zapisu.txt', 'w')

#a oznacza dopisywanie - dane zostaną dopisane na koncu pliku
file_for_appending = open('plik_do_dopisania.txt', 'a')

#trzeba zamknąć plik po zakończeniu pracy na nim
file_for_writing.close()
file_for_reading.close()
file_for_appending.close()

#można używać pliku w bloku with, wtedy po wyjściu z bloku plik sam się zamknie
with open('nazwapliku.txt', 'r') as f:
    data = 'aaaa'

#wczytany plik tekstowy można iterować po wierszach
starts_with_hash = 0
with open('plikwejsciowy.txt', 'r') as file:
    for line in file:
        if re.match("^#", line): #wyrażenie regularne sprawdzające czy dana linijka nie zaczyna się od #
            starts_with_hash += 1

#każda linia wczytana w taki sposób kończy się znakiem nowego wiersza,
#przed zaczęciem pracy na takich danych można użyć funkcji strip() żeby pozbyć się takiej linii

