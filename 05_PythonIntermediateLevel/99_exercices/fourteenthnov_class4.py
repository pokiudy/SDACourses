#deschide fisier txt.(un fisier oarecare .txt se deschide in pycharm cu drag and drop

try:
    f = open('exceptii.txt')

#citeste fisierul
    line = f.readline()

#afiseaza

    print(line)

except:
    print("Everything's going to be fine")