import pygame
import os

pygame.init()


class Menu:
    def __init__(self, screen):
        self.screen = screen
        self.player = []
        self.user_text = ""
        self.input_rect = pygame.Rect(200, 200, 140, 32)

    def menu_screen(self):
        base_font = pygame.font.Font(None, 32)


        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                if event.type == pygame.MOUSEBUTTONUP:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.start_game(mouse_x, mouse_y):
                        return True
                    if self.exit_game(mouse_x, mouse_y):
                        return False
                self.player_input(event)
            self.screen.blit(pygame.image.load(os.path.join("packege_cards", "UnoScreenText.jpg")), (0, 0))
            pygame.draw.rect(self.screen,(0,0,0),self.input_rect)
            text_surface = base_font.render(self.user_text, False, (255, 255, 255))
            self.screen.blit(text_surface, (205, 205))
            pygame.display.update()

    def player_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_text = self.user_text[0:-1]
            else:
                self.user_text += event.unicode

    def start_game(self, x, y):
        if 0 <= x <= 255 and 200 <= y <= 255:
            return True

    def exit_game(self, x, y):
        if 0 <= x <= 255 and 275 <= y <= 315:
            return True
