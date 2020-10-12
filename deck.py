from card import Card
import random


class Deck:
    def __init__(self, screen):
        self.cards = []
        self.screen = screen

    def deck_creator(self):

        for c in range(4):
            for i in range(13):
                self.cards.append(Card(c, i, self.screen))  # c is color with: 1 red, 2 green, 3 blue, 4 yellow
            for i in range(1, 13):
                self.cards.append(Card(c, i, self.screen))  # c is color with: 1 red, 2 green, 3 blue, 4 yellow
        for c in range(2):
            for i in range(4):
                self.cards.append((Card(4, 13+c, self.screen)))
        for c in self.cards:
            c.set_cards()
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) == 0:
            self.deck_creator()
        return self.cards.pop()

    def shuffle_deck(self):
        random.shuffle(self.cards)
