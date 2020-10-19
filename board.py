import pygame
import os
import random

from Settings import *
from card import Card
from deck import Deck
from npc import Npc
from player import Player


class Board:
    def __init__(self, nr_of_bots, player, screen):

        self.player = [Player(player)]
        for i in range(nr_of_bots):
            self.player.append(Npc(random.choice(NAMES)))
        self.deck = Deck(screen)

        self.screen = screen
        self.active_card = Card(1, 1, screen)

        self.player_turn = random.randrange(0, nr_of_bots)
        self.running = True
        self.real_player = 0


    def run(self):
        clock = pygame.time.Clock()

        while self.running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.button_input(mouse_x, mouse_y)

            self.screen.fill([0, 0, 0])
            self.screen.blit(pygame.image.load(os.path.join("package_cards", "play_area.jpg")), (0, 0))

            self.draw()
            pygame.display.update()

            if self.uno_win():
                self.running = False
                self.end_screen_card_rain()
            clock.tick(10)

    def end_screen_card_rain(self):

        clock = pygame.time.Clock()
        running = True
        fall_x = []
        fall_y = 0
        fall_x.append(0)
        base_font = pygame.font.Font(None, 32)

        for i in range(12):
            fall_x.append(i * 80)

        while running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    running = False
            for i, x in enumerate(fall_x):
                self.deck.cards[i + random.randrange(0, 9)].draw(x, fall_y)
            text_surface = base_font.render(f"{self.player[self.player_turn - 1].player_name} won this time", False,
                                            (255, 255, 255))
            pygame.draw.rect(self.screen,(0,0,0),(SCREEN_WIDTH/2-350/2, SCREEN_HEIGHT/2-50, 350, 100))
            self.screen.blit(text_surface, (SCREEN_WIDTH/2-350/2+5, 240))
            self.screen.blit(base_font.render("click anywhere to play again", False, (255, 255, 255)),
                             (SCREEN_WIDTH / 2 - 350 / 2 + 5,  240 + 32))

            pygame.display.update()

            fall_y += 120
            if fall_y > SCREEN_HEIGHT:
                fall_y = 0
            clock.tick(2)

    def draw(self):
        self.screen.blit(pygame.image.load(os.path.join("package_cards", "uDraw.jpg")), (DRAW_BUTTON_X, DRAW_BUTTON_Y))
        self.screen.blit(pygame.image.load(os.path.join("package_cards", "uUno.jpg")), (UNO_BUTTON_X, UNO_BUTTON_Y))
        if not isinstance(self.player[self.player_turn], Npc):
            self.player[self.player_turn].draw()
            self.real_player = self.player_turn
        else:
            for p in self.player:
                if not isinstance(p, Npc):
                    p.draw()
                    break
        self.active_card.draw(CARDAREA_X, CARDAREA_y)
        self.name_player()

    def name_player(self):
        base_font = pygame.font.Font(None, 32)
        for i, p in enumerate(self.player):
            if i == self.player_turn:
                name_color = (0, 255, 0)

            else:
                name_color = (255, 255, 255)
            text_surface = base_font.render(f"{p.player_name} : {p.print_hand()}", False, name_color)
            self.screen.blit(text_surface, (675, 50 + 30 * i))

    def next_player(self):

        if self.player_turn == len(self.player) - 1:
            self.player_turn = 0
        else:
            self.player_turn += 1

    def button_input(self, x, y):
        self.played_card(x, y)
        self.draw_card_button(x, y)
        self.uno_button(x, y)

    def uno_button(self, x, y, ):
        if UNO_BUTTON_X <= x <= UNO_BUTTON_X + 100 and UNO_BUTTON_Y <= y <= UNO_BUTTON_Y + 50:
            self.player[self.player_turn].has_uno()

    def draw_card_button(self, x, y):
        if DRAW_BUTTON_X <= x <= DRAW_BUTTON_X + 100 and DRAW_BUTTON_Y <= y <= DRAW_BUTTON_Y + 50 and \
                not isinstance(self.player[self.player_turn], Npc):
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
            pygame.draw.rect(self.screen, [255, 0, 0], (CARDAREA_X, CARDAREA_y, 50, 80))
            pygame.draw.rect(self.screen, [0, 0, 255], (CARDAREA_X + 50, CARDAREA_y, 50, 80))
            pygame.draw.rect(self.screen, [255, 255, 0], (CARDAREA_X, CARDAREA_y + 80, 50, 80))
            pygame.draw.rect(self.screen, [0, 255, 0], (CARDAREA_X + 50, CARDAREA_y + 80, 50, 80))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if not isinstance(self.player[self.player_turn - 1], Npc):
                    if event.type == pygame.MOUSEBUTTONUP:
                        mouse_x, mouse_y = pygame.mouse.get_pos()
                        if CARDAREA_X <= mouse_x <= CARDAREA_X + 50 and \
                                CARDAREA_y <= mouse_y <= CARDAREA_y + 80:  # red
                            self.active_card = Card(0, self.active_card.val, self.screen)
                            running = False
                        if CARDAREA_X + 50 <= mouse_x <= CARDAREA_X + 100 and \
                                CARDAREA_y <= mouse_y <= CARDAREA_y + 80:  # blue
                            self.active_card = Card(2, self.active_card.val, self.screen)
                            running = False
                        if CARDAREA_X <= mouse_x <= CARDAREA_X + 50 and \
                                CARDAREA_y + 80 <= mouse_y <= CARDAREA_y + 160:  # yellow
                            self.active_card = Card(3, self.active_card.val, self.screen)
                            running = False
                        if CARDAREA_X + 50 <= mouse_x <= CARDAREA_X + 100 and \
                                CARDAREA_y + 80 <= mouse_y <= CARDAREA_y + 160:  # green
                            self.active_card = Card(1, self.active_card.val, self.screen)
                            running = False
                else:
                    self.active_card = Card(self.player[self.player_turn - 1].npc_pick_color(),
                                            self.active_card.val, self.screen)
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
