import pygame
import os

from card import Card
from deck import Deck
from player import Player


class Board:
    def __init__(self, player, screen):
        self.player = Player(player)
        self.deck = Deck(screen)

        self.screen = screen
        self.active_card = self.deck.draw_card()

    def draw(self):
        self.screen.blit(pygame.image.load(os.path.join("packege_cards", "uDraw.jpg")), (800, 200))
        self.screen.blit(pygame.image.load(os.path.join("packege_cards", "uUno.jpg")), (800, 130))
        self.player.draw()
        self.active_card.draw(450, 200)

    def draw_card_button(self, x, y):
        if 800 <= x <= 900 and 200 <= y <= 250:
            self.player.draw_card(self.deck)

    def uno_button(self, x, y):
        if 800 <= x <= 900 and 130 <= y <= 180:
            self.player.has_uno()

    def played_card(self, x, y):
        selected_card = self.player.play_card(x, y)

        if selected_card:
            print(selected_card.val, selected_card.color)
            if selected_card.color == self.active_card.color or selected_card.val == self.active_card.val:
                self.active_card = selected_card
                self.player.remove_card(selected_card)

    def run(self):
        pass
