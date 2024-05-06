from game_structure.utility import get_position_after_move
import pygame

class GridCell():
    def __init__(self,
                 grid_position: tuple[int],
                 grid_size: int,
                 scale: int = 1
                 ):
        self.scale = scale
        self._grid_size = grid_size
        self._grid_coord = (grid_position[0] * self.grid_size, grid_position[1] * self.grid_size)
        self.thickness = int(self.grid_size * 4 / 30)

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
    
    @property
    def grid_size(self):
        return self._grid_size * self.scale

    @property
    def grid_coord(self):
        return (self._grid_coord[0] * self.scale, self._grid_coord[1] * self.scale)
    
    def set_scale(self, new_scale):
        self.scale = new_scale

    def update(self, **kwargs):
        if kwargs['scale']:
            self.set_scale(kwargs['scale'])

    def get_position(self) -> tuple[int]:
        """This method return index of this grid in maze

        Returns:
            tuple[int]: None description
        """
        return self.grid_coord[0] // self.grid_size, self.grid_coord[1] // self.grid_size
    
    def get_center_coord(self):
        return (self.grid_coord[0] + self.grid_size // 2, self.grid_coord[1] + self.grid_size // 2)

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

        return '-'.join(features)

    def draw(self, screen, grid_source, is_last= False):
        """This method for drawing a grid"""

        # grid_name = self.get_feature() + '.png' # May be jpg or sth, Fuhoa do not know about thys hee he
        """For test, do not have beautiful display"""
        x, y = self.grid_coord

        if self.walls['top']:
            pygame.draw.line(screen, pygame.Color((255, 255, 255)), (x, y), (x + self.grid_size, y), self.thickness)
        if self.walls['right']:
            pygame.draw.line(screen, pygame.Color((255, 255, 255)), (x + self.grid_size, y), (x + self.grid_size, y + self.grid_size), self.thickness)
        if not is_last:
            if self.walls['bottom']:
                pygame.draw.line(screen, pygame.Color((255, 255, 255)), (x + self.grid_size, y + self.grid_size), (x, y + self.grid_size), self.thickness)
        if self.walls['left']:
            pygame.draw.line(screen, pygame.Color((255, 255, 255)), (x, y + self.grid_size), (x, y), self.thickness)
            
        """Do some thing to visualize this grid""" 
        # raise NotImplementedError       