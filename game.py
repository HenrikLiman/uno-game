import pygame

from board import Board


def main():
    nr_of_players = 2
    screen = pygame.display.set_mode((1000, 800))
    board = Board(nr_of_players, screen)
    board.set_up()
    board.run()

if __name__ == '__main__':
    main()
