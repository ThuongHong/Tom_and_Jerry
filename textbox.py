import pygame

TEXT_LENGTH = 18


class TextBox:
    def __init__(self, x_coord, y_coord, length, width, sound):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.length = length
        self.width = width
        self.sound = sound
        self.rect = pygame.Rect(self.x_coord, self.y_coord, self.length, self.width)

    def draw(self, surface): 
        pygame.draw.rect(surface, (239, 237, 240), self.rect)


class LoginTextBox(TextBox):
    def get_text(self, surface):
        LoginTextBox.draw(self, surface)
        pos = pygame.mouse.get_pos()
        activated = False
        if self.rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
            activated = True
        user_text = ""
        while activated:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    pygame.quit() 

                if event.type == pygame.KEYDOWN: 
                    if len(user_text) > 0 and event.key == pygame.K_BACKSPACE: 
                        user_text = user_text[:-1] 
                    elif event.key == pygame.K_RETURN or event.key == pygame.K_ESCAPE:
                        activated = False
                        break
                    elif len(user_text) < TEXT_LENGTH:
                        user_text += event.unicode

            LoginTextBox.draw(self, surface)
            text_surface = pygame.font.Font("The fountain of wishes.ttf", 40).render(user_text, True, (0, 0, 0)) 
            surface.blit(text_surface, (self.x_coord + 10, self.y_coord + 10))

            pygame.display.update() 
