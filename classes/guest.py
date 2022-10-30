

class Guest:
    def __init__(self, name, money, favourite_song):
        self.name = name
        self.money = money
        self.favourite_song = favourite_song
        self.bar_tab = None
    
    def __str__(self):
        return f"guest.{self.name}"

    def check_song(self, room):
        for song in room.songs:
            if self.favourite_song in song.name:
                return "Whoo!"

    def decrease_money(self, amount):
        self.money -= amount
        