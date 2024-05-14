from game_structure.utility import get_position_after_move
from os.path import join
import pygame

class GridCell(pygame.sprite.Sprite):
    def __init__(self,
                 group,
                 grid_position: tuple[int],
                 grid_size: int,
                 scale: int = 1
                 ):
        super().__init__(group)

        self.offset = pygame.math.Vector2(0, 40)

        self.position = grid_position
        self.scale = scale
        self._grid_size = grid_size
        self._grid_coord = (grid_position[0] * self.grid_size, grid_position[1] * self.grid_size)
        # self.thickness = int(self.grid_size * 4 / 30) // 2

        # Variable check if cell is go over or not in generate maze by using DFS algorithm
        self.is_visited = False

        # Walls specify for wall in one grid cell
        # Performd clockwise ----- Important
        self.walls = {
            'top': True,
            'right': True,
            'bottom': True,
            'left': True
        }
        self.old_feature = ""
        self.set_image()
    
    @property
    def grid_size(self):
        return self._grid_size * self.scale
    @property
    def grid_coord(self):
        return (self._grid_coord[0] * self.scale + self.offset[0], 
                self._grid_coord[1] * self.scale + self.offset[1])
    
    def get_wall_direction(self) -> list[str]:
        """This method support for DFS algorithm in generate maze. Opposite with the method below

        Returns:
            list[str]: 'T', 'R', 'B', 'L'
        """
        wall_directions = []

        for direction in self.walls:
            # If this direction has wall
            if self.walls[direction]: 
                wall_directions.append(direction[0].upper())

        return wall_directions

    def get_actions(self) -> list[str]:
        """This method will look over the neighbor and return action it's can make.

        Returns:
            list[str]: 'T', 'R', 'B', 'L'
        """
        actions = []

        for direction in self.walls:
            # If this direction does not have wall
            if not self.walls[direction]: 
                actions.append(direction[0].upper())
        
        return actions

    def get_neighbors(self, is_wall_direction: bool= False, is_get_direction: bool = False) -> list[tuple[int]]:
        """Dafault: Return neighbors that this grid can move. Modified: like description

        Args:
            is_wall_direction (bool, optional): If we want to get the neighbors that this grid cannot move to. Opposite to the meaning of method in the first place
            is_get_direction (bool, optional): A boolean if we want to get either direction and grid cell. Defaults to False.

        Returns:
            list[tuple[int]]: _description_
        """
        actions = []
        neighbors = []
        
        # If we want to get neighbors grid that can not move to
        if is_wall_direction:
            for direction in self.get_wall_direction():
                neighbors.append(get_position_after_move(self.get_position(), direction= direction))
        
        # Otherwise
        else:
            for action in self.get_actions():
                neighbors.append(get_position_after_move(self.get_position(), direction= action))
                actions.append(action)
        
        # If want to get the action
        if is_get_direction: return zip(actions, neighbors)
        
        # Otherwise
        return neighbors
    
    def get_position(self) -> tuple[int]:
        """This method return index of this grid in maze

        Returns:
            tuple[int]: None description
        """
        return self.position

    def set_scale(self, new_scale):
        if new_scale != self.scale:
            self.scale = new_scale
            self.set_image()

    @property
    def get_feature(self) -> str:
        """Thie method return feature of this cell to be easier for visualize. Perform clockwise

        Returns:
            str: A feature str, e.g 'top-right', 'right-bottom-left'
        """
        features = []

        # If there is a wall in any direction, append it to features
        if self.walls['top']: features.append('top')
        if self.walls['right']: features.append('right')
        if self.walls['bottom']: features.append('bottom')
        if self.walls['left']: features.append('left')

        if not features: return 'no-wall' + '.png'

        return '-'.join(features) + '.png'

    def set_image(self):
        """Use this method after generate maze
        """
        if self.get_feature != self.old_feature:
            self.image = pygame.image.load(join('Graphics', 'Grids', self.get_feature)).convert_alpha()
            self.old_feature = self.get_feature
            # self._grid_size = self.image.get_height()
            self.image = pygame.transform.rotozoom(self.image, 0, self.grid_size / self.image.get_height())
            
            self.rect = self.image.get_rect(topleft= self.grid_coord)
    
    # @property
    # def rect(self):
    #     return self._rect.topleft - self.offset
    
    def update(self,scale = None, offset_change = None, **kwargs):
        # if scale:
            # if scale != self.scale:
            #     self.set_scale(scale)
        if offset_change:
            self.offset = self.offset - offset_change
        
        self.set_image()