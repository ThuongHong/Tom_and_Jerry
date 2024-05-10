import pygame

class Graphic:
    def __init__(self, x_coord, y_coord, image, scale=1):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x_coord, y_coord)

    def draw(self, surface):
        # draw button on screen
        surface.blit(self.image, self.rect)