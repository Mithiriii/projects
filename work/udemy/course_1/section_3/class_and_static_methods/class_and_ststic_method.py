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

    @classmethod
    def ReadFromText(cls, aText):
        aNewCar = cls(*aText.split(':'))
        return aNewCar

    @staticmethod
    def Convert_KM_KW(KM):
        return KM * 0.735

    @staticmethod
    def Convert_KW_KM(KW):
        return KW * 1.36


lineOfText = 'Renault:Megane:True:True:False:False'
car_03 = Car.ReadFromText(lineOfText)
car_03.GetInfo()

print('converting 120 KM to KW', Car.Convert_KM_KW(120))
print('converting 90 kw to km', Car.Convert_KW_KM(90))

