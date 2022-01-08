my_lambda = lambda x: x.lower()
print(my_lambda("HA HA HA"))  # "ha ha ha"

square_lambda = lambda x: x ** 2
print(square_lambda(45))

items = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, items))  # [1, 4, 9, 16, 25]

print(squared)

l = [3, 4 , 5, 6]

print(list(map(lambda y: y ** 3, l)))


print("================================")




# Using sorted() function and lambda sort the tuples in the list based on the second items.
lst=[(19542209, "New York") ,(4887871, "Alabama"), (1420491, "Hawaii"), (626299, "Vermont"), (1805832, "West Virginia"), (39865590, "California")]

lambda_second_elem = lambda x: x[1]
lst=sorted(lst, key=lambda_second_elem)

print(lst)


