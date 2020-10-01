import pygame
import os


class Card:
    def __init__(self, color, val, screen):
        self.color = color
        self.val = val
        self.screen = screen
        self.uno_card = pygame.image.load(os.path.join("packege_cards", f"ub{self.val}.jpg"))

    def draw(self, x, y):
        self.screen.blit(self.uno_card, (x, y))

    def set_cards(self):
        if self.color == 1:
            self.uno_card = pygame.image.load(os.path.join("packege_cards", f"ur{self.val}.jpg"))
        if self.color == 2:
            self.uno_card = pygame.image.load(os.path.join("packege_cards", f"ug{self.val}.jpg"))
        if self.color == 4:
            self.uno_card = pygame.image.load(os.path.join("packege_cards", f"uy{self.val}.jpg"))


