lista = [3, 8, 4, 9]


def selection_sort(lista):
    for i in range(0, len(lista)):
        min = i
        alt_min_gasit = False

        for j in range(i + 1, len(lista)):
            if lista[j] < lista[min]:
                min = j
                alt_min_gasit = True

            if min != i:
                lista[min], lista[i] = lista[i], lista[min]

    return lista


print(selection_sort(lista))