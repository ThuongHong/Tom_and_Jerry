import pygame

class Button:
    def __init__(self, x_coord, y_coord, image, sound, scale=1, hover_scale=1.1):
        width = image.get_width()
        height = image.get_height()
        self.modified_width = int(width * scale)
        self.modified_height = int(height * scale)
        self.modified_hover_width = int(width * hover_scale)
        self.modified_hover_height = int(height * hover_scale)
        
        self.sound = sound
        self.image = pygame.transform.scale(image, (self.modified_width, self.modified_height))
        self.hover_image = pygame.transform.scale(image, (self.modified_hover_width, self.modified_hover_height))
        self.image_rect = self.image.get_rect()
        self.hover_image_rect = self.hover_image.get_rect()
        self.image_rect.center = (x_coord, y_coord)
        self.hover_image_rect.center = (x_coord, y_coord)
        self.mouse_down = False
        self.mouse_click = False
    
    def draw(self, surface, pos, sound_on):
        action = False
        # check mouseover and clicked conditions
        if self.image_rect.collidepoint(pos) and self.mouse_click == False:
            surface.blit(self.hover_image, self.hover_image_rect)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouse_down = True
                if event.type == pygame.MOUSEBUTTONUP and self.mouse_down == True:
                    self.mouse_click = True
                
        else:
            surface.blit(self.image, self.image_rect)
            self.mouse_down = False
        
        if self.mouse_click == True:
            if sound_on == True:
                pygame.mixer.Sound.play(self.sound)
            action = True
            self.mouse_down = False
            self.mouse_click = False
        
        return action
