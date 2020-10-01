from card import Card
import random


class Deck:
    def __init__(self, screen):
        self.cards = []
        self.screen = screen

    def deck_creator(self):
        for i in range(10):
            self.cards.append(Card([255, 0, 0], i, self.screen))
        for i in range(10):
            self.cards.append(Card([0, 255, 0], i, self.screen))
        for i in range(10):
            self.cards.append(Card([0, 0, 255], i, self.screen))
        for i in range(10):
            self.cards.append(Card([255, 255, 0], i, self.screen))
        for c in self.cards:
            c.set_cards()
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            self.deck_creator()

        return self.cards.pop()

    def shuffle_deck(self):
        random.shuffle(self.cards)
