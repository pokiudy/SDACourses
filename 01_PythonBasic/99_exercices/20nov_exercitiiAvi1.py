coada_salata=['Alex', 'Mihai', 'Nicoleta', 'Klaudia']
for i in range(len(coada_salata)):
    print(f'{coada_salata[i]} a cumparat 3 kg de salata')

    #coada_salata.pop(0)
    print(coada_salata)


while coada_salata:     #cat timp avem ceva in lista si se valideaza cu True
    x=coada_salata.pop(0)  #FIFO = first in, first out   cu pop(0) se scoate mereu primul element
    print(f'{x} a cumparat 3 kg de salata')