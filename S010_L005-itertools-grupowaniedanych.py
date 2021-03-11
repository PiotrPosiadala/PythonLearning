import os 
import itertools

def scantree(path):
    for object in os.scandir(path):
        if object.is_dir():
            yield object
            yield from scantree(object.path)
        else:
            yield object


listing = scantree('D:/temp')
for l in listing:
    print('DIR ' if l.is_dir() else 'FILE', l.path)
 
 
listing = scantree('D:/temp')
listing = sorted(listing, key=lambda e: e.is_dir())
 
for is_dir, elements in itertools.groupby(listing, key=lambda e: e.is_dir()):
    print('DIR ' if is_dir else 'FILE', len(list(elements)))