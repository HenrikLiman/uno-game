class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_card(self, cards):
        self.hand.append(cards.draw_card())

    def draw(self):
        for i, cards in enumerate(self.hand):
            cards.draw(i * 30, 300)

    def play_card(self, x, y):
        for i, card in enumerate(self.hand):
            if i * 30 <= x <= i * 30 + 20 and 300 <= y <= 400:
                return card
