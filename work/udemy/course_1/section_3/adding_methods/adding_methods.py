import csv
import types


def exportToFile_Static(path, header, data):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    print('>>>> This is function exportToFile - static method')


def exportToFile_Class(cls, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand', 'model', 'IsOnSale'])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])
    print('>>>> This is function exportToFile - class method')


def exportToFile_Instance(self, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['brand', 'model', 'IsOnSale'])
        writer.writerow([self.brand, self.model, self.IsOnSale])
    print('>>>> This is function exportToFile - instance method')


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

print('Static----------'*10)

Car.ExportToFile_Static = exportToFile_Static
#exportToFile_Static(r'C:\temp\export_static.csv', ['Brand', 'Model', 'IsOnSale'], [car_01.brand, car_01.model, car_01.IsOnSale])
Car.ExportToFile_Static(r'C:\temp\export_static.csv', ['Brand', 'Model', 'IsOnSale'], [car_01.brand, car_01.model, car_01.IsOnSale])

print('Class-----------'*10)
#Car.ExportToFile_Class = exportToFile_Class
Car.ExportToFile_Class = types.MethodType(exportToFile_Class, Car)
Car.ExportToFile_Class(path=r'C:\temp\export_class.csv')

print('Instance-----------'*10)
car_01.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_01)
car_01.ExportToFile_Instance(path=r'C:\temp\export_instance.csv')
