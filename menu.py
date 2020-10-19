import pygame
import os
from Settings import *


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.player = ""
        self.user_text = ""
        self.input_rect = pygame.Rect(NAME_INPUT_X, NAME_INPUT_Y, 140, 32)
        self.input_nr_of_players = ""
        self.nr_of_npc = 0

        self.input_npc = False
        self.name_the_player = False
        self.running = True

        self.play_game = True

        self.image = pygame.image.load(os.path.join("package_cards", "input.png"))

    def menu_screen(self):
        self.input_npc = False
        self.name_the_player = False
        self.nr_of_npc = 0
        self.image = pygame.image.load(os.path.join("package_cards", "input.png"))
        clock = pygame.time.Clock()
        base_font = pygame.font.Font(None, 32)
        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    self.play_game = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.start_game(mouse_x, mouse_y)
                    self.exit_game(mouse_x, mouse_y)

                    if self.input_npc:
                        self.nr_of_players(mouse_x, mouse_y)
                if event.type == pygame.KEYDOWN and self.name_the_player:
                    self.player_input(event)

            self.screen.blit(pygame.image.load(os.path.join("package_cards", "UnoScreenText.jpg")), (0, 0))
            if self.name_the_player:
                self.screen.blit(self.image, (0, 0))
            if self.name_the_player and not self.input_npc:
                text_surface = base_font.render(self.user_text, False, (255, 255, 255))
                self.screen.blit(text_surface, (NAME_INPUT_X, NAME_INPUT_Y + 5))

            pygame.display.update()

            clock.tick(10)
        if self.nr_of_npc == 0:
            self.play_game = False
        else:
            self.play_game = True

    def player_input(self, event):
        if event.key == pygame.K_BACKSPACE:
            self.user_text = self.user_text[0:-1]
        elif event.key == pygame.K_RETURN:
            self.player = self.user_text
            self.input_npc = True
            self.user_text = ""
            self.image = pygame.image.load(os.path.join("package_cards", "input2.png"))

        else:
            self.user_text += event.unicode

    def nr_of_players(self, x, y):
        for i in range(3):
            for j in range(5):
                if 305 + j * 100 <= x <= 360 + j * 100 and 220 + 60 * i <= y <= 270 + 60 * i:
                    self.nr_of_npc = i * 4 + j + 1
        if self.nr_of_npc > 0:
            self.running = False

    def start_game(self, x, y):
        if 0 <= x <= 255 and 200 <= y <= 255:
            self.name_the_player = True

    def exit_game(self, x, y):
        if 0 <= x <= 255 and 275 <= y <= 315:
            self.running = False
