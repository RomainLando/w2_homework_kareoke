from classes.song import Song
from classes.guest import Guest
from classes.bar_tab import BarTab

class Room:
    def __init__(self, availability, fee):
        self.availability = availability
        self.guests = set()
        self.bar_tab = None
        self.songs = set()
        self.drinks = set()
        self.fee = fee
        self.bank = 0.00

    def add_drink(self, drink):
        self.drinks.add(drink)

    def add_guest(self, guest):
        if self.availability > 0 and guest.money >= self.fee:
            self.guests.add(guest)
            self.availability -= 1
            self.increase_bank(self.fee)
            guest.decrease_money(self.fee)
            return guest.check_song(self)
    
    def add_song(self, song):
        self.songs.add(song)

    def start_tab(self, guest):
        if not self.bar_tab and guest in self.guests:
            self.bar_tab = BarTab(guest.name)

    def increase_bank(self, amount):
        self.bank += amount
    
    def increase_tab(self, amount):
        if self.bar_tab:
            self.bar_tab.bill += amount

    def find_drink(self, drink_name):
        for drink in self.drinks:
            if drink.name == drink_name:
                return drink
    
    def sell_drink(self, guest, drink_name):
        found_drink = self.find_drink(drink_name)
        if guest in self.guests and found_drink:
            if self.bar_tab:
                self.increase_tab(found_drink.price)
            else:
                self.increase_bank(found_drink.price)
                guest.decrease_money(found_drink.price)
    
    def total_guest_money():
        pass

    def settle_tab(self):
        if self.bar_tab:
            total_guest_money = 0
            for guest in self.guests:
                total_guest_money += guest.money
            if total_guest_money >= self.bar_tab.bill:
                while self.bar_tab.bill > 0:
                    guests_to_pay = [ guest for guest in self.guests if guest.money > 0]
                    individual_fee = self.bar_tab.bill / len(guests_to_pay)
                    for guest in guests_to_pay:
                        if guest.money >= individual_fee:
                            guest.decrease_money(individual_fee)
                            self.bar_tab.bill -= individual_fee
                        else:
                            self.bar_tab.bill -= guest.money
                            guest.decrease_money(guest.money)
            else:
                return "Oh oh..."
