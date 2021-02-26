"""
id(class)
id(instance)
isinstance(car01,Car)
type(car01) is Car 
car01.__class__
vars(car01) - slownik atrybutow
vars(Car) - zwraca slownik WAZNE!
Mozna tez zdefiniowac atrybuty klasy przed __init__ - bezposrednio w klasie - zmienne zdefiniowane na poziomie klasy
Np. NumberofCars mozna zwiekszac w kazdym init
dir(car01) - pokazuje metody ktore mozna wywolac na rzecz danej klasy oraz atrybuty instancji
dir(Car) - pokazuje metody ktore mozna wywolac na rzecz danej klasy oraz zmienne tej klasy
"""

class Cake: 
    
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other'] 
    bakkery_offer = []

    def __init__(self, name, kind, taste, addictions, fillings):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = "other"
        self.taste = taste
        self.addictions = addictions
        self.fillings = fillings
        self.bakkery_offer.append(self)

    def showInfo(self):
        print("---{}---".format(self.name).upper())
        print("Taste: {}".format(self.taste))
        if self.addictions:
            print("Additions: {}".format(self.addictions))
        if self.fillings:
            print("Fillings: {}".format(self.fillings))
    
    def showAllInfo(self):
        for elmnt in self.bakkery_offer:
            print("---{}---".format(elmnt.name).upper())
            print("Taste: {}".format(elmnt.taste))
            if elmnt.addictions:
                print("Additions: {}".format(elmnt.addictions))
            if elmnt.fillings:
                print("Fillings: {}".format(elmnt.fillings))    
    
    def setFilling(self, filling):
        self.fillings.extend(filling)
    
    def addAdditives(self,additive):
        self.addictions.extend(additive)


cake01 = Cake("Ponczek", "ciastko", "slodki", ["puder", "likier"], ["dzem", "pusty"])
cake02 = Cake("Wuzetka", "tort", "slodki", [], ["smietanka"])
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], [])

cake01.showInfo()
cake03.showInfo()
cake03.setFilling("dzemor")
cake03.addAdditives(["owoce","bita smietana"])
cake03.showInfo()

print("--------------------------------------------")
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa')
print(cake04.kind)
print(Cake.bakkery_offer)
print("--------------------------------------------")
cake01.showAllInfo()
print("--------------------------------------------")

print(dir(cake01))
print(vars(cake01))