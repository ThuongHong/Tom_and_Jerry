import pygame


class Graphic:
    def __init__(self, x_coord, y_coord, image, scale=1):
        width = image.get_width()
        height = image.get_height()
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.modified_width = int(width * scale)
        self.modified_height = int(height * scale)
        self.image = pygame.transform.scale(
            image, (self.modified_width, self.modified_height)
        )
        self.rect = self.image.get_rect()
        self.rect.center = (x_coord, y_coord)

    def draw(self, surface):
        # draw graphic on screen
        surface.blit(self.image, self.rect)

    def change_image(self, image):
        self.image = pygame.transform.scale(
            image, (self.modified_width, self.modified_height)
        )

    def set_alpha(self, alpha):
        self.image.set_alpha(alpha)
