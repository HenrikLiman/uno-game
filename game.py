import pygame

from board import Board


def main():
    screen = pygame.display.set_mode((1000, 800))
    board = Board("hej", screen)
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                print(mouse_x, mouse_y)
                board.draw_card_button(mouse_x, mouse_y)
                board.played_card(mouse_x, mouse_y)

        screen.fill([0, 0, 0])
        board.draw()
        pygame.display.update()


if __name__ == '__main__':
    main()
