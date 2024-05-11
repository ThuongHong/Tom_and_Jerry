from game_structure.maze import Maze
from game_structure.utility import get_position_after_move, get_diffirent_coord, get_direction
from solving_maze.solving_maze import solve_maze
from algorithm.draw_utility import mark_grid
from Game_Constant.Color import Color
from os.path import join
from os import listdir
import pygame

class Character(pygame.sprite.Sprite):
    def __init__(self,
                #  character_maze: Maze,
                 start_position: tuple[int],
                 grid_size: int,
                 screen,
                 imgs_directory: str = None,
                 img_scale: int = 1):
        super().__init__()

        # self.Maze = character_maze
        # self.position = self.Maze.start_position
        self.position = start_position
        self._grid_size = grid_size
        self.scale = img_scale
        self.screen = screen

        self.step_moves = 0
        
        # Rect will be draw while we using GroupSingle then add this character
        img_tmp = pygame.image.load(r'imgs/tom_norm.jpg').convert_alpha()
        
        bigger_size = img_tmp.get_height() if (img_tmp.get_height() > img_tmp.get_width()) else img_tmp.get_width()
        scale_index = bigger_size // self.grid_size
        self.image = pygame.transform.rotozoom(img_tmp, 0, 1 / scale_index)

        self.rect = self.image.get_rect(topleft= (self.position[0] * self.grid_size,
                                                  self.position[1] * self.grid_size))

    @property
    def grid_size(self):
        return self._grid_size * self.scale

    def set_scale(self, new_scale):
        self.scale = new_scale

    def is_valid_move(self, direction: str, grids) -> bool:
        if get_position_after_move(position= self.position,
                                   direction= direction) in grids[self.position].get_neighbors():
            return True
        return False
    
    # def teleport(self, new_position):
    #     direction = get_direction(current_grid= self.position,
    #                                     next_grid= new_position,
    #                                     maze_grid_size= self.grid_size)
    #     self.position = new_position
    #     move_coord = get_diffirent_coord(direction= direction, maze_grid_size= self.grid_size)
    #     self.rect.move(move_coord[0], move_coord[1])

    #     pygame.time.wait(10)

    #     # self.step_moves += 1
        
    def move(self, direction: str, grids):
        if self.is_valid_move(direction= direction, grids= grids):
            self.position = get_position_after_move(position= self.position, direction= direction)
            
            move_coord = get_diffirent_coord(direction= direction, maze_grid_size= self.grid_size)
            self.rect = self.rect.move(move_coord[0], move_coord[1])
            
            self.step_moves += 1

    # def update(self, **kwargs):
    #     """This method is use for update state of character. This one is one of method of Group() in pygame we will use later because we cannot create a sprite not have group include its
    #     """
    #     if 'direction' in kwargs:
    #         self.move(direction= kwargs['direction'])
    #     # More feature like draw, update img, state of character


class Tom(Character):
    YELLOW = (255, 255, 0)

    def __init__(self,
                #  maze: Maze,
                 start_position: tuple[int],
                 grid_size: int,
                 screen,
                 scale: int
                 ):
        super().__init__(start_position= start_position,
                         grid_size= grid_size,
                         screen= screen,
                         img_scale= scale)
        
    def draw_solution(self, 
                      solution: list,
                      grids = None):
        """This method will draw a line from current position of Tom to the end position

        Args:
            solution (list): This solution include move and the grid after move
            grids (_type_, optional): Take the information of grid like coord to draw. Defaults to None.
        """
        # If do not have solution a.k.a you in the right spot
        if not solution: return

        while solution:
            # Iterate for all grir and mark it
            current_grid = solution.pop(0)[1]
            mark_grid(grids= grids,
                      current_grid= current_grid,
                      screen= self.screen,
                      color= (255, 255, 0))

        # pygame.display.update()

    def update(self, maze,
               scale: int = None,
               direction: str = None, 
               show_solution: bool = False, 
               algorithm: str = 'DFS',
                **kwargs) -> bool:
        """Update state of player

        Args:
            scale (float): current_scale
            direction (str): If want to update move
            draw_solution (pygame.Surface): Given screen if want to draw solution
        """
        # May be using for loop here, update later
        
        # If want to zoom change the scale -> If that scale != current scale zoom player
        if scale:
            if scale != self.scale:
                self.set_scale(kwargs['scale'])

                self.image = pygame.transform.rotozoom(self.image, 0, self.scale)

                self.rect = self.image.get_rect(topleft= (self.position[0] * self.grid_size,
                                                        self.position[1] * self.grid_size))
                
        # If direction is given so move the player
        if direction:
            self.move(direction= direction, grids= maze.grids)

        # If show_solution so draw_solution
        if show_solution:
            solution = solve_maze(player= self, 
                                  maze= maze, 
                                  algorithm= algorithm)                
            self.draw_solution(solution= solution,
                                grids= maze.grids,
                                screen= self.screen)  
           
        # More feature like draw, update img, state of character
