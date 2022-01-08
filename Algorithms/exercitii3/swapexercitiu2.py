def insertion_sort(lista):
    for i in range(1, len(lista)):
        print(f"Elementul din lista nesortata ce va fi introdus in lista sortata este: {lista[i]}")
        print(f"Noua lista nesoratata este: {lista[i:]}")
        for j in range(i - 1, -1, -1):
            print(f"Comparam elementul din partea dreapta {lista[j + 1]} cu elementul din partea stanga {lista[j]}")
            if lista[j + 1] < lista[j]:
                lista[j + 1], lista[j] = lista[j], lista[j + 1]
            else:
                break


if __name__ == "__main__":
    lista = [3, 2, 5, 7, 4]

    insertion_sort(lista)

    print(lista)