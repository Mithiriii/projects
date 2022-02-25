class Car:

    def __init__(self, brand, model, is_air_bag_ok, is_painting_ok, is_mechanic_ok, accessories):
        self.brand = brand
        self.model = model
        self.is_air_bag_ok = is_air_bag_ok
        self.is_painting_ok = is_painting_ok
        self.is_mechanic_ok = is_mechanic_ok
        self.accessories = accessories

    def get_info(self):
        print("{} {}".format(self.brand, self.model).upper())
        print("Air Bag    - ok -      {}".format(self.is_air_bag_ok))
        print("Painting   - ok -      {}".format(self.is_painting_ok))
        print("Mechanic   - ok -      {}".format(self.is_mechanic_ok))
        print("Accessories            {}".format(self.accessories))
        print('------------------------------')

    def __iadd__(self, other):
        if type(other) is list:
            accessories = self.accessories
            accessories.extend(other)
            return Car(self.brand, self.model, self.is_air_bag_ok, self.is_painting_ok, self.is_mechanic_ok, accessories)
        elif type(other) is str:
            accessories = self.accessories
            accessories.append(other)
            return Car(self.brand, self.model, self.is_air_bag_ok, self.is_painting_ok, self.is_mechanic_ok,
                       accessories)
        else:
            raise Exception('Adding type {} to Car is not implemented'.format(type(other)))

    def __add__(self, other):
        if type(other) is Car:
            return [self, other]
        else:
            raise Exception('Adding type {} to Car is not implemented'.format(type(other)))

    def __str__(self):
        return "Brand: {}, Model: {}".format(self.brand, self.model)

car_o1 = Car('Seat', 'Ibiza', True, True, True, ['winter tires'])
car_o2 = Car('Opel', 'Corsa', True, False, True, [])
car_o1.get_info()

car_o1 += ['navigation system', 'roof rack']
car_o1 += 'loudspeeker system'

car_o1.get_info()

car_pack = car_o1 + car_o2
print('car01 + car02=', car_pack[0].brand, car_pack[1].brand)
print(car_pack)
print(car_o1)