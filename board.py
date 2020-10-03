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
        self.play_direction_revers = False  # True = Right, False = left
        self.running = True

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.button_input(mouse_x, mouse_y)

            self.screen.fill([0, 0, 0])

            self.draw()
            pygame.display.update()
            if self.uno_win():
                self.running = False
                print(f"Player nr: {self.player[self.player_turn].payer_name} won")

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
        if not self.play_direction_revers:
            if self.player_turn == len(self.player) - 1:
                self.player_turn = 0
            else:
                self.player_turn += 1
        else:
            if self.player_turn == len(self.player):
                self.player_turn = len(self.player)
            else:
                self.player_turn -= 1

    def button_input(self, x, y):
        self.draw_card_button(x, y)
        self.uno_button(x, y)
        self.played_card(x, y)

    def uno_button(self, x, y, ):
        if 800 <= x <= 900 and 130 <= y <= 180:
            self.player[self.player_turn].has_uno()

    def card_effect(self, chosen_effect):
        if chosen_effect == 10:  # block
            self.next_player()
        if chosen_effect == 11:  # draw2
            for i in range(2):
                self.player[self.player_turn].draw_card(self.deck)
        if chosen_effect == 12:  # revers
            self.reverse_order()
            self.next_player()
        if chosen_effect == 13:  # change color
            while True:
                self.pick_a_color


                print("...")
        if chosen_effect == 14:  # draw 4 and change color
            for i in range(4):
                self.player[self.player_turn].draw_card(self.deck)

    def pick_a_color(self):
        pygame.draw.rect(self.screen, [255, 0, 0], (100, 50, 50, 50))
        pygame.draw.rect(self.screen, [0, 0, 255], (100, 100, 50, 50))
        pygame.draw.rect(self.screen, [255, 255, 0], (100, 150, 50, 50))
        pygame.draw.rect(self.screen, [0, 255, 0], (100, 200, 50, 50))
        pygame.display.update()

    def played_card(self, x, y):

        selected_card = self.player[self.player_turn].play_card(x, y)

        if selected_card:
            if selected_card.color == self.active_card.color or selected_card.val == self.active_card.val or selected_card.color == 4:
                self.active_card = selected_card
                self.player[self.player_turn].remove_card(selected_card)
                self.next_player()
                if selected_card.val > 9:
                    self.card_effect(selected_card.val)

    def set_up(self):
        self.deck.deck_creator()
        self.active_card = self.deck.draw_card()
        for i in range(len(self.player)):
            self.player[i].set_up(self.deck)

    def uno_win(self):
        if self.player[self.player_turn - 1].uno and len(self.player[self.player_turn - 1].hand) == 0:
            return True
        return False

    def reverse_order(self):
        self.player.reverse()
        self.player_turn = len(self.player) - self.player_turn
