'''

Operatory zaczynaja sie od def __[...]__

Metoda extend moze rozszerzyc liste o elementy nowej listy, np. liste stringow
Metoda append moze rozszerzyc liste o nowy element, np. string

if:

else: 
    raise Exception("")


+  --> __add__
print(klasa) --> __str__
'''


class Cake:
    
    bakery_offer = []
    
    def __init__(self, name, kind, taste, additives, filling):
    
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
    
    def __str__(self):
        return("Kind = {}, Name = {}, Additives = {}".format(self.kind, self.name, self.additives))

    def __iadd__(self, other):
        if type(other) is str:
            additives = self.additives
            additives.append(other)
            return Cake(self.name, self.kind, self.taste, additives, self.filling)
        elif type(other) is list:
            additives = self.additives
            additives.extend(other)
            return Cake(self.name, self.kind, self.taste, additives, self.filling)
        else:
            raise Exception("Additives have to be string or list of strings! {} cannot be used!".format(type(other)))


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
        print('-'*20)
    
        
cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
print(cake01)

cake01 += 'caramel'
print(cake01)

cake01 += ['other_caramel', 'ice_creams']
print(cake01)

cake01 += 1
print(cake01)