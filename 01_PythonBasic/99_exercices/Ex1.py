# 1
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}

dic3 = {}
for x in (dic1, dic2):
    dic3.update(x)
print(dic3)


# 2
dic3 = {1: 10, 2: 20, 3: 30, 4: 40}
for x in dic3:
    print(x)

# 4
dic_sum = sum(dic3.values())
dic_max = min(dic3.values())
dic_min = max(dic3.values())
print(dic_sum)
print(dic_min)
print(dic_max)




