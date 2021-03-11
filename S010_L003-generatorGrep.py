import os
import requests


def gen_get_files(dir):
    for file in os.listdir(dir):
        yield os.path.join(dir, file)


def gen_get_file_lines(filename):
    with open(filename, 'r') as f:
        for line in f.readlines():
            yield line.replace('\n', '')


def check_webpage(url):
    try:
        response = requests.get(url)
        return response.status_code==200
    except:
        return False


try:
    os.mkdir('D:/temp/links_to_check')
except:
    pass
    
with open('D:/temp/links_to_check/pl.txt', 'w') as f:
    f.write('http://www.wykop.pl/\n')
    f.write('http://www.ale-beka-jest-taki-aDres.pl/\n')
    f.write('http://www.demotywatory.pl')
    
with open('D:/temp/links_to_check/com.txt', 'w') as f:
    f.write('http://www.realpython.com/\n')
    f.write('http://www.nonexistenturl.com/\n')
    f.write('http://www.stackoverflow.com')


for file in gen_get_files('D:/temp/links_to_check'):
    for line in gen_get_file_lines(file):
        print("{} - {} - {}".format(file, line, check_webpage(line)))
