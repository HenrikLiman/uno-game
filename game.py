import pygame

from board import Board
from menu import Menu


def main():
    pygame.init()
    nr_of_bots = 3
    screen = pygame.display.set_mode((960, 540))

    menu = Menu(screen)
    if menu.menu_screen():
        board = Board(nr_of_bots, screen)
        board.set_up()
        board.run()


if __name__ == '__main__':
    main()
