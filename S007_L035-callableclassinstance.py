'''
Obiekty mozna wywolywac tak jakby byly funkcja. 

Sprawdzanie czy jest callable: callable(MemoryClass), callable(mem)

Normalnie jak mamy __init__ to Klasę mozna wywolywać, a metody nie.
Jest taka funkcja predefiniowalna __call__(init)

def __call__(self,item):
    self.list_of_items.append(item)

'''

class NoDuplicates:
    def __init__(self):
        self.list = []
    
    def __call__(self, new_items):
        for i in new_items:
            if i not in self.list:
                self.list.append(i)
            else:
                print(">>>{} already in list".format(i))

my_no_dup_list = NoDuplicates()
my_no_dup_list(['keyboard','mouse'])
print(my_no_dup_list.__dict__)

my_no_dup_list(['keyboard','mouse','pendrive'])
print(my_no_dup_list.__dict__)

my_no_dup_list(['charger','pendrive'])
print(my_no_dup_list.__dict__)