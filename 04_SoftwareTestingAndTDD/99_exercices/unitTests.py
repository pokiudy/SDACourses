"""
- nucleul testarii este "assert", aici se evalueaza conditia de credibitlitate
- toate assert-urile trebuie sa existe in functii, ce incep cu test_*
- toate functii trebuie sa existe intr-o clasa ce mosteneste unittest.TestCase

if __name__ == "__main__":
    unittest.main()


- permite rularea direct din IDE
"""

import unittest


class Car():
    def __init__(self, colour, brand):
        self.colour = colour
        self.brand = brand       

Masina = Car("green", "audi")
z = 25
Masina2 = Car("neon green", "volvo")

class TestExample(unittest.TestCase):
    def test_include(self):
        self.assertNotIn("S", "SDAAcademy")

    def test_instanta(self):
        self.assertNotIsInstance(Masina2, Car, "This car doesn't exist!")

    def test_egalitate(self):
        result = 5 + 5
        self.assertEqual(result, 10)

    def test_verify_not_none(self):
        x = 10
        self.assertIsNotNone(x, "Facem SDA Academy if x is not none!")

    def test_adevarat(self):
        x = False
        self.assertTrue(x, "Daca nu e egal, te anunt eu")
 
    

# entry point
# aparent in PyCharm merge fara ?!
if __name__ == "__main__":
    unittest.main()

