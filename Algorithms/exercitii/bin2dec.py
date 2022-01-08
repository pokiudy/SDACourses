'''
Binary to Decimal:
Numar: 01001011

[6][5][4][3][2][1][0]
 1  0  0  1  0  1  1

(2 ** 7) * 0 +
(2 ** 6) * 1 +
(2 ** 5) * 0 +
(2 ** 4) * 0 +
(2 ** 3) * 1 +
(2 ** 2) * 0 +
(2 ** 1) * 1 +
(2 ** 0) * 1 +
dec

(base ** power) * bit

Selectam doar valaorile cu "1"
(2 ** 6) * 1 + (2 ** 3) * 1 + (2 ** 1) * 1 + (2 ** 0) * 1

64 + 8 + 2 + 1 = 75

'''
def bin2dec(bin):
    dec = 0
    power = 0
    while bin > 0:
        #selectam ultimul element
        bit = bin % 10
        print("Ultimul element este:", bit)
        '''
        folosit pentru selectarea ultimului element:
        123 % 10 = 3
        187 % 10 = 7
        '''
        result = 2 ** power * bit
        print(f"(2 ** {power}) * {bit}")
        dec += result

        # aruncam ultimul element
        new_bin = bin // 10
        print("Noul numar dupa eliminarea ultimului element", new_bin)
        bin = new_bin

        power = power + 1
        print("Marim puterea cu fecare iteratie:", power)

    return dec

print(bin2dec(1001011))