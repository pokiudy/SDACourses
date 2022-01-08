list = [3, 2, 5, 7, 4]


def inseration_sort(list):
    for i in range(1, len(list)):
        print(f"Elementul curent din lista Nesortata ce va fi introdus in lista Sortata este: {list[i]}")
        print(f"Noua lista nesortata este: {list[i:]}")
        for j in range( i-1, -1, -1):
            print(f"Comparam elementul nou introdus, si anume: {list[j+1]} cu elementul deja aflat in lista sortata, si anume: {list[j]} ")
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
            else:
                break


if __name__ == "__main__":
    lista = [3, 2, 5, 7, 4]

    inseration_sort(lista)