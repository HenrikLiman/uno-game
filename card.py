import pygame


class Card:
    def __init__(self, color, val, screen):
        self.color = color
        self.val = val
        self.screen = screen

    def draw(self, x, y):
        pygame.draw.rect(self.screen, self.color, (x, y, 20, 100))

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y
