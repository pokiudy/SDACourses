# def new_bubble(list):
#     for i in range(0, len(list) - 1):
#         for j in range(0, len(list) - 1 - i):
#             if list[j] > list[j + 1]:
#                 list[j], list[j +1] = list[j +1], list[j]
#


def bubble_sort(list):
    for index in range(0, len(list) - 1): #5 cu 9, 9 cu 1, 1 cu 2, 2 cu 7, 7 cu !!!
        for j in range(0, (len(list) - 1 - index)):
            # index = 0 { len(list) = (5 - 1) - 0 = 4 }
            # index = 1 { len(list) = (5 - 1) - 1 = 3 }
            # index = 2 { len(list) = (5 - 1) - 2 = 2 }
            # index = 3 { len(list) = (5 - 1) - 3 = 1 }
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]

list = [5, 9, 1, 2, 7, 10, 99]
bubble_sort(list)
print(list)