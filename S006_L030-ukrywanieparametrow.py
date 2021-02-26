"""
Jesli przed nazwa atrybutu dodamy __ to bedize on ukryty. Np self.__isOnSale
Jesli w programie bedziemy probwac ta zmienna zmienic to po wywolaniu var(car01) dostaniemy
_Car__isOnSale - tak zostaje ukryty ten atrybut 
__isOnSale - tworzony jest kompletnie nowy atrybtut
Jesli zmienimy ten pierwszy atrybut, to faktycznie zmieni sie ten ukryty, zdefiniowanny na poczarku w klasie 
Wniosek = pythonowe klasy nie brionią się dobrze
Mozna tez juz w programie bez problemu dodac nowy atrybut do obiektu, ale można go tez usunac 
(car01.YerOfProduction = 2005
del car01.YerOfProduction lub delattr(car01, 'TAXI'))

Jest nawet specjalna funkcja do dodawania atrybutow
setattr(car01, 'TAXI', False)

Sprawdzenie czy obiekt posiada dany atrybut
hasattr(car01, 'TAXI')
"""

class Cake: 
    
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other'] 
    bakkery_offer = []

    def __init__(self, name, kind, taste, addictions, fillings, glutenfree):
        self.name = name
        if kind in self.known_types:
            self.kind = kind
        else:
            self.kind = "other"
        self.taste = taste
        self.addictions = addictions
        self.fillings = fillings
        self.__glutenfree = glutenfree
        self.bakkery_offer.append(self)

    def showInfo(self):
        print("---{}---".format(self.name).upper())
        print("Taste: {}".format(self.taste))
        if self.addictions:
            print("Additions: {}".format(self.addictions))
        if self.fillings:
            print("Fillings: {}".format(self.fillings))
        # if self.__glutenfree.:
        #     print("GlutenFree: {}".format(self.__glutenfree))
        print("GlutenFree: {}".format(self.__glutenfree))

    def setFilling(self, filling):
        self.fillings.extend(filling)
    
    def addAdditives(self,additive):
        self.addictions.extend(additive)


cake01 = Cake("Ponczek", "ciastko", "slodki", ["puder", "likier"], ["dzem", "pusty"], True)
cake02 = Cake("Wuzetka", "tort", "slodki", [], ["smietanka"], True)
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], [], False)
cake03.setFilling("dzemor")
cake03.addAdditives(["owoce","bita smietana"])

for cake in Cake.bakkery_offer:
    cake.showInfo()

print("##########################")
print(vars(cake01))
cake01.__glutenfree = False
print(vars(cake01))   
cake01._Cake__glutenfree = False
print(vars(cake01))


