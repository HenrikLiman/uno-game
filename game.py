import pygame

from Settings import *
from board import Board
from menu import Menu

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    menu = Menu(screen)
    if menu.menu_screen():
        board = Board(menu.nr_of_npc, menu.player, screen)
        board.set_up()
        board.run()


if __name__ == '__main__':
    main()
