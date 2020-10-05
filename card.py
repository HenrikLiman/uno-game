import pygame
import os


class Card:
    def __init__(self, color, val, screen):
        self.color = color
        self.val = val
        self.screen = screen
        self.colors = ["r", "g", "b", "y", "w"]
        self.uno_card = pygame.image.load(os.path.join("package_cards", f"u{self.colors[color]}n.jpg"))

    def draw(self, x, y):
        self.screen.blit(self.uno_card, (x, y))

    def set_cards(self):

        for i, c in enumerate(self.colors):
            if self.color == i:
                if self.val == 10:  # stop next players turn
                    self.uno_card = pygame.image.load(os.path.join("package_cards", f"u{c}s.jpg"))
                elif self.val == 11:  # next player draws 2
                    self.uno_card = pygame.image.load(os.path.join("package_cards", f"u{c}d.jpg"))
                elif self.val == 12:  # revers play order
                    self.uno_card = pygame.image.load(os.path.join("package_cards", f"u{c}r.jpg"))
                elif self.val == 13:
                    self.uno_card = pygame.image.load(os.path.join("package_cards", f"u{c}c.jpg"))
                elif self.val == 14:
                    self.uno_card = pygame.image.load(os.path.join("package_cards", f"u{c}d.jpg"))

                else:
                    self.uno_card = pygame.image.load(os.path.join("package_cards", f"u{c}{self.val}.jpg"))


