import sys, re
from collections import Counter

#egrep.py
if __name__ == "__main__":
    regex = sys.argv[1]
    for line in sys.stdin:
        if re.search(regex, line):
            sys.stdout.write(line)


#line_count.py
count = 0
for line in sys.stdin:
    count += 1

print(count)

#policzenie liczby wierszy w zawartym pliku tekstowym
#polecenie windows type cos.txt | python egrep.py "[0-9]" | python line_count.py


#skrypt liczący najczęściej występujące słowa
#most_common_words.py

try:
    num_words = int(sys.argv[1])
except:
    print("Uruchomiono: most_common_words.py num_words")
    sys.exit(1)

counter = Counter(word.lower() #słowa zapisane małymi literami
                  for line in sys.stdin
                  for word in line.strip().split() #dzielenie na spacjach
                  if word) #pomiń puste słowa

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")

#uruchomienie type cos.txt | python most_common_words.py 10