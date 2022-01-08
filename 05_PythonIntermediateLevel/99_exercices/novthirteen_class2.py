#model clasic:

l = [4, 5, 10, 20]

my_list = []

for i in l:
    if i < 8:
        my_list.append(i)

print(my_list)


#model cu list comprehension

l = [4, 5, 10, 20]
my_list = [i for i in l if i < 15]
print(my_list)

