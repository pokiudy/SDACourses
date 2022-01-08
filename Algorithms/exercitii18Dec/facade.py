"""
10  16
------
1   1
2   2
.....
9   9
10  A
11  B
12  C
13  D
14  E
15  F
16  10
17  11
18  12
"""

# hexa = '17A' #378
# 1 * 16^2 + 7 * 16^1 + A[10] * 16^0
# hexa = 'FFF' #4095
# 15 * 16^2 + 15 * 16^1 + 15 * 16^0
# hexa = '‭C410B‬' #803083
# 12*16^4 + 4*16^3 + 1*16^2 + 0*16^1 + 11*16^0

"""
Sa se creeze o functie denmita: hex2dec, ce va primii ca parametru 
un numar sub format de string hexadecimal (e.g. 17A)
Functia trebuie sa returneze valoarea lui decimala.
Hint! aveti nevoie de un dictionar in care sa stocati literele de la 
A-F si corespondentul lui in decimal.
"""

'''
10  16
------
1   1
2   2
.....
9   9
10  A
11  B
12  C
13  D
14  E
15  F
16  10
17  11
18  12
'''

# hexa = '17A' #378
#1 * 16^2 + 7 * 16^1 + A[10] * 16^0
# hexa = 'FFF' #4095
#15 * 16^2 + 15 * 16^1 + 15 * 16^0
# hexa = '‭C410B‬' #803083
# 12*16^4 + 4*16^3 + 1*16^2 + 0*16^1 + 11*16^0

'''
Sa se creeze o functie denmita: hex2dec, ce va primii ca parametru 
un numar sub format de string hexadecimal (e.g. 17A)
Functia trebuie sa returneze valoarea lui decimala.
Hint! aveti nevoie de un dictionar in care sa stocati literele de la 
A-F si corespondentul lui in decimal.
'''

def hex2dec(hex):
    map = {
        "A" : 10,
        "B" : 11,
        "C" : 12,
        "D" : 13,
        "E" : 14,
        "F" : 15
    }

    puteri = len(hex) - 1
    rezultat = 0
    for i in hex:

        if i in map:
            rezultat += int(map[i] * 16 ** puteri)
            puteri -= 1
        else:
            rezultat += int(i) * 16 ** puteri
            puteri -= 1

    print(rezultat)

hex2dec("17A")
hex2dec("FF")
