import pygame

from board import Board


def main():
    nr_of_players = 3
    screen = pygame.display.set_mode((1000, 800))
    board = Board(nr_of_players, screen)
    running = True
    board.set_up()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                board.draw_card_button(mouse_x, mouse_y)
                board.uno_button(mouse_x, mouse_y)
                board.played_card(mouse_x, mouse_y)

        screen.fill([0, 0, 0])

        board.draw()
        pygame.display.update()
        if board.UnoWin():
            running == False


if __name__ == '__main__':
    main()
