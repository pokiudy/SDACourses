def recursiv(parametru):
    if parametru < 2:
        return parametru
    else:
        return parametru * recursiv(parametru - 1)

print(recursiv(5))


string = "salutariSdaAcademy!"

def counter(string):
    result = 0
    for i in string:
        result += 1

    return result

print(counter(string))


