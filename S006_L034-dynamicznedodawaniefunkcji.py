'''
writer = csv.writer(file, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
writer.writerow(header)

Mozna dodac sobie do klasy nowa funckje
Car.ExportToFile = exportToFile
  

Metoda dla klasy:
def exportToFile_Class(cls, path):
    with ope(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["brand", "model", "IsOnSale"])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])

Car.ExportToFile_Class = types.MethodType(exportToFile_Class, Car)

--------------
Metoda dla instancji: 

def exportToFile_Instance(self,path):
    with ope(path, mode="w") as file:
        writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(["brand", "model", "IsOnSale"])
        writer.writerow([self.brand, self.model, self.IsOnSale])

car01.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_01)

sprawdzenie czy metoda istnieje: hasattr(car_01, 'Export')
Czy mozna wywolac callable(car01.Export) 


'''
import csv # modul pozwalazacy na eksportowanie do csv
import types #do przypisywania metod dla klasy


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

def export_1_cake_to_html(obj, path):
    template = """
<table border=1>
        <tr>
        <th colspan=2>{}</th>
        </tr>
        <tr>
            <td>Kind</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Taste</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Additives</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Filling</td>
            <td>{}</td>
        </tr>
</table>"""
    
    with open(path, "w") as f:
        content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
        f.write(content)

def export_all_cakes_to_html(cls, path):
    template = """
<table border=1>
        <tr>
        <th colspan=2>{}</th>
        </tr>
        <tr>
            <td>Kind</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Taste</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Additives</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Filling</td>
            <td>{}</td>
        </tr>
</table>"""
    
    with open(path, "w") as f:
        for obj in cls.bakery_offer:
            content = template.format(obj.name, obj.kind, obj.taste, obj.additives, obj.filling)
            f.write(content)

def export_this_cake_to_html(self, path):
    template = """
<table border=1>
        <tr>
        <th colspan=2>{}</th>
        </tr>
        <tr>
            <td>Kind</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Taste</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Additives</td>
            <td>{}</td>
        </tr>
        <tr>
            <td>Filling</td>
            <td>{}</td>
        </tr>
</table>"""
    
    with open(path, "w") as f:
        content = template.format(self.name, self.kind, self.taste, self.additives, self.filling)
        f.write(content)
    
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


Cake.Export_1_cake_to_html = export_1_cake_to_html
Cake.Export_1_cake_to_html(cake01,'d:/Python/python_tutorial_udemy/S006_L034-dynamicznedodawaniefunkcji/cake01_static.html' )

Cake.Export_all_cakes_to_html = types.MethodType(export_all_cakes_to_html, Cake)
Cake.Export_all_cakes_to_html('d:/Python/python_tutorial_udemy/S006_L034-dynamicznedodawaniefunkcji/all_cakes_class.html')

for cake in Cake.bakery_offer:
    cake.Export_this_cake_to_html = types.MethodType(export_this_cake_to_html, cake)

for cake in Cake.bakery_offer:
    cake.Export_this_cake_to_html('d:/Python/python_tutorial_udemy/S006_L034-dynamicznedodawaniefunkcji/instance_method_{}.html'.format(cake.name.replace(" ","_")))


