"""
1. Sa se reprezite un numar DECIMAL (BAZA 10) in sistem BINAR   (BAZA 2 )
2. Sa se reprezite un numar BINAR   (BAZA 2 ) in sistem DECIMAL (BAZA 10)

1. BAZA 10 -> BAZA 2 (target)

75 / 2 = 37 restul e 0.5, il rotunjim   = 1 [LSB] = less significant bit
37 / 2 = 18 restul e 0.5, il rotunjim   = 1
18 / 2 = 9 restul e 0, il rotunjim      = 0
9 / 2  = 4 restul e 0.5, il rotunjim    = 1
4 / 2  = 2 restul e 0                   = 0
2 / 2  = 1 restul e 0                   = 0
1 / 2  = 0 restul e 0.5, il rotunjim    = 1 [MSB] = most significant bit

                                     [MSB]      [LSB]
Scrierea se face de la MSB la LSB =>   1  00101   1

- MSB se afla intotdeauna in stanga
- LSB se afla intotdeauna in dreapta

Notiunea de binar vine la pachet cu notiunea de bit si de byte
* un bit reprezinta 1 sau 0
* un byte este format INTOTDEAUNA de 8 bits

2 bytes = 16 bits
4 bytes = 32 bits
...

Din cauza ca un byte are tot timpul 8 bits, bitii pana la 8 se pot inlocuii 0

1 byte = 1001 => vrem sa il umplem pentru a putea fi mai usor de citit = 0000 1001
2 bytes 11110110001 => vrem sa il umplem pentru a putea fi mai usor de citit = 0000 0111 1011 0001

"""



"""""" 1.1 Sa se converteasca in binar nr. 121
121 / 2 = 60 rest 0.5 ----> 1
60 / 2 = 30 rest ---------> 0
30 / 2 = 15 rest ---------> 0
15 / 2 = 7 rest 0.5 ------> 1
7 / 2 = 3 rest 0.5 -------> 1
3 / 2 = 1 rest 0.5 -------> 1
1 / 2 = 0 rest 0.5 -------> 1

Rezultatul este: 0111 1001""""""

"""1.2 Sa se converteasca in binar nr. 278 

278 / 2 = 139 rest 0 --------> 0
139 / 2 = 69,5 rest 0.5 -----> 1
69 / 2 = 34,5 rest 0.5 ------> 1
34 / 2 = 17 rest 0 ----------> 0
17 / 2 = 8,5 rest 0,5 -------> 1
8 / 2 = 4 rest 0 ------------> 0 
4 / 2 = 2 rest 0 ------------> 0
2 / 2 = 1 rest 0 ------------> 0 
1/ 2 = 0,5 rest 0,5 ---------> 1

Rezultatul este: 0000000100010110


"""

