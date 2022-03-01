import datetime as dt
import sys

start = dt.datetime.now()
print('Execution started at: {}'.format(start))


# dates = [dt.date(2000, 1, 1) + dt.timedelta(days=i) for i in range(2500000)]
# print('size of dates is {}'.format(sys.getsizeof(dates)))
# for d in dates:
#     pass

class MillionDays:

    def __init__(self, year, month, day, maxdays):
        self.date = dt.date(year, month, day)
        self.maxdays = maxdays

    def __next__(self):
        if self.maxdays <= 0:
            raise StopIteration()
        ret = self.date
        self.date += dt.timedelta(days=1)
        self.maxdays -= 1
        return ret

    def __iter__(self):
        return self


md = MillionDays(2000, 1, 1, 2500000)
print('size of MilionDay object is: {}'.format(sys.getsizeof(md)))
for d in md:
    pass


stop = dt.datetime.now()
print('Execution started at: {}'.format(stop))
print('Total time: {}'.format(stop - start))
