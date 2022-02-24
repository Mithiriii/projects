carBrand = 'Seat'
carModel = 'Ibiza'
carIsAirBagOk = True
carIsPaintingOk = True
carIsMechanicOk = True


def IsCarDamaged(carIsAirBagOk, carIsPaintingOk, carIsMechanicOk):
    return not (carIsAirBagOk and carIsPaintingOk and carIsMechanicOk)


print(IsCarDamaged(carIsAirBagOk, carIsPaintingOk, carIsMechanicOk))