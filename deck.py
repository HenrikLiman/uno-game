from card import Card
import random


class Deck:
    def __init__(self, screen):
        self.cards = []
        self.screen = screen

    def deck_creator(self):
        for i in range(10):
            self.cards.append(Card(1, i, self.screen))#red
        for i in range(10):
            self.cards.append(Card(2, i, self.screen))#green
        for i in range(10):
            self.cards.append(Card(3, i, self.screen))#blue
        for i in range(10):
            self.cards.append(Card(4, i, self.screen)) #yellow
        for c in self.cards:
            c.set_cards()
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            self.deck_creator()
        return self.cards.pop()

    def shuffle_deck(self):
        random.shuffle(self.cards)
