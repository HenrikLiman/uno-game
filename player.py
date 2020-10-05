import operator


class Player:
    def __init__(self, player_name):

        self.player_name = player_name
        self.hand = []
        self.uno = False

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())
        self.hand.sort(key=operator.attrgetter('val'))
        self.hand.sort(key=operator.attrgetter("color"))

        self.uno = False

    def draw(self):
        for i, cards in enumerate(self.hand):
            cards.draw(30 + i * 30, 430)

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


class Npc(Player):
    def __init__(self, player_name):
        super().__init__(player_name)

    def npc_turn(self, active_card):
        self.has_uno()
        self.play_card(active_card)

    def play_card(self, active_card):
        for c in self.hand:
            if c.color == active_card.color or c.val == active_card.val:
                self.has_uno()
                print(f"{c.colors[c.color]} {c.val}")
                return c
        for c in self.hand:
            if c.color == 4:
                self.has_uno()
                print(f"{c.colors[c.color]} {c.val}")
                return c
        print("draw")
        return False

    def draw_card(self, deck):
        self.hand.append(deck.draw_card())
        self.uno = False

    def npc_pick_color(self):
        hand_colors = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0}
        largest_amount = 0
        largest_key = 0
        for cards in self.hand:
            hand_colors[cards.color] += 1
        for i in hand_colors:
            if i == 4:
                largest_amount = largest_amount
            else:
                if largest_amount < hand_colors[i]:
                    largest_key = i
                    largest_amount = hand_colors[i]
        return largest_key

