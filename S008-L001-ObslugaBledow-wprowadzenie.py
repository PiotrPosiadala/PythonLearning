import requests
import os
import shutil
    
def save_url_to_file(url, file_path):
        
    r = requests.get(url, stream = True)     
    with open(file_path, "wb") as f: 
        f.write(r.content)
    
url = 'http://www.mobilo24.eu/spis/'
dir = 'c:/temp/'
tmpfile = 'download.tmp'
file = 'spis.html'
    
tmpfile_path = os.path.join(dir, tmpfile)
file_path = os.path.join(dir, file)