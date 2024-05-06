import pygame

class Button:
    def __init__(self, x_coord, y_coord, image, sound, scale=1, hover_scale=1.1):
        width = image.get_width()
        height = image.get_height()
        self.modified_width = int(width * scale)
        self.modified_height = int(height * scale)
        self.modified_hover_width = int(width * hover_scale)
        self.modified_hover_height = int(height * hover_scale)
        self.hover_x_coord = int(x_coord - (self.modified_hover_width - self.modified_width) / 2)
        
        self.sound = sound
        self.image = pygame.transform.scale(image, (self.modified_width, self.modified_height))
        self.hover_image = pygame.transform.scale(image, (self.modified_hover_width, self.modified_hover_height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_coord, y_coord)
        self.mouse_down = False
        self.mouse_click = False
    
    def draw(self, surface):
        action = False
        pos = pygame.mouse.get_pos()
        
        # check mouseover and clicked conditions
        if self.rect.collidepoint(pos):
            if self.mouse_click == False:
                surface.blit(self.hover_image, (self.hover_x_coord, self.rect.y))
                for event in pygame.event.get():
                    pos = pygame.mouse.get_pos()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        self.mouse_down = True
                    if event.type == pygame.MOUSEBUTTONUP and self.mouse_down == True:
                        self.mouse_click = True
                
        else:
            surface.blit(self.image, (self.rect.x, self.rect.y))
            self.mouse_down = False
        
        if self.mouse_click == True:
            pygame.mixer.Sound.play(self.sound)
            action = True
            self.mouse_down = False
            self.mouse_click = False
        
        return action