# rows = 5
# for i in range(rows + 1, 0, -1):
#     # nested reverse loop
#     for j in range(0, i - 1):
#         # display star
#         print("*", end=' ')
#     print(" ")
#
# rows = 10
# k = 2 * rows - 2
# for i in range(0, rows):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")
#
# k = rows - 2
#
# for i in range(rows, -1, -1):
#     for j in range(k, 0, -1):
#         print(end=" ")
#     k = k + 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")

n=10
l = [(" " * (n-i) + "*" * i * 2 + " " * (n-i)) for i in range(n)]
for i in range(len(l)):
    print(l[i])

# #Varianta 1: cu list comprehension
# n = 8
# l_nou = []
# l_nou = [" " * (int(n * 2) - i) + '**' * i for i in range(n)]
# for steluta in l_nou:
#  print(steluta)
#
# print('\n')
#
#
#
# #Varianta 2: cu matrice
# rows = 10
# k = 2 * rows - 2
# for i in range(0, rows):
#     for j in range(0, k):
#         print(end=" ")
#     k = k - 1
#     for j in range(0, i + 1):
#         print("* ", end="")
#     print("")
# print('\n')
#
#
#
# #Varianta lui Radu programmer
# l = [ (" "* (n-i) + "*" * i * 2 + " " * (n-i)) for i in range(n) ]
# for i in range(len(l)):
#      print(l[i])


# Bradul mai estetic

lista = []

n = 10

lista = [f'{"* " * i: ^{n * 2 - 2}}' for i in range(1, n)]
for i in lista:
    print(i)