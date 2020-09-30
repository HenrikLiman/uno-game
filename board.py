import pygame

from card import Card
from deck import Deck
from player import Player


class Board:
    def __init__(self, player1, player2, screen):
        self.player1 = Player(player1)
        self.player2 = Player(player2)
        self.deck = Deck(screen)

        self.screen = screen
        self.active_card = self.deck.draw_card()

    def draw(self):
        pygame.draw.rect(self.screen, [255, 255, 255], (800, 400, 50, 50))
        self.player1.draw()
        self.active_card.draw(100, 100)

    def draw_card_button(self, x, y):
        if 800 <= x <= 850 and 400 <= y <= 450:
            self.player1.draw_card(self.deck)

    def played_card(self, x, y):
        selected_card = self.player1.play_card(x, y)

        if selected_card:
            print(selected_card.val, selected_card.color)
            if selected_card.color == self.active_card.color or selected_card.val == self.active_card.val:
                self.active_card = self.player1.play_card(x, y)

    def run(self):
        pass
