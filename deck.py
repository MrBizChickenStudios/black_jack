import random

class Card():
    def __init__(self, face, vaule, suite):
        self.face = face
        self.vaule = vaule
        self.suite = suite

    def get_card(self):
        return f"card face {self.face} card vaule {self.vaule} card suite {self.suite}"

class Deck():
    def __init__(self):
        self.deck = []
        self.faces = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
        self.vaules = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.suites = ["Diamond", "Spade", "Club", "Heart"]
    def make_deck(self):
        for face in range(len(self.faces)):
            for suite in self.suites:

                self.deck.append(Card(self.faces[face], self.vaules[face], suite))



    def shuffle_deck(self):
        random.shuffle(self.deck)


    def deal_cards(self, hand, number_of_cards):
        for card in range(number_of_cards):
            hand.append(self.deck[0])
            self.deck.pop(0)
