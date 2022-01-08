'''
PEP 20  - link: https://www.python.org/dev/peps/pep-0020/

PEP 08  - link: https://www.python.org/dev/peps/pep-0008/
        - defineste formatarea codului.
        - maximul de caractere pe un rand sa fie de 79 (~90)
        - tot timpul folositi TAB! nu spatii!!!

1. Indentarea functiilor si alinierea multiplilor parametrii

# wrong
foo = function_long_parameter(param1, param2, param3, param4, param5)
foo = function_long_parameter(
param1,
param2,
param3,
param4,
param5
)

# correct
foo = function_long_parameter(param1, param2,
                            param3, param4,
                            param5)

# in caz de definiere a corpului functiei

# wrong
def function_long_parameter(param1, param2, param3, param4, param5)
    print("Hello")
    return

# wrong
def function_long_parameter(param1, param2,
    param3, param4, param5)
    print("Hello")
    return

# correct
def function_long_parameter(param1, param2,
                            param3, param4,
                            param5)
    print("Hello")
    return


2. In cazul operatorilor binari se face linebreak inainte sau dupa ei?

# limit correct/wrong
income = (variabila1 + variabila2 - (variabila3 / variabila5) * variabila4)

#wrong
income = (variabila1 +
        variabila2 -
        (variabila3 / variabila5) *
         variabila4)

# correct
income = (variabila1
        + variabila2
        - (variabila3 / variabila5)
        * variabila4)



3. Formatarea importurilor

# wrong
import os, sys, time

# correct
import os
import sys
import time

4. Dunder fields __***__

__author1__ = "Mihai"
__author2__ = "Corina"
__version__ = 0.1
__project__ = "SdaAcademy"

# Dunder fields-urile de mai sus trebuie sa fie tot timpul deasupara importului

# wrong
import os
import sys
import time

__author1__ = "Mihai"
__author2__ = "Corina"
__version__ = 0.1
__project__ = "SdaAcademy"

#correct
__author1__ = "Mihai"
__author2__ = "Corina"
__version__ = 0.1
__project__ = "SdaAcademy"

import os
import sys
import time

# singurul lucru ce preceda dunder fields-urile sunt comentarile modului ce sunt tot timpul
# inglobate in 3 ghilimele

# wrong
# Acest modul, citeste din fisiere CSV.

# corect
"""
Acest modul, citeste din fisiere CSV.
"""

5. Evitarea whitespace-urilor in urmatoarele situatii:
a. Imediat in interiorul parantezelor:

# correct:
spam(ham[1], {eggs: 2})

#wrong
spam( ham[ 1 ], { eggs: 2 } )

b. Imediat inainte virgula

#correct:
if x == 4: print x, y, z

#wrong:
if x == 4: print x , y , z

c. Imediat inainte de paranteza functiei

#correct:
make_breakfast(4)

#wrong
make_breakfast (4)

d. Spatierea inuitla in timpul assgiment-ului

#correct:
x = 5
long_varaible = 4

#wrong:
x               = 5
long_varaible   = 4

e. In momentul definirii parametrilor default

#wrong
def do_some(real, imag = 4):

#correct:
def do_some(real, imag=4):


6. Format in definierea variabileleor

b (single lowercase letter)
B (single uppercase letter)
lowercase
lower_case_with_underscores
UPPERCASE
UPPER_CASE_WITH_UNDERSCORES
CapitalizedWords (CamelCase)

#wrong
Capitalized_Words_With_Underscores (ugly!)


7. Functii de maxim 2 linii de cod sa se converteasca in lambda:

#wrong
def f(x): retunr x*x

#correct:
f = lambda x: x*x

8. Corpul Try-Except trebuie sa contina si un backfield

#wrong
try:
    value = 5
except KeyError:
    print("Worng")

#correct:
try:
    value = 5
except KeyError:
    print("Worng")
else:
    print("alta exceptie")

9. Compararea boolean-elor

x = True

#worse
if x is True:
    ---

#wrong
if x == True:
    ---

#correct:
# if x:
    ---

10. In cazul selectarii inceputului sau sfarsitului de cuvant sa se foloseasca
@startwith(), endwith()

x = "Florin"
y = "Floare"

#wrong
if y == x[:1] # verificare daca y incepe cu acelasi cuvant ca x

#correct
if y.startswith("F")
'''