import pygame

from board import Board
from menu import Menu


def main():
    nr_of_players = 4
    screen = pygame.display.set_mode((960, 540))
    menu = Menu(screen)
    if menu.menu_screen():
        board = Board(nr_of_players, screen)
        board.set_up()
        board.run()


if __name__ == '__main__':
    main()
