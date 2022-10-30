import unittest

from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("...Baby one more time", "Britney Spears")
        self.song2 = Song("Chop Suey!", "System of a Down")
        self.song3 = Song("Thoughts and Prayers" , "Samm Henshaw")
        self.song4 = Song("Nothing Wrong With That", "Sahara Beck")


    def test_song_has_a_name(self):
        self.assertEqual("...Baby one more time", self.song1.name)


    def test_song_has_an_artist(self):
        self.assertEqual("Britney Spears", self.song1.artist)
    
