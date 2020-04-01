import os

def countWords(path):
    with open(path,'r') as f:
        content = f.read()
        word_count = len(content.split())
    return word_count

path = r'd:\Python\python_tutorial_udemy\data.txt'

if os.path.isfile(path):
    print("There are {} words in file {}.".format(countWords(path),path))

#os.path.isfile(path) and print("There are {} words in file {}.".format(countWords(path),path))

