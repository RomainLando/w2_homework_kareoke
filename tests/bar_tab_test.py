import unittest

from classes.guest import Guest
from classes.bar_tab import BarTab

class TestBarTab(unittest.TestCase):
    def setUp(self):
        self.tab_1 = BarTab("Raquel")
    
    def test_tab_has_owner(self):
        self.assertEqual("Raquel", self.tab_1.guest_name)
    
    def test_tab_has_amount(self):
        self.assertEqual(0.00, self.tab_1.bill)
