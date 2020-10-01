import pygame
import os

from board import Board


class Menu:
    def __init__(self, screen):
        self.screen = screen

    def menu_screen(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    self.start_game(mouse_x, mouse_y)
                    self.exit_game(mouse_x, mouse_y)
                    print(mouse_x, mouse_y)

            self.screen.blit(pygame.image.load(os.path.join("packege_cards", "UnoScreenText.jpg")), (0, 0))
            pygame.display.update()

    def start_game(self, x, y):
        if 0 <= x <= 255 and 200 <= y <= 255:
            print("hej")

    def exit_game(self, x, y):
        if 0 <= x <= 255 and 275 <= y <= 315:
            print("exit")


def main():
    nr_of_players = 2
    screen = pygame.display.set_mode((960, 540))
    menu = Menu(screen)
    menu.menu_screen()
    board = Board(nr_of_players, screen)
    board.set_up()
    board.run()


if __name__ == '__main__':
    main()
