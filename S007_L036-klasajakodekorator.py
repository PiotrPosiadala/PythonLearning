'''
import random
random.choice(list_of_cars)

Żeby funkcje udekorować klasą to ta klasa musi mieć metodę:

class MemoryClass:
    
    list_of_already_selected_items = []
    
    def __init__(self,funct):
        self.funct = funct

    def __call__(self,list):
        items_not_selected = [i for i in list if i not in MemoryClass.list_already_selected_items]
        item = self.funct(items_not_selected)
        MemoryClass.lis_of_already_selected_items.append(item)
        return item

cars = ['Opel', 'Toyota', 'Mazda', 'Renault']

@MemoryClass
def SelectTodayPromotion(list_of_cars):
    return random.choice(list_of_cars)

@MemoryClass
def SelectTodayShow(list_of_cars):
    return random.choice(list_of_cars)

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
    
    def add_additives(self, additives):
        self.additives.extend(additives)
    
class NoDuplicates:

    def __init__(self, funct):
        print(">>> NoDuplicates init called")
        self.funct = funct

    def __call__(self, cake, additives):
        print('>>> NoDuplicates call function for cake={} additives={}'.format(cake,additives))
        no_duplicate_list = []
        for a in additives:
            if a not in cake.additives:
                no_duplicate_list.append(a)
        self.funct(cake, no_duplicate_list)


@NoDuplicates
def add_extra_additives(cake, additives):
    cake.add_additives(additives)


cake01 = Cake('Vanilla Cake','cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

add_extra_additives(cake01, ['strawberries', 'sugar-flowers'])
cake01.show_info()
    
add_extra_additives(cake01, ['strawberries', 'sugar-flowers','chocolade', 'nuts'])
cake01.show_info()



