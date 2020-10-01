import pygame
import os

from card import Card
from deck import Deck
from player import Player


class Board:
    def __init__(self, nr_of_players, screen):

        self.player = []
        for i in range(nr_of_players):
            self.player.append(Player(i))
        self.deck = Deck(screen)

        self.screen = screen
        self.active_card = Card(1, 1, screen)

        self.player_turn = 0
        self.running = True

    def draw(self):
        self.screen.blit(pygame.image.load(os.path.join("packege_cards", "uDraw.jpg")), (800, 200))
        self.screen.blit(pygame.image.load(os.path.join("packege_cards", "uUno.jpg")), (800, 130))
        self.player[self.player_turn].draw()
        self.active_card.draw(300, 200)

    def draw_card_button(self, x, y):
        if 800 <= x <= 900 and 200 <= y <= 250:
            self.player[self.player_turn].draw_card(self.deck)
            self.next_player()

    def next_player(self):
        if self.player_turn == len(self.player)-1:
            self.player_turn = 0
        else:
            self.player_turn += 1

    def uno_button(self, x, y, ):
        if 800 <= x <= 900 and 130 <= y <= 180:
            self.player[self.player_turn].has_uno()

    def played_card(self, x, y):
        selected_card = self.player[self.player_turn].play_card(x, y)

        if selected_card:
            if selected_card.color == self.active_card.color or selected_card.val == self.active_card.val:
                self.active_card = selected_card
                self.player[self.player_turn].remove_card(selected_card)
                self.next_player()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.draw_card_button(mouse_x, mouse_y)
                    self.uno_button(mouse_x, mouse_y)
                    self.played_card(mouse_x, mouse_y)

            self.screen.fill([0, 0, 0])

            self.draw()
            pygame.display.update()
            if self.uno_win():
                self.running = False
                print(f"Player nr: {self.player[self.player_turn].payer_name} won")

    def set_up(self):
        self.deck.deck_creator()
        self.active_card = self.deck.draw_card()
        for i in range(len(self.player)):
            self.player[i].set_up(self.deck)

    def uno_win(self):
        if self.player[self.player_turn-1].uno and len(self.player[self.player_turn-1].hand) == 0:
            return True
        return False
