import datetime
netto = 100
brutto = 120
assert netto <= brutto, "Netto cannot be greater than brutto"


orderDate = datetime.date(2022, 10, 13)
deliveryDate = datetime.date(2022, 10, 18)
assert orderDate <= deliveryDate, "Order date cannot be later than delivery date"
