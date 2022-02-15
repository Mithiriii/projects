#6/20/2014 AAPL 90.91
#6/20/2014 MSFT 41.68
#6/20/2014 FB 64.5
#6/19/2014 AAPL 91.86
#6/19/2014 MSFT 41.51
#6/19/2014 FB 64.34
#wyglad przykladowego pliku

import csv

with open('file.cvs', 'rb') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        date = row[0]
        symbol = row[1]
        closing_price = float(row[2])
        print(str(date) + str(symbol) + str(closing_price))


#plik z naglowkami
#date:symbol:closing_price
#6/20/2014:AAPL:90.91
#6/20/2014:MSFT:41.68
#6/20/2014:FB:64.5

with open('file_cos.txt', 'rb') as f:
    reader = csv.DictReader(f, delimiter=':')           #korzystamy ze słownika
    for row in reader:
        date = row['date']
        symbol = row['symbol']
        closing_price = float(row['closing_price'])

#zapisywanie danych rozdzielonych separatorem
today_prices = {'AAPL': 90.91, 'MSFT': 41.68, 'FB': 64.5}

with open('cos.txt', 'wb') as f:
    writer = csv.writer(f, delimiter=',')
    for stock, price in today_prices.items():
        writer.writerow([stock, price])
