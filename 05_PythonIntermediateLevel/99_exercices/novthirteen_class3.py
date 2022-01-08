dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, "Semi": 13600, "Bicycle": 7, "Motorcycle": 110}

#Type your answer here.

lst=[i.upper() for i in dict if dict[i] < 5000]

print(lst)



a_treia_list=["Korina","Kalauz","Niko","Shevcenko"]
a_treia_list=[i for i in a_treia_list[::-1]]


print(a_treia_list)
