import pygame
from os.path import join

class EnergyItem(pygame.sprite.Sprite):
    def __init__(self,
                 group,
                 grid_position: tuple[int],
                 grid_size: int,
                 hp: int = 1,
                 scale: int = 1,
                 img_directory: str = r'images/Energy'):
        super().__init__(group)

        self.offset = pygame.math.Vector2(0, 40)

        self.position = grid_position
        self.scale = scale
        self._grid_size = grid_size
        self._grid_coord = (grid_position[0] * self.grid_size, grid_position[1] * self.grid_size)

        self.is_visited = False

        if hp <= 0:
            self.hp = 1
        elif hp > 5:
            raise ValueError(hp)
        else:
            self.hp = hp

        # Load ảnh ứng với HP
        image_name = str(self.hp) + '.png'
        self.image = pygame.image.load(join(img_directory, image_name)).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.grid_size * 0.8, self.grid_size * 0.8))
        # self._grid_size = self.image.get_height()
        # self.image = pygame.transform.rotozoom(self.image, 0, self.grid_size / self.image.get_height())    
        self.rect = self.image.get_rect(center= self.grid_coord_center)

    @property
    def grid_size(self):
        return self._grid_size * self.scale
    @property
    def grid_coord(self):
        return (self._grid_coord[0] * self.scale + self.offset[0], 
                self._grid_coord[1] * self.scale + self.offset[1])
    @property
    def grid_coord_center(self):
        return (
            self.grid_coord[0] + self.grid_size / 2,
            self.grid_coord[1] + self.grid_size / 2.1,

        )
    def update(self, player,**kwargs):
        if player.position == self.position:
            player.hp += self.hp
