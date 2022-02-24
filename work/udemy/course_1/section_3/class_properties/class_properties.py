brandOnSale = 'Opel'


class Car:

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK
        self.__isOnSale = isOnSale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag   - ok -    {}".format(self.isAirBagOK))
        print("Painting  - ok -    {}".format(self.isPaintingOK))
        print("Mechanic  - ok -    {}".format(self.isMechanicOK))
        print("IS ON SALE   {}".format(self.__isOnSale))
        print("------------------------")

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'if set to true, the car is available in sale/promo')


car_01 = Car('Seat', 'Ibiza', True, True, True, False)
car_02 = Car('Opel', 'Corsa', True, False, True, True)
'''
print("Status of cars:", car_01.GetIsOnSale(), car_02.GetIsOnSale())
car_01.SetIsOnSale(True)
car_02.SetIsOnSale(False)
print("Status of cars:", car_01.GetIsOnSale(), car_02.GetIsOnSale())
'''

car_01.IsOnSale = True
car_02.IsOnSale = True
print("Status of cars:", car_01.IsOnSale, car_02.IsOnSale)
