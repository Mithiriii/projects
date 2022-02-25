brandOnSale = 'Opel'


class Car(object):

    numberOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, is_air_bag_ok, is_painting_ok, is_mechanic_ok, is_on_sale):
        self.brand = brand
        self.model = model
        self.is_air_bag_ok = is_air_bag_ok
        self.is_painting_ok = is_painting_ok
        self.is_mechanic_ok = is_mechanic_ok
        self.__isOnSale = is_on_sale
        Car.numberOfCars += 1
        Car.listOfCars.append(self)

    def is_damaged(self):
        return not (self.is_air_bag_ok and self.is_painting_ok and self.is_mechanic_ok)

    def get_info(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag    - ok -      {}".format(self.is_air_bag_ok))
        print("Painting   - ok -      {}".format(self.is_painting_ok))
        print("Mechanic   - ok -      {}".format(self.is_mechanic_ok))
        print("IS ON SALE             {}".format(self.__isOnSale))
        print('------------------------------')

    def __GetIsOnSale(self):
        return self.__isOnSale

    def __SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing status IsOnSale to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print('Cannot change status IsOnSale. Sale valid only for {}'.format(brandOnSale))

    IsOnSale = property(__GetIsOnSale, __SetIsOnSale, None, 'if set to true, the car is available in sale/promo')


class Truck(Car):

    def __init__(self, brand, model, is_air_bag_ok, is_painting_ok, is_mechanic_ok, is_on_sale, capacity_kg):
        super().__init__(brand, model, is_air_bag_ok, is_painting_ok, is_mechanic_ok, is_on_sale)
        self.capacity_kg = capacity_kg

    def get_info(self):
        super().get_info()
        print('CapacityKG      -      {}'.format(self.capacity_kg))


truck_o1 = Truck('Ford', 'Transit', True, False, True, False, 1600)
truck_o2 = Truck('Reanult', 'Trafic', True, True, True, True, 1200)

print('Calling properties:')
print(truck_o1.brand, truck_o1.capacity_kg, truck_o1.IsOnSale, truck_o2.brand, truck_o2.capacity_kg, truck_o2.IsOnSale)

truck_o2.get_info()
truck_o1.get_info()