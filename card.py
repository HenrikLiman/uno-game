import pygame
import os


class Card:
    def __init__(self, color, val, screen):
        self.color = color
        self.val = val
        self.screen = screen
        self.uno_card = pygame.image.load(os.path.join("packege_cards", f"ub{self.val}.jpg"))

    def draw(self, x, y):
        # pygame.draw.rect(self.screen, self.color, (x, y, 20, 100))
        self.screen.blit(self.uno_card, (x, y))

    def set_cards(self):
        if self.color == [255, 0, 0]:
            self.uno_card = pygame.image.load(os.path.join("packege_cards", f"ur{self.val}.jpg"))
        if self.color == [0, 255, 0]:
            self.uno_card = pygame.image.load(os.path.join("packege_cards", f"ug{self.val}.jpg"))
        if self.color == [255, 255, 0]:
            self.uno_card = pygame.image.load(os.path.join("packege_cards", f"uy{self.val}.jpg"))


