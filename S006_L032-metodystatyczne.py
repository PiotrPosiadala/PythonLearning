'''
Metoda operująca na poziomie klasy: 
    Dekorator @classmethod
    cls - skrót od class
    * - sluzy do przekazania oddzielnych wartosci, chroni przed przekazaniem jednej listy
    
    @classmethod
    def ReadFromText(cls, aText):
        aNewCar = cls(*aText.split(':'))
        return aNewCar

    Car.ReadFromText(lineofText)

Metoda statyczna - nie musi mieć żadnego związku z klasą. 
    Dekorator @staticmethod

    @staticmethod
    def Convert_KM_KW(KM):
        return KM * 0.735

    Nie przekazujemy żadnych parametrów, nawet self'a.

Metody klasy i metody statyczne można wywolywać na rzecz instancji. 

https://pl.wikibooks.org/wiki/Zanurkuj_w_Pythonie/Praca_z_katalogami
https://pl.python.org/docs/tut/node9.html#foot972
'''
import pickle  #zapisywanie obiektu do plikow
import glob #mozna latwo pozyskac pelne sciezki do pliku

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

    def save_to_file(self, path):
        print(">>>Opening file. Path = {}".format(path))
        with open(path, 'wb') as f:
            print(">>>Object dumping.")
            pickle.dump(self, f)
            f.close()

    @classmethod
    def read_from_file(cls, path):
        print(">>>Opening file. Path = {}".format(path))
        with open(path, 'rb') as f:
            newCake = pickle.load(f)
            print(">>>Object read.")
        cls.bakkery_offer.append(newCake)
        return newCake
        
    @staticmethod
    def get_bakery_files(path):
        print(">>>get_bakery_files")
        bakery_path = '*.bakery'
        return glob.glob(path+bakery_path)


    Text = property(__getText, __setText, None)

cake01 = Cake("Ponczek", "cake", "slodki", ["puder", "likier"], ["dzem", "pusty"], True, "tekscik")
cake02 = Cake("Wuzetka", "tort", "slodki", [], ["smietanka"], True, "")
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], [], False, "")
cake03.setFilling("dzemor")
cake03.addAdditives(["owoce","bita smietana"])

cake01.save_to_file('d:/Python/python_tutorial_udemy/S006_L032-metodystatyczne/cake01.bakery')
cake02.save_to_file('d:/Python/python_tutorial_udemy/S006_L032-metodystatyczne/cake02.bakery')
print("Bakkery offer = {}".format(Cake.bakkery_offer))

cake05 = Cake.read_from_file('d:/Python/python_tutorial_udemy/S006_L032-metodystatyczne/cake01.bakery')
cake05.showInfo()
print("Bakkery offer = {}".format(Cake.bakkery_offer))

print(Cake.get_bakery_files('d:/Python/python_tutorial_udemy/S006_L032-metodystatyczne/'))