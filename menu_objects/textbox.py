import pygame
import time
import os
from menu_objects import button
from CONSTANTS import DISPLAY
from CONSTANTS import COLOR

def create_img(image_source, image_name):
    image_name = image_name + '.png'
    return pygame.image.load(os.path.join(image_source, image_name)).convert_alpha()

class TextBox:
    def __init__(self, x_coord, y_coord, length, width, image_source, sound_source):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.length = length
        self.width = width
        self.sound = sound_source
        self.rect = pygame.Rect(self.x_coord, self.y_coord, self.length, self.width)
        self.text = ""
        fontsize = 38
        # self.font = pygame.font.SysFont('ShakyHandSomeComic-Bold', fontsize)
        self.font = pygame.font.Font('fonts/ShakyHandSomeComic-Bold.otf', 38)


        self.eye1_img = create_img(image_source, 'eye_1')
        self.eye2_img = create_img(image_source, 'eye_2')
        self.eye1_button = button.Button(self.x_coord + 270, self.y_coord + 23, self.eye1_img, self.sound, 0.1, 0.11)
        self.eye2_button = button.Button(self.x_coord + 270, self.y_coord + 23, self.eye2_img, self.sound, 0.1, 0.11)

    def draw(self, surface, color): 
        pygame.draw.rect(surface, color, self.rect, border_radius=int(self.width * 0.2))

    def draw_text(self, surface, cursor_color, is_password, censored, activated=False):
        if is_password and censored:
            text = self.font.render("*" * len(self.text), True, cursor_color)
        else: 
            text = self.font.render(self.text, True, cursor_color)

        surface.blit(text, (self.x_coord + 10, self.y_coord + 10))

        if activated:
            cursor = self.font.render("|", True, cursor_color)

            if time.time() % 1 > 0.5:
                surface.blit(cursor, (self.x_coord + text.get_rect().width + 10, self.y_coord + 10))
    
    def clicked_inside_textbox(self, event=None, sound_on = True):
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
                if sound_on == True:
                    pygame.mixer.Sound.play(self.sound)
                return True
        return False
    
    def clicked_outside_textbox(self, event):
        pos = pygame.mouse.get_pos()

        if not self.rect.collidepoint(pos) and event.type == pygame.MOUSEBUTTONDOWN:
            return True
        
        return False
    
    def is_valid_char(self, char):
        valid_symbols = ['@', '#', "_", ".", ","]

        if char.isalpha() or char.isnumeric() or char in valid_symbols:
            return True

        return False
    
    def get_text(self, surface, back_button, submit_button, event, is_password=False, censored=False, sound_on = True):
        activated = TextBox.clicked_inside_textbox(self, event, sound_on)

        while activated:
            pos = pygame.mouse.get_pos()
            
                        
            if not TextBox.clicked_outside_textbox(self, event):
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
            else:
                TextBox.draw(self, surface, COLOR.GREY)
                activated = False
            
            if is_password:
                if censored:
                    if self.eye1_button.draw(surface, pos, event, sound_on):
                        censored = False
                else:
                    if self.eye2_button.draw(surface, pos, event, sound_on):
                        censored = True

            TextBox.draw_text(self, surface, COLOR.BLACK, is_password, censored, activated)

            if back_button.draw(surface, pos, event, sound_on):
                return 'back'
            
            if submit_button.draw(surface, pos, event, sound_on):
                return 'submit'

            pygame.display.flip()

        return None