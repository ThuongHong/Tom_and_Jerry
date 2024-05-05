from game_structure.grid import GridCell
from algorithm.BDFS import BDFS
import random
import pygame
import time    

class Maze():
    def __init__(self,
                 maze_size: int,
                 maze_grid_size: int,
                 scale: int = 1):
        self.maze_size = maze_size
        self.maze_grid_size = maze_grid_size
        self.scale = scale
        
        self.grids = {}

        for i in range(self.maze_size):
            for j in range(self.maze_size):
                self.grids[i, j] = GridCell(grid_position= (i, j), grid_size= self.maze_grid_size)

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
                                 end_position= None):    
        """This method create two class variable start_position and end_position in maze

        Args:
            option (str, optional): One of ['TOP_BOTTOM', 'SELECT']. Defaults to 'TOP_BOTTOM'.
            start_position (tuple[int], optional): If the option is 'SELECT', Fill start_position. Defaults to None.
            end_position (tuple[int], optional): If the option is 'SELECT'. Defaults to None.
            IF DOES NOT PROVIDE ONE OF ARG(start_position or end_position) IF option is SELECT, Raise ValueError
        """
        if option == 'TOP_BOTTOM':
            start = random.randint(0, self.maze_size - 1)
            end = random.randint(0, self.maze_size - 1)

            self.start_position = (start, 0)
            self.end_position = (end, self.maze_size - 1)
            
            # Remove wall for visualize
            self.grids[self.start_position].walls['top'] = False
            self.grids[self.end_position].walls['bottom'] = False

            self.grids[start, -1] = GridCell((start, -1), self.maze_grid_size)
            self.grids[end, self.maze_size] = GridCell((end, self.maze_size), self.maze_grid_size)

            self.grids[start, -1].walls['bottom'] = False
            self.grids[end, self.maze_size].walls['top'] = False

        elif option == 'SELECT' and start_position and end_position:
            if BDFS(grids= self.grids,
                    player_current_position= start_position,
                    player_winning_position= end_position,
                    algorithm= 'DFS'):
                self.start_position = start_position
                self.end_position = end_position
            else: return False
        
        else: raise ValueError("Missing Inputs")
    
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
            if self.check_grid_exist(position= grid) and self.grids[grid].is_visited:
                unvisited_grids.append(grid)
        
        return unvisited_grids

    def draw(self, screen):
        """For test, no use for real game"""
        screen.fill((0, 0, 0))

        for position in self.grids:
            is_last_grid = True if position[1] == self.maze_size else False
            self.grids[position].draw(screen, self.maze_grid_size, is_last= is_last_grid)

    def carve_wall_one_line(self, current_grid,
                            is_stack: bool = False,
                            stack: list = None,
                            draw: bool = False, 
                            screen = None, 
                            draw_speed = 'NORMAL'):
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
                    self.draw(screen= screen)
                    pygame.display.update()
                    if draw_speed == 'NORMAL':
                        time.sleep(0.01)
                    elif draw_speed == 'FAST':
                        time.sleep(0.0001)

            # Set current to next
            current_grid = next_grid

    def generate_new_maze(self,
                          algorithm: str = 'DFS',
                          draw: bool = False,
                          screen = None,
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
                                         screen= screen,
                                         draw_speed= draw_speed)
                # Mark current grid visited
                # self.grids[current_grid].is_visited = True
                
                # # Choose next grid by random neighbors that unvisited of current grid
                # try:
                #     next_grid = random.choice(self.get_unvisited_grid(current_grid))
                # # There is a case that current grid does not have any neighbors that unvisited
                # # Then will return [], and random.choice() will raise IndexError if input is a empty list
                # except IndexError:
                #     # Set next grid to NULL or Nothing
                #     next_grid = None
                
                # if next_grid:
                #     # Does not need this one. Fuhoa Sori:>>
                #     # self.grids[current_grid].is_visited = True

                #     # Because we will loop until all gird in maze is visited so if we can move to other grid, we increase th value of break_count to 1
                #     break_count += 1

                #     # Append to DFS_stack for backtracking later
                #     DFS_stack.append(current_grid)

                #     # Create connection between two grid
                #     self.remove_wall_between_two_grid(current_grid= current_grid,
                #                                       next_grid= next_grid)
                #                     # Draw maze if you want to see the process
                #     if draw:
                #         self.draw(screen= screen)
                #         pygame.display.update()
                #         if draw_speed == 'NORMAL':
                #             time.sleep(0.01)
                #         elif draw_speed == 'FAST':
                #             time.sleep(0.0001)

                #     # Set current to next
                #     current_grid = next_grid
                
                # If does not have next grid -> Backtrack
                if len(DFS_stack) != 0:
                    current_grid = DFS_stack.pop()
                else:
                    break

        elif algorithm == 'HAK': # e.g Hunt and Kill
            # Start generate maze
            
            # Carve until do not any neighbors
            self.carve_wall_one_line(current_grid= current_grid,
                                     draw= draw,
                                     screen= screen,
                                     draw_speed= draw_speed)
            # Enter Hunt Mode
            for i in range(self.maze_size):
                for j in range(self.maze_size):
                    visited_grids = self.get_visited_grid(position= (i, j))
                    # If find a grid that not visited and have visited grid in neighbors
                    if not self.grids[i, j].is_visited and visited_grids:
                        # Connect the unvited with visited
                        for grid in visited_grids:
                            self.remove_wall_between_two_grid(current_grid= (i, j),
                                                              next_grid= grid)
                        
                        # Carve again
                        self.carve_wall_one_line(current_grid= (i, j),
                                                 draw= draw,
                                                 screen= screen,
                                                 draw_speed= draw_speed)



