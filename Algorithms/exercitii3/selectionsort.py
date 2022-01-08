def selection_sort(list):
    # un loop va trece prin lista pana la final
    for i in range(0, len(list)):
        indexul_celui_mai_mic_element = i # index:[0] = element:4

        # al doilea loop va cauta si compara elementele in scopul gasirii celui mai mic element
        for j in range(i + 1, len(list)):

            if list[j] < list[indexul_celui_mai_mic_element]:
                indexul_celui_mai_mic_element = j

            if indexul_celui_mai_mic_element != i:
                list[indexul_celui_mai_mic_element], list[i] = list[i], list[indexul_celui_mai_mic_element]

    return list

list = [4, 6, 2, 8, 7]
selection_sort(list)
print(list)