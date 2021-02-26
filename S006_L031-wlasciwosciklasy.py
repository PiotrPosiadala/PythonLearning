"""
property(getter, setter, deleter, doc) - property to funkcja


"""


class Cake: 
    
    known_types = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other'] 
    bakkery_offer = []

    def __init__(self, name, kind, taste, addictions, fillings, glutenfree, text):
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
        if self.kind == "cake" or not text:
            self.__text = text
        else:
            self.__text = ''
            print(">>>Text cannot be accepted. (Kind = cake or text is empty)")

    def showInfo(self):
        print("---{}---".format(self.name).upper())
        print("Taste: {}".format(self.taste))
        if self.addictions:
            print("Additions: {}".format(self.addictions))
        if self.fillings:
            print("Fillings: {}".format(self.fillings))
        print("GlutenFree: {}".format(self.__glutenfree))
        print("Text: {}".format(self.__text))
        

    def setFilling(self, filling):
        self.fillings.extend(filling)
    
    def addAdditives(self,additive):
        self.addictions.extend(additive)

    def __getText(self):
        return __text

    def __setText(self, newtext):
        print(">>>__setText method called")
        if self.kind == "cake":
            self.__text = newtext
        else:
            print(">>>Text cannot be accepted. (Kind != cake)")

    Text = property(__getText, __setText, None)

cake01 = Cake("Ponczek", "cake", "slodki", ["puder", "likier"], ["dzem", "pusty"], True, "tekscik")
cake02 = Cake("Wuzetka", "tort", "slodki", [], ["smietanka"], True, "")
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], [], False, "")
cake03.setFilling("dzemor")
cake03.addAdditives(["owoce","bita smietana"])

for cake in Cake.bakkery_offer:
    cake.showInfo()

cake01.Text = "lol"
cake01.showInfo()

cake02.Text = "lol"
cake02.showInfo()