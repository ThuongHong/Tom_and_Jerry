from game_structure.maze import Maze
from game_structure.utility import get_position_after_move, get_diffirent_coord
from os.path import join
from os import listdir
import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self,
                 character_maze: Maze,
                 imgs_directory: str = None,
                 img_scale: int = 1):
        super().__init__()

        self.Maze = character_maze
        self.position = self.Maze.start_position
        
        # Rect will be draw while we using GroupSingle then add this character
        img_tmp = pygame.image.load(r'imgs/tom_norm.jpg').convert_alpha()
        
        bigger_size = img_tmp.get_height() if (img_tmp.get_height() > img_tmp.get_width()) else img_tmp.get_width()
        scale_index = bigger_size // self.Maze.maze_grid_size
        self.image = pygame.transform.rotozoom(img_tmp, 0, 1 / scale_index)

        self.rect = self.image.get_rect(topleft= (self.position[0] * self.Maze.maze_grid_size,
                                                  self.position[1] * self.Maze.maze_grid_size))

    def is_valid_move(self, direction: str) -> bool:
        if get_position_after_move(position= self.position,
                                   direction= direction) in self.Maze.grids[self.position].get_neighbors():
            return True
        return False
        
    def move(self, direction: str):
        if self.is_valid_move(direction= direction):
            self.position = get_position_after_move(position= self.position, direction= direction)
            
            move_coord = get_diffirent_coord(direction= direction, maze_grid_size= self.Maze.maze_grid_size)
            self.rect = self.rect.move(move_coord[0], move_coord[1])

    def update(self, **kwargs):
        """This method is use for update state of character. This one is one of method of Group() in pygame we will use later because we cannot create a sprite not have group include its
        """
        if 'direction' in kwargs:
            self.move(direction= kwargs['direction'])
        # More feature like draw, update img, state of character

class Tom(Character):
    def __init__(self,
                 maze: Maze,
                 ):
        super().__init__(character_maze= maze)