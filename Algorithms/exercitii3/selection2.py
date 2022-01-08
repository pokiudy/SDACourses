def selection_sort(list):
    # un loop va trece prin lista pana la final

    for i in range(0, len(list)):
        indexul_celui_mai_mic_element = i  # index:[0] = element:4
        am_gasit_un_nou_element_de_minim = False

        # al doilea loop va cauta si compara elementele in scopul gasirii celui mai mic element
        for j in range(i + 1, len(list)):
            if list[j] < list[indexul_celui_mai_mic_element]:
                indexul_celui_mai_mic_element = j
                am_gasit_un_nou_element_de_minim = True

            if am_gasit_un_nou_element_de_minim == True:
                list[indexul_celui_mai_mic_element], list[i] = list[i], list[indexul_celui_mai_mic_element]

    return list


list = [6, 7, 8, 7, 6, 5, 4, 5, 6, 7, 6, 7, 8, 9, 7, 9, 0]
selection_sort(list)
print(list)