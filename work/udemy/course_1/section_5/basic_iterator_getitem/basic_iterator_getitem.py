import datetime as dt


class MillionDays:

    def __init__(self, year, month, day, maxdays):
        self.date = dt.date(year, month, day)
        self.maxdays = maxdays

    def __getitem__(self, item):
        if item <= self.maxdays:
            return self.date + dt.timedelta(days=item)
        else:
            raise StopIteration()


md = MillionDays(2000, 1, 1, 2500000)

# print(md[0], md[1], md[2], md[10])

it = iter(md)


print(next(it))
print(next(it))
print(next(it))

for d in md:
    pass