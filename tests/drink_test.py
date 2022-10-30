import unittest

from classes.drink import Drink

class TestDrink(unittest.TestCase):
    
    def setUp(self):
        self.drink_1 = Drink("Rum and Coke", 6.0)
        self.drink_2 = Drink("Sprite", 3.00)
        self.drink_3 = Drink("Gin and Tonic", 7.50)

    def test_drink_has_name(self):
        self.assertEqual("Rum and Coke", self.drink_1.name)
    
    def test_drink_has_price(self):
        self.assertEqual(6.0, self.drink_1.price)