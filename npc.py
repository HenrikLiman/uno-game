from player import Player


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
                return c
        for c in self.hand:
            if c.color == 4:
                self.has_uno()
                return c
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

