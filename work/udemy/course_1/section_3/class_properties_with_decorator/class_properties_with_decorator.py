brandOnSale = 'Opel'


class Car:

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale

    def __GetIsOnSale(self):
        return self.__isOnSale

    @property
    def IsOnSale(self):
        return self.__isOnSale

    @IsOnSale.setter
    def IsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    @IsOnSale.deleter
    def IsOnSale(self):
        self.__isOnSale = None

    @property
    def CarTitle(self):
        return  "Brand: {}, Model {}".format(self.brand, self.model).title()



car_01 = Car('Seat', 'Ibiza', True, True, True, False)

print(car_01.IsOnSale)
car_01.IsOnSale = True
del car_01.IsOnSale
print(car_01.IsOnSale)
print(car_01.CarTitle)