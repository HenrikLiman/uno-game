import pygame
import os

from card import Card
from deck import Deck
from player import Player, Npc


class Board:
    def __init__(self, nr_of_bots, screen):

        self.player = [Player("Henrik")]
        for i in range(nr_of_bots):
            self.player.append(Npc(f"npc {i}"))
        self.deck = Deck(screen)

        self.screen = screen
        self.active_card = Card(1, 1, screen)

        self.player_turn = 0
        #        self.play_direction_revers = False  # True = Right, False = left
        self.running = True

    def run(self):
        clock = pygame.time.Clock()
        while self.running:
            base_font = pygame.font.Font(None, 32)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.button_input(mouse_x, mouse_y)

            self.screen.fill([0, 0, 0])
            text_surface = base_font.render(self.player[self.player_turn].player_name, False, (255, 255, 255))
            self.screen.blit(text_surface, (100, 100))
            self.draw()
            pygame.display.update()

            if self.uno_win():
                self.running = False
                print(f"Player nr: {self.player[self.player_turn-1].player_name} won")
        clock.tick(10)

    def draw(self):
        self.screen.blit(pygame.image.load(os.path.join("package_cards", "uDraw.jpg")), (800, 200))
        self.screen.blit(pygame.image.load(os.path.join("package_cards", "uUno.jpg")), (800, 130))
        # if not isinstance(self.player[self.player_turn], Npc):
        self.player[self.player_turn].draw()
        self.active_card.draw(300, 200)

    def next_player(self):

        if self.player_turn == len(self.player) - 1:
            self.player_turn = 0
        else:
            self.player_turn += 1

    def button_input(self, x, y):
        self.draw_card_button(x, y)
        self.uno_button(x, y)
        self.played_card(x, y)

    def uno_button(self, x, y, ):
        if 800 <= x <= 900 and 130 <= y <= 180:
            self.player[self.player_turn].has_uno()

    def draw_card_button(self, x, y):
        if 800 <= x <= 900 and 200 <= y <= 250:
            self.player[self.player_turn].draw_card(self.deck)
            self.next_player()

    def card_effect(self, chosen_effect):
        if chosen_effect == 10:  # block
            self.next_player()
        if chosen_effect == 11:  # draw2
            for i in range(2):
                if self.player_turn == len(self.player):
                    self.player[0].draw_card(self.deck)
                else:
                    self.player[self.player_turn].draw_card(self.deck)
        if chosen_effect == 12:  # revers
            self.reverse_order()
            self.next_player()
        if chosen_effect == 13:  # change color
            self.pick_a_color()

        if chosen_effect == 14:  # draw 4 and change color
            for i in range(4):
                if self.player_turn == len(self.player):
                    self.player[0].draw_card(self.deck)
                else:
                    self.player[self.player_turn].draw_card(self.deck)

            self.pick_a_color()

    def played_card(self, x, y):

        if isinstance(self.player[self.player_turn], Npc):
            selected_card = self.player[self.player_turn].play_card(self.active_card)
        else:
            selected_card = self.player[self.player_turn].play_card(x, y)

        if selected_card == 0:
            self.player[self.player_turn].draw_card(self.deck)
            self.next_player()
        if selected_card:

            if selected_card.color == self.active_card.color or selected_card.val == self.active_card.val or \
                    selected_card.color == 4 or self.active_card.color == 4:

                self.active_card = selected_card
                self.player[self.player_turn].remove_card(selected_card)
                self.next_player()
                if selected_card.val > 9:
                    self.card_effect(selected_card.val)

    def pick_a_color(self):
        running = True
        while running:
            pygame.draw.rect(self.screen, [255, 0, 0], (300, 200, 50, 80))
            pygame.draw.rect(self.screen, [0, 0, 255], (350, 200, 50, 80))
            pygame.draw.rect(self.screen, [255, 255, 0], (300, 280, 50, 80))
            pygame.draw.rect(self.screen, [0, 255, 0], (350, 280, 50, 80))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if not isinstance(self.player[self.player_turn-1], Npc):
                    if event.type == pygame.MOUSEBUTTONUP:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if 300 <= mouse_x <= 350 and 200 <= mouse_y <= 280:  # red
                            self.active_card = Card(0, self.active_card.val, self.screen)
                            running = False
                        if 350 <= mouse_x <= 400 and 200 <= mouse_y <= 280:  # blue
                            self.active_card = Card(2, self.active_card.val, self.screen)
                            running = False
                        if 300 <= mouse_x <= 350 and 280 <= mouse_y <= 360:  # yellow
                            self.active_card = Card(3, self.active_card.val, self.screen)
                            running = False
                        if 350 <= mouse_x <= 400 and 280 <= mouse_y <= 360:  # green
                            self.active_card = Card(1, self.active_card.val, self.screen)
                            running = False
                else:
                    self.active_card = Card(self.player[self.player_turn-1].npc_pick_color(), self.active_card.val,
                                            self.screen)
                    running = False

            pygame.display.update()

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
        self.player_turn = len(self.player) - self.player_turn - 1
        self.next_player()
