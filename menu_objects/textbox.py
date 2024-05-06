import pygame
import time
from CONSTANTS import DISPLAY
from CONSTANTS import COLOR

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

    def draw_cursor(self, surface, cursor_color, censored):
        if censored:
            text = self.font.render("*" * len(self.text), True, cursor_color)
        else: 
            text = self.font.render(self.text, True, cursor_color)

        cursor = self.font.render("|", True, cursor_color)

        if time.time() % 1 > 0.5:
            surface.blit(cursor, (self.x_coord + text.get_rect().width + 10, self.y_coord + 10))

    def clicked_inside_textbox(self):

        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            pygame.mixer.Sound.play(self.sound)
            return True
        
        return False
    
    def clicked_outside_textbox(self):
        pos = pygame.mouse.get_pos()

        if not self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            return True
        
        return False
    
    def is_valid_char(self, char):
        valid_symbols = ['@', '#', "_", ".", ","]

        if char.isalpha() or char.isnumeric() or char in valid_symbols:
            return True

        return False
    
    def get_text(self, surface, censored = False):
        activated = TextBox.clicked_inside_textbox(self)

        while activated:
            if not TextBox.clicked_outside_textbox(self):
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        pygame.quit() 
                    if event.type == pygame.KEYDOWN: 
                        if event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                            activated = False
                        elif len(self.text) > 0 and event.key == pygame.K_BACKSPACE: 
                            self.text = self.text[:-1] 
                        elif len(self.text) < DISPLAY.TEXT_LENGTH and TextBox.is_valid_char(self, event.unicode):
                            self.text += event.unicode
                TextBox.draw(self, surface, COLOR.WHITE)
                TextBox.draw_cursor(self, surface, COLOR.BLACK, censored)
            else:
                TextBox.draw(self, surface, COLOR.GREY)
                activated = False

            TextBox.draw_text(self, surface, COLOR.BLACK, censored)

            pygame.display.update()