import itertools
from operator import itemgetter

def wordCounter (file):
    try: 
        file = open('text.txt', 'r')    

    except:
        print('Error al leer el archivo.')
    
    wordsCounter = {}
    for line in file: 
        line.rstrip()
        arrayLine = line.split(" ")
        for x in arrayLine:
            if x in wordsCounter:
                # print('Esta el elemento')
                value = wordsCounter.get(x)
                wordsCounter.update({x: value+1})
            else:
                wordsCounter.update({x: 1})
    wordsCounter = dict(sorted(wordsCounter.items(), key=lambda item: item[1], reverse=True))
    return print(dict(itertools.islice(wordsCounter.items(), 10)))
    
wordCounter(input('Porfavor ingrese nombre del archivo: '))