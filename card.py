import pygame
import os
from  packege_cards import *


class Card:
    def __init__(self, color, val, screen):
        self.color = color
        self.val = val
        self.screen = screen
        self.uno_card = pygame.image.load(os.path.join("packege_cards", f"ub{val}.jpg"))

    def draw(self, x, y):
        # pygame.draw.rect(self.screen, self.color, (x, y, 20, 100))
        self.screen.blit(self.uno_card, (x, y))

    def set_cards(self):
        if self.color == [0, 255, 0]:
            self.uno_card = pygame.image.load(os.path.join("packege_cards", "ug0.jpg"))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
