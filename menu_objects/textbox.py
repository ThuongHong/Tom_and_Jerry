import pygame
from constants.INTERFACE_CONSTANTS import DISPLAY
from constants.INTERFACE_CONSTANTS import COLOR

class TextBox:
    def __init__(self, x_coord, y_coord, length, width, sound):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.length = length
        self.width = width
        self.sound = sound
        self.rect = pygame.Rect(self.x_coord, self.y_coord, self.length, self.width)
        self.text = ""
        self.font = pygame.font.SysFont('The fountain of wishes', 40)

    def draw(self, surface, color): 
        pygame.draw.rect(surface, color, self.rect)

    def draw_text(self, surface, text_color, censored):
        if censored:
            text = self.font.render("*" * len(self.text), True, text_color)
        else:
            text = self.font.render(self.text, True, text_color)
        surface.blit(text, (self.x_coord + 10, self.y_coord + 10))

    def get_text(self, surface, censored = False):
        pos = pygame.mouse.get_pos()
        activated = False
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            activated = True

        while activated:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit() 
                if event.type == pygame.KEYDOWN: 
                    if len(self.text) > 0 and event.key == pygame.K_BACKSPACE: 
                        self.text = self.text[:-1] 
                    elif event.key == pygame.K_RETURN:
                        activated = False
                    elif len(self.text) < DISPLAY.TEXT_LENGTH:
                        self.text += event.unicode

            TextBox.draw(self, surface, COLOR.WHITE)
            TextBox.draw_text(self, surface, COLOR.BLACK, censored)

            pygame.display.update()

