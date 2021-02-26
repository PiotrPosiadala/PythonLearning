class Cake: 
    def __init__(self, name, kind, taste, addictions, fillings):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.addictions = addictions
        self.fillings = fillings

cake01 = Cake("Ponczek", "ciastko", "slodki", ["puder", "likier"], ["dzem", "pusty"])
cake02 = Cake("Wuzetka", "tort", "slodki", [], ["smietanka"])
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], [])

bakkery_offer = []
bakkery_offer.append(cake01)
bakkery_offer.append(cake02)
bakkery_offer.append(cake03)

for cake in bakkery_offer:
    print("{} - ({}) main taste: {} with additives of {} filled with {}".format(cake.name, cake.kind, cake.taste, cake.addictions, cake.fillings))
