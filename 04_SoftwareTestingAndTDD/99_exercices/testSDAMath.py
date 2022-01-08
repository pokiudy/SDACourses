from SDAMath.functii import *

import unittest

print(add(23, 34))
print(divide(23, 12))

import unittest

class TestSDAMath(unittest.TestCase):
    def test_add(self):
        result = add(23, 34)
        self.assertEqual(result, 57)

    def test_divide(self):
        result = divide(45, 12)
        self.assertEqual(result, 45)

    def test_multiply(self):
        result = multiply(2, 3)
        self.assertEqual(result, 6)

    def test_substract(self):
        result = substract(4, 2)
        self.assertEqual(result, 2)

    def test_substracterror(self):
        result = substract(4, 3)
        self.assertNotEqual(result, 1)




if __name__ == "__main__":
    unittest.main()







