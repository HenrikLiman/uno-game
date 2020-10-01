import operator


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.uno = False

    def draw_card(self, top_card):
        self.hand.append(top_card.draw_card())
        self.hand.sort(key=operator.attrgetter('val'))
        self.hand.sort(key=operator.attrgetter("color"))

    def draw(self):
        for i, cards in enumerate(self.hand):
            cards.draw(30 + i * 30, 600)

    def play_card(self, x, y):
        if 30 + len(self.hand) * 30 <= x <= len(self.hand) * 30 + 100 and 600 <= y <= 760:
            return self.hand[-1]
        for i, card in enumerate(self.hand):
            if 30 + i * 30 <= x <= i * 30 + 60 and 600 <= y <= 760:
                return card

    def remove_card(self, card):
        for i, c in enumerate(self.hand):
            if c.val == card.val and c.color == card.color:
                print(card.val, card.color, i)
                self.hand.remove(self.hand[i])
                break

    def has_uno(self):
        if len(self.hand) == 1:
            self.uno = True