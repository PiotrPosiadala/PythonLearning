'''
Wygodne jest dodanie w klasie atrybutu ukrytego __IsOnSale i przypisywanie do niego IsOnSale=property(getter, setter, )

Mozna też zdefiniować funkcję IsOnSale zwracającą wartośćparametru ukrytego, ale poprzedzając ją dekoratorem @property.

@property
def IsOnSale(self):
    return self.__IsOnSale

Wtedy wywolujemy car01.IsOnSale - bez nawiasow
Nie uda sie wtedy zmiana tej wlasciwosci bo był ustawiony setter, a teraz go nie ma. Rozwiazanie - funkcje ktora ma byc setterem poprzedzamy dekoratorem @IsOnSale.setter
Uwaga! Setter musi byc zdefiniowany po properties!

Moożna też ustawić deleter - @IsOnSale.deleter

Inne: format().title() - zamieni na słowa zaczynające się od dużej litery



'''
class Cake:
    
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel','other']
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling, gluten_free,text):
    
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if kind == 'cake' or text == '':
            self.__text = text
        else:
            self.__text = ''
            print('>>>>>Text can be set only for cake ({})'.format(name))
    
    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print("Gluten free: {}".format(self.__gluten_free))
        if len(self.__text) > 0:
            print("Text:      {}".format(self.__text))
        print('-'*20)
    
    def set_filling(self, filling):
        self.filling = filling
    
    def add_additives(self, additives):
        self.additives.extend(additives)

    @property
    def Text(self):
        return self.__text
    
    @Text.setter
    def Text(self, new_text):
        if self.kind == 'cake':
            self.__text = new_text
        else:
            print('>>>>>Text can be set only for cake ({})'.format(self.name))


    
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, 'Happy Birthday Margaret!')
cake02 = Cake('Chocolade Muffin','muffin', 'chocolade', ['chocolade'], '', False, '')
cake03 = Cake('Super Sweet Maringue','meringue', 'very sweet', [], '', True, '')
cake04 = Cake('Cocoa waffle','waffle','cocoa',[],'cocoa', False, 'Good luck!')
    
print("Today in our offer:")
for c in Cake.bakery_offer:
    c.show_info()
    
cake01.Text = 'Happy birthday!'
cake02.Text = '18'
    
for c in Cake.bakery_offer:
    c.show_info()