list = ['red', 'orange', 'green', 'violet', 'blue', 'yellow']


def new_list(list, n):
    return list[:n+1]


for i in range(len(list)):
    print(new_list(list, i))


text = 'Korporacja (z łac. corpo – ciało, ratus – szczur; pol. ciało szczura) – organizacja, która pod przykrywką prowadzenia biznesu włada dzisiejszym światem. Wydawać się może utopijnym miejscem realizacji pasji zawodowych. W rzeczywistości jednak nie jest wcale tak kolorowo. Korporacja służy do wyzyskiwania człowieka w imię postępu. Rządzi w niej prawo dżungli.'

new_text = text[text.index('(')+1:text.index(')')]
print(new_text)