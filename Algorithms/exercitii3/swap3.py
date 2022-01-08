def insertion_sort(list):
    # primul for trece prin lista nesortata
    for index in range(1, len(list)):  # [0] = 2

        index_element_de_stanga = index - 1  # accesam elementul din stanga lui = 3

        while list[index_element_de_stanga] > list[index_element_de_stanga + 1] and index_element_de_stanga >= 0:
            list[index_element_de_stanga], list[index_element_de_stanga + 1] = list[index_element_de_stanga + 1], list[
                index_element_de_stanga]
            index_element_de_stanga -= 1


list = [3, 2, 5, 7, 4]
insertion_sort(list)
print(list)