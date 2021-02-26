class Car: 
    #w init musi być self, ale nie trzeba go przekazywać w momencie tworzenia obiektu
    def __init__(self, brand, model, isAirBagOK, isPaintingOK, isMechanicOK):
        self.brand = brand
        self.model = model
        self.isAirBagOK = isAirBagOK
        self.isPaintingOK = isPaintingOK
        self.isMechanicOK = isMechanicOK

car_01 = Car("Seat", "Ibiza", True, True, True)
car_02 = Car("Opel", "Corsa", True, False, True)

print(car_01.model, car_01.brand)

#roznica miedzy konstruktorem a init: jak uruchamiany jest konstruktor to obiektu jeszczze nie ma. kiedy jest wywolywany init to obiekt juz istnieje