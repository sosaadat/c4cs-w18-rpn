import unittest

import rpn

class TestBasics(unittest.TestCase):
    def test_add(self):
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
    def test_subtract(self):
        result = rpn.calculate("5 3 -")
        self.assertEqual(2, result)
    def test_multiply(self):
        result = rpn.calculate("5 3 *")
        self.assertEqual(15, result)
    def test_divide(self):
        result = rpn.calculate("6 3 /")
        self.assertEqual(2, result)
#Testing carrat
    def test_carrat1(self):
        result = rpn.calculate("1 1 ^")
        self.assertEqual(1, result)
    def test_carrat2(self):
        result = rpn.calculate("4 0 ^")
        self.assertEqual(1, result)
    def test_carrat3(self):
        result = rpn.calculate("2 3 ^")
        self.assertEqual(8, result)
    def test_carrat4(self):
        result = rpn.calculate("0 1 ^")
        self.assertEqual(0, result)



