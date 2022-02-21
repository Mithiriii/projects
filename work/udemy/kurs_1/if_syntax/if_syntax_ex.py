price = 123
bonus = 23
bonus_granted = True

price -= bonus if bonus_granted else price

print(price)


rating = 5
print('very good') if rating == 5 else print('good') if rating == 4 else print('week')