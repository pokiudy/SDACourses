def bubble_sort(lista):
    for i in range(0, len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[j] < lista[i]:
                lista[j], lista[i] = lista[i], lista[j]


def bubble_sort2(lista):
    for i in range(0, len(lista)):
        for j in range(0, (len(lista) - i - 1)):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]