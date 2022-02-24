class Car:

    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

    def IsDamaged(self):
        return not (self.isAirBagOK and self.isPaintingOK and self.isMechanicOK)

    def GetInfo(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag   - ok -    {}".format(self.isAirBagOK))
        print("Painting  - ok -    {}".format(self.isPaintingOK))
        print("Mechanic  - ok -    {}".format(self.isMechanicOK))
        print("------------------------")


car_01 = Car('Seat', 'Ibiza', True, True, True)
car_02 = Car('Opel', 'Corsa', True, False, True)

print(car_01.brand, car_01.model, car_01.isAirBagOK, car_01.isPaintingOK)
print(car_01.model, car_01.brand, car_01.IsDamaged())

car_01.GetInfo()
car_02.GetInfo()