from card import Card


class Deck:
    def __init__(self, screen):
        self.cards = []
        self.screen = screen

    def draw(self):
        for c in self.cards:
            c.draw()

    def shuffle_deck(self):
        self.cards.reverse()

    def deck_creator(self):
        for i in range(10):
            self.cards.append(Card([255, 0, 0], i, self.screen))
        for i in range(10):
            self.cards.append(Card([0, 255, 0], i, self.screen))
        for i in range(10):
            self.cards.append(Card([0, 0, 255], i, self.screen))
        for c in self.cards:
            c.set_cards()
    def get_pos(self, x, y):
        for c in self.cards:
            if c.get_x() <= x <= c.get_x() + 20 and c.get_y() <= y <= c.get_y() + 100:
                return c

    def draw_card(self):
        if len(self.cards) == 0:
            self.deck_creator()

        return self.cards.pop()
