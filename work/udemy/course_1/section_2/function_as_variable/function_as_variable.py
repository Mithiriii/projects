def BuyMe(what):
    print('Give me', what)


BuyMe('a new car')
StealForMe = BuyMe
print(type(StealForMe))
StealForMe('a new car')


