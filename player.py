import operator


class Player:
    def __init__(self, player_name):

        self.player_name = player_name
        self.hand = []
        self.uno = False

    def draw(self):
        for i, cards in enumerate(self.hand):
            cards.draw(30 + i * 30, 430)

    def print_hand(self):
        if self.uno:
            return "UNO!"
        else:
            return len(self.hand)

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())
        self.hand.sort(key=operator.attrgetter('val'))
        self.hand.sort(key=operator.attrgetter("color"))

        self.uno = False

    def play_card(self, x, y):
        if 30 + len(self.hand) * 30 <= x <= len(self.hand) * 30 + 100 and 430 <= y <= 590:
            return self.hand[-1]
        for i, card in enumerate(self.hand):
            if 30 + i * 30 <= x <= i * 30 + 60 and 430 <= y <= 590:
                return card

    def remove_card(self, card):
        for i, c in enumerate(self.hand):
            if c.val == card.val and c.color == card.color:
                self.hand.remove(self.hand[i])
                break

    def has_uno(self):
        if len(self.hand) == 2:
            self.uno = True

    def set_up(self, deck):
        for i in range(5):
            self.draw_card(deck)
