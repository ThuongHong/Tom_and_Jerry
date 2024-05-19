from game_structure.grid import GridCell
from algorithm.BDFS import BDFS
import random
import pygame
from os import listdir
from os.path import join
import time    

class Maze(pygame.sprite.Group):
    def __init__(self,
                 maze_size: int,
                 maze_grid_size: int,
                 scale: int = 1,
                 screen= None,
                 window_screen= None):
        super().__init__()

        self.maze_size = maze_size
        self._maze_grid_size = maze_grid_size
        self.scale = scale

        self.screen = screen
        self.screen_vector = pygame.math.Vector2(self.screen.get_size())

        self.window_screen = window_screen

        self.scale_surface_offset = pygame.math.Vector2()
        
        self.grids = {}

        for i in range(self.maze_size):
            for j in range(self.maze_size):
                self.grids[i, j] = GridCell(grid_position= (i, j), grid_size= self.maze_grid_size, group= self)
                self.add(
                    self.grids[i, j]
                )

        # Camera offset
        self.offset = pygame.math.Vector2()
        self.half_w = self.screen.get_size()[0] // 2
        self.half_h = self.screen.get_size()[1] // 2

        self.image = None

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def custom_draw(self, player):
        self.center_target_camera(player)
        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft + self.offset
            self.screen.blit(sprite.image, offset_pos)
        
    def image_draw(self, screen):
        screen.blit(self.image, (0, 0))

    @property
    def maze_grid_size(self):
        return self._maze_grid_size * self.scale

    def set_scale(self, new_scale):
        self.scale = new_scale

    def spawn_start_position_for_generate_maze(self) -> tuple[int]:
        """This methos will randomly create start position for generate maze

        Returns:
            tuple[int]: Random position in maze
        """
        x_random = random.randint(0, self.maze_size - 1)
        y_random = random.randint(0, self.maze_size - 1)

        return (x_random, y_random)
    
    def spawn_start_end_position(self, option= 'TOP_BOTTOM', 
                                 start_position= None, 
                                 end_position= None) -> bool:    
        """This method create two class variable start_position and end_position in maze

        Args:
            option (str, optional): One of ['TOP_BOTTOM', 'SELECT']. Defaults to 'TOP_BOTTOM'.
            start_position (tuple[int], optional): If the option is 'SELECT', Fill start_position. Defaults to None.
            end_position (tuple[int], optional): If the option is 'SELECT'. Defaults to None.
            IF DOES NOT PROVIDE ONE OF ARG(start_position or end_position) IF option is SELECT, Raise ValueError
        Returns:
            True if everythings work fine else False
        """
        if option == 'TOP_BOTTOM':
            
            while True:
                start = random.randint(0, self.maze_size - 1)
                end = random.randint(0, self.maze_size - 1)

                self.start_position = (start, 0)
                self.end_position = (end, self.maze_size - 1)

                if BDFS(
                    grids= self.grids,
                    player_current_position= self.start_position,
                    player_winning_position= self.end_position
                ):
                    break
            
            # Remove wall for visualize
            # self.grids[self.start_position].walls['top'] = False
            # self.grids[self.end_position].walls['bottom'] = False

            # self.grids[start, -1] = GridCell(grid_position= (start, -1), 
            #                                  grid_size= self.maze_grid_size,
            #                                  group= self)
            # self.grids[end, self.maze_size] = GridCell(grid_position= (end, self.maze_size), 
            #                                            grid_size= self.maze_grid_size, 
            #                                            group= self)

            # self.grids[start, -1].walls['bottom'] = False
            # self.grids[end, self.maze_size].walls['top'] = False

            return True

        elif option == 'SELECT' and start_position and end_position:
            
            if BDFS(grids= self.grids,
                    player_current_position= start_position,
                    player_winning_position= end_position,
                    algorithm= 'DFS'):
                # self.start_position = start_position
                # self.end_position = end_position

                return True
            
            else: return False
        
        else: return False
    
    def check_grid_exist(self, position: tuple[int]) -> bool:
        """This method will check if a grid is valid or not

        Args:
            position (tuple[int]): None description

        Returns:
            bool: True, False
        """
        if 0 <= position[0] < self.maze_size and 0 <= position[1] < self.maze_size:
            return True
        return False
    
        # return position in self.grids
        # Tien hon neu co o co index am de cho nhan vat bay ra khoi maze :>>
    
    def remove_wall_between_two_grid(self, 
                                     current_grid: tuple[int],
                                     next_grid: tuple[int]):
        """Remove wall between two grid

        Args:
            current_grid (tuple[int]): None_description_
            next_grid (tuple[int]): None_description_
        """
        delta_x = current_grid[0] - next_grid[0]
        delta_y = current_grid[1] - next_grid[1]
        
        # next || current
        if delta_x == 1:
            self.grids[current_grid].walls["left"] = False
            self.grids[next_grid].walls["right"] = False
        # current || next
        elif delta_x == -1:
            self.grids[current_grid].walls["right"] = False
            self.grids[next_grid].walls["left"] = False
        # next
        # ----
        # current
        if delta_y == 1:
            self.grids[current_grid].walls["top"] = False
            self.grids[next_grid].walls["bottom"] = False
        # currrent
        # ----
        # next
        elif delta_y == -1:
            self.grids[current_grid].walls["bottom"] = False
            self.grids[next_grid].walls["top"] = False

    def get_unvisited_grid(self, position: tuple[int]) -> list[tuple[int]]:
        """Return neighbors that is unvisited, This method support for generating maze by using DFS or HAK algorithm

        Args:
            position (tuple[int]): None_description_

        Returns:
            list[tuple[int]]: None_description_
        """
        unvisited_grids = []

        # Iterate for each grid that position cannot move to that(or can say have wall in the connect between two grid)
        for grid in self.grids[position].get_neighbors(is_wall_direction= True): # Option is_wall_direction modify behave of the method. Read GridCell for more
            # Check if is that a valid grid because get_neighbors does not design to check
            # Check if that grid is not visited
            if self.check_grid_exist(position= grid) and not self.grids[grid].is_visited:
                unvisited_grids.append(grid)
        
        return unvisited_grids
    
    def get_visited_grid(self, position: tuple[int]) -> list[tuple[int]]:
        """Return neighbors that is visited, This method support for generating maze by using HAK algorithm

        Args:
            position (tuple[int]): None_description_

        Returns:
            list[tuple[int]]: None_description_
        """
        unvisited_grids = []

        # Iterate for each grid that position cannot move to that(or can say have wall in the connect between two grid)
        for grid in self.grids[position].get_neighbors(is_wall_direction= True): # Option is_wall_direction modify behave of the method. Read GridCell for more
            # Check if is that a valid grid because get_neighbors does not design to check
            # Check if that grid is not visited
            if self.check_grid_exist(position= grid) and self.grids[grid].is_visited:
                unvisited_grids.append(grid)
        
        return unvisited_grids

    def carve_wall_one_line(self, current_grid,
                            is_stack: bool = False,
                            stack: list = None,
                            draw: bool = False, 
                            draw_speed = 'NORMAL'):
        generate_adjust_scale = 0
        if self.maze_size == 20: generate_adjust_scale = 1
        elif self.maze_size == 40: generate_adjust_scale = 0.5
        elif generate_adjust_scale == 100: generate_adjust_scale = 0.2

        while current_grid:
            # Mark current grid visited
            self.grids[current_grid].is_visited = True
            
            # Choose next grid by random neighbors that unvisited of current grid
            try:
                next_grid = random.choice(self.get_unvisited_grid(current_grid))
            # There is a case that current grid does not have any neighbors that unvisited
            # Then will return [], and random.choice() will raise IndexError if input is a empty list
            except IndexError:
                # Set next grid to NULL or Nothing
                next_grid = None

            if next_grid:
                # Does not need this one. Fuhoa Sori:>>
                # self.grids[current_grid].is_visited = True
                if is_stack: 
                    stack.append(current_grid)

                # Create connection between two grid
                self.remove_wall_between_two_grid(current_grid= current_grid,
                                                    next_grid= next_grid)
                
                # Draw maze if you want to see the process
                if draw:
                    self.update()
                    self.draw(self.screen)
                    
                    # scale_surface = pygame.transform.scale(self.screen, self.screen_vector * self.scale)
                    scale_surface = pygame.transform.scale(self.screen, self.screen_vector * generate_adjust_scale)

                    scale_rect = scale_surface.get_rect(center= (500, 325))

                    # self.window_screen.blit(scale_surface, scale_rect.topleft + self.scale_surface_offset)
                    self.window_screen.blit(scale_surface, scale_rect.topleft + self.scale_surface_offset)

                    pygame.display.update()

                    if draw_speed == 'NORMAL':
                        pygame.time.wait(20)
                    elif draw_speed == 'FAST':
                        pygame.time.wait(5)
                    elif draw_speed == 'SLOW':
                        pygame.time.wait(50)

            # Set current to next
            current_grid = next_grid

    def generate_new_maze(self,
                          algorithm: str = 'DFS',
                          draw: bool = False,
                          draw_speed= 'NORMAL'):
        """Generate new maze using following algorithm

        Args:
            algorithm (str, optional): _description_. Defaults to 'DFS'.
        """
        # Generate spawn and end position
        current_grid = self.spawn_start_position_for_generate_maze()
        # self.spawn_start_end_position()

        if algorithm == 'DFS':

            # Stack store grid for later move in backtracking
            DFS_stack = []

            # Define stop condition for generate maze
            break_count = 1
            break_value = self.maze_size ** 2

            # Start generate maze
            while current_grid:
                self.carve_wall_one_line(current_grid= current_grid,
                                         is_stack= True,
                                         stack= DFS_stack,
                                         draw= draw,
                                         draw_speed= draw_speed)
                
                # If does not have next grid -> Backtrack
                if len(DFS_stack) != 0:
                    current_grid = DFS_stack.pop()
                else:
                    break

        elif algorithm == 'HAK': # i.e Hunt and Kill
            # Start generate maze
            
            # Carve until do not any neighbors
            self.carve_wall_one_line(current_grid= current_grid,
                                     draw= draw,
                                     draw_speed= draw_speed)
            # Enter Hunt Mode
            for row in range(self.maze_size):
                for col in range(self.maze_size):
                    try:
                        visited_grids = self.get_visited_grid(position= (col, row))
                    except IndexError:
                        visited_grids = None
                    
                    # If find a grid that not visited and have visited grid in neighbors
                    if not self.grids[col, row].is_visited:
                        
                        # Connect the unvited with visited
                        if visited_grids:
                            for visited_grid in visited_grids:
                                self.remove_wall_between_two_grid(current_grid= (col, row),
                                                                    next_grid= visited_grid)
                            
                        # Carve again
                        self.carve_wall_one_line(current_grid= (col, row),
                                                 draw= draw,
                                                 draw_speed= draw_speed)
                        
        for grid in self.grids:
            self.grids[grid].set_image()

    def is_have_start(self):
        for grid in self.grids:
            if self.grids[grid].is_start:
                return True
        return False

    def is_have_end(self):
        for grid in self.grids:
            if self.grids[grid].is_end:
                return True
        return False