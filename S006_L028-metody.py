#W tworzeniu metody dodawac trzeba self w argumentach
class Cake: 
    
    def __init__(self, name, kind, taste, addictions, fillings):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.fillings = fillings

    def showInfo(self):
        print("---{}---".format(self.name).upper())
        print("Taste: {}".format(self.taste))
        if self.addictions:
            print("Additions: {}".format(self.addictions))
        if self.fillings:
            print("Fillings: {}".format(self.fillings))
    
    def setFilling(self, filling):
        self.fillings.extend(filling)
    
    def addAdditives(self,additive):
        self.addictions.extend(additive)


cake01 = Cake("Ponczek", "ciastko", "slodki", ["puder", "likier"], ["dzem", "pusty"])
cake02 = Cake("Wuzetka", "tort", "slodki", [], ["smietanka"])
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], [])

bakkery_offer = []
bakkery_offer.append(cake01)
bakkery_offer.append(cake02)
bakkery_offer.append(cake03)

cake01.showInfo()
cake03.showInfo()
cake03.setFilling("dzemor")
cake03.addAdditives(["owoce","bita smietana"])
cake03.showInfo()


