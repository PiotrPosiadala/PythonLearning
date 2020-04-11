import os
import urllib.request

data_dir = r'd:\Python\python_tutorial_udemy\2_13_lab'

pages = [
    { 'name': 'mobilo',      'url': 'http://www.mobilo24.eu/'},
    { 'name': 'nonexistent', 'url': 'http://abc.cde.fgh.ijk.pl/' },
    { 'name': 'kursy',       'url': 'http://www.kursyonline24.eu/'} ]


for page in pages:

    try:
        file_name = "{}.html".format(page["name"])
        path = os.path.join(data_dir, file_name)
        print("Path: {}".format(path))

        print ("Processing: {} => {} ...". format(page["url"], file_name))
        urllib.request.urlretrieve(page["url"],path)
        print("...done")
    
    except:
        print("FAILURE processing web page: {}".format(page["name"]))
        print("Stopping the process")
        break
    
    else:
        print("All pages downloaded succesfully!")


