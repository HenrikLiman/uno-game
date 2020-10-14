import pygame

from Settings import *
from board import Board
from menu import Menu


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    menu = Menu(screen)
    menu.menu_screen()
    while menu.play_game:
        board = Board(menu.nr_of_npc, menu.player, screen)
        board.set_up()
        board.run()
        menu.menu_screen()


if __name__ == '__main__':
    main()
