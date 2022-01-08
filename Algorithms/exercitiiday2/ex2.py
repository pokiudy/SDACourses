#Sa se numere consoanele atat iterativ cat si recursiv

vocale = "aeiou"

input_str = "abcde"

def count_consonants(text):
    counter_consoane = 0
    for caracter in text:
        print(caracter)
        if caracter not in vocale:
            counter_consoane += 1
    return counter_consoane

print(count_consonants(input_str))

print("========================================")

def count_consonants2(text2):
    counter_consoane = 0
    for index in range(len(text2)):
        print(f"indexul curent este: {index}")
        print(f"caracterul este: {text2[index]}")
        if text2[index] not in vocale:   # fara text2[index] nu se afiseaza caracterele doar indexul

            counter_consoane += 1
    return counter_consoane

print(f"numarul consoanelor este: {count_consonants2(input_str)}")

print("========================================")
#recursiv
# iter 1 : a b c d e
# iter 2: b c d e
# iter 3: c d e
# iter 4: d e
# iter 5: e
# iter 6: 0
def nr_consoane_recursiv(text):
    print(f"inainte de slice-ul urmator ---> {text}")
    if text == "":
        return 0
    if text[0] not in vocale:
        return 1 + nr_consoane_recursiv(text[1:])
    else: # aici am intalnit o vocala
        return nr_consoane_recursiv(text[1:])

print(nr_consoane_recursiv(input_str))
