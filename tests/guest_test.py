import unittest

from classes.guest import Guest
from classes.song import Song
from classes.room import Room


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest_1 = Guest("Raquel", 100, "...Baby one more time")
        self.guest_2 = Guest("Romain", 150, "Chop Suey!")

        self.room_2 = Room(2, 25.00)

        self.song1 = Song("...Baby one more time", "Britney Spears")
        self.song2 = Song("Chop Suey!", "System of a Down")
        self.song3 = Song("Thoughts and Prayers" , "Samm Henshaw")
        self.song4 = Song("Nothing Wrong With That", "Sahara Beck")

    
    def test_guest_has_name(self):
        self.assertEqual("Raquel", self.guest_1.name)

    def test_guest_has_money(self):
        self.assertEqual(100, self.guest_1.money)

    def test_guest_has_favourite_song(self):
        self.assertEqual("...Baby one more time", self.guest_1.favourite_song)

    def test_guest_favourite_song_not_in_room(self):
        self.room_2.add_song(self.song4)
        self.room_2.add_song(self.song3)
        self.assertEqual(None, self.guest_1.check_song(self.room_2))
    
    def test_decrease_money(self):
        self.guest_1.decrease_money(25.00)
        self.assertEqual(75.0, self.guest_1.money)
