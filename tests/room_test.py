import unittest

from classes.drink import Drink
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    
    def setUp(self):
        self.room_1 = Room(10, 5.00)
        self.room_2 = Room(1, 25.00)

        self.guest_1 = Guest("Raquel", 100, "...Baby one more time")
        self.guest_2 = Guest("Romain", 150, "Chop Suey!")
        self.guest_3 = Guest("Richard", 4.95, "As")
        self.guest_4 = Guest("Romney", 25, "Mamma Mia")
        self.guest_5 = Guest("Rita", 30, "Gangsta's Paradise")


        self.song1 = Song("...Baby one more time", "Britney Spears")
        self.song2 = Song("Chop Suey!", "System of a Down")

        self.drink_1 = Drink("Rum and Coke", 6.0)
        self.drink_2 = Drink("Sprite", 3.00)
        self.drink_3 = Drink("Gin and Tonic", 7.50)

    def test_room_has_no_drinks(self):
        self.assertEqual(0, len(self.room_1.drinks))

    def test_room_has_drinks(self):
        self.room_1.add_drink(self.drink_1)
        self.assertEqual(1, len(self.room_1.drinks))

    def test_room_has_fee(self):
        self.assertEqual(5, self.room_1.fee)

    def test_room_has_bank(self):
        self.assertEqual(0, self.room_1.bank)
        
    def test_room_has_no_guests(self):
        self.assertEqual(0, len(self.room_1.guests))

    def test_room_has_no_bar_tab(self):
        self.assertIsNone(self.room_1.bar_tab)

    def test_room_has_no_songs(self):
        self.assertEqual(0, len(self.room_1.songs))
    
    def test_room_availability(self):
        self.assertEqual(10, self.room_1.availability)
    
    def test_add_guests_success(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_guest(self.guest_2)
        self.assertEqual(2, len(self.room_1.guests))
        self.assertEqual(8, self.room_1.availability)
        self.assertEqual(10.0, self.room_1.bank)
        self.assertEqual(95, self.guest_1.money)
        self.assertEqual(145, self.guest_2.money)
    
    def test_add_guest_no_availability(self):
        self.room_2.add_guest(self.guest_1)
        self.room_2.add_guest(self.guest_2)
        self.assertEqual(1, len(self.room_2.guests))
        self.assertEqual(0, self.room_2.availability)

    def test_songs_added(self):
        self.room_1.add_song(self.song1)
        self.room_1.add_song(self.song2)
        self.assertEqual(2, len(self.room_1.songs))

    def test_songs_added_twice(self):
        self.room_1.add_song(self.song1)
        self.room_1.add_song(self.song1)
        self.assertEqual(1, len(self.room_1.songs))

    def test_room_has_no_tab(self):
        self.assertIsNone(self.room_1.bar_tab)

    def test_room_has_a_tab(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.start_tab(self.guest_1)
        self.assertEqual(self.guest_1.name, self.room_1.bar_tab.guest_name)

    def test_can_not_start_tab_guest_not_in_room(self):
        self.room_1.start_tab(self.guest_1)
        self.assertIsNone(self.room_1.bar_tab)
    
    def test_guest_added_to_room_with_favourite_song(self):
        self.room_2.add_song(self.song1)
        self.assertEqual("Whoo!", self.room_2.add_guest(self.guest_1))
    
    def test_increase_bank_amount(self):
        self.room_1.increase_bank(25.0)
        self.assertEqual(25.0, self.room_1.bank)
    
    def test_guest_can_not_afford_room(self):
        self.room_1.add_guest(self.guest_3)
        self.assertEqual(10, self.room_1.availability)
        self.assertEqual(0, len(self.room_1.guests))
    
    def test_find_drink(self):
        self.room_1.add_drink(self.drink_1)
        self.assertEqual(self.drink_1, self.room_1.find_drink("Rum and Coke"))

    def test_drink_sold_to_guest(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_drink(self.drink_1)
        self.room_1.sell_drink(self.guest_1, self.drink_1.name)
        self.assertEqual(89.0, self.guest_1.money)
        self.assertEqual(11.0, self.room_1.bank)

    def test_drink_not_sold_guest_not_in_room(self):
        self.room_1.add_drink(self.drink_1)
        self.room_1.sell_drink(self.guest_1, self.drink_1.name)
        self.assertEqual(100.0, self.guest_1.money)
        self.assertEqual(0.0, self.room_1.bank)

    def test_drink_not_sold_drinnk_not_found(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_drink(self.drink_2)
        self.room_1.sell_drink(self.guest_1, self.drink_1.name)
        self.assertEqual(95.0, self.guest_1.money)
        self.assertEqual(5.0, self.room_1.bank)

    def test_room_cannot_have_another_tab(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_guest(self.guest_2)
        self.room_1.start_tab(self.guest_1)
        self.room_1.start_tab(self.guest_2)
        self.assertEqual("Raquel", self.room_1.bar_tab.guest_name)

    def test_increase_bar_tab_successful(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.start_tab(self.guest_1)
        self.room_1.increase_tab(25)
        self.assertEqual(25, self.room_1.bar_tab.bill)

    def test_increase_bar_tab_no_bar_tab(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.increase_tab(25)
        self.assertIsNone(self.room_1.bar_tab)

    def test_drink_fee_placed_on_tab(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_guest(self.guest_2)
        self.room_1.start_tab(self.guest_1)
        self.room_1.add_drink(self.drink_1)
        self.room_1.add_drink(self.drink_2)
        self.room_1.sell_drink(self.guest_1, self.drink_1.name)
        self.room_1.sell_drink(self.guest_2, self.drink_2.name) 
        self.assertEqual(10, self.room_1.bank)
        self.assertEqual(9, self.room_1.bar_tab.bill) 
        self.assertEqual(95, self.guest_1.money)
        self.assertEqual(145, self.guest_2.money)

    def test_pay_off_bar_tab_successfully(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_guest(self.guest_2)
        self.room_1.add_guest(self.guest_4)
        self.room_1.add_guest(self.guest_5)
        self.room_1.start_tab(self.guest_1)
        self.room_1.increase_tab(200)
        self.room_1.settle_tab()
        self.assertEqual(0, self.room_1.bar_tab.bill)

    def test_cannot_pay_tab(self):
        self.room_1.add_guest(self.guest_1)
        self.room_1.add_guest(self.guest_2)
        self.room_1.add_guest(self.guest_4)
        self.room_1.add_guest(self.guest_5)
        self.room_1.start_tab(self.guest_1)
        self.room_1.increase_tab(500)
        self.assertEqual("Oh oh..." ,self.room_1.settle_tab())
