from game_structure.grid import GridCell
import random

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
    
    def spawn_start_end_position(self, option= 'TOP_BOTTOM'):
        """This method create 2 new class variable call start_position and end_position
        """
        start = random.randint(0, self.maze_size - 1)
        end = random.randint(0, self.maze_size - 1)

        if option == 'TOP_BOTTOM':
            self.start_position = (start, 0)
            self.end_position = (end, self.maze_size - 1)

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

        if delta_x == 1:
            self.grids[current_grid].walls["left"] = False
            self.grids[next_grid].walls["right"] = False
        
        elif delta_x == -1:
            self.grids[current_grid].walls["right"] = False
            self.grids[next_grid].walls["left"] = False
        
        if delta_y == 1:
            self.grids[current_grid].walls["top"] = False
            self.grids[next_grid].walls["bottom"] = False
        
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

        for grid in self.grids[position].get_neighbors(is_wall_direction= True):
            if self.check_grid_exist(position= grid) and not self.grids[grid].is_visited:
                unvisited_grids.append(grid)
        
        return unvisited_grids

    def generate_new_maze(self,
                          algorithm: str = 'DFS'):
        """Generate new maze using following algorithm

        Args:
            algorithm (str, optional): _description_. Defaults to 'DFS'.
        """
        if algorithm == 'DFS':
            self.spawn_start_end_position()
            current_grid = self.start_position
            DFS_stack = []

            break_count = 1
            break_value = self.maze_size ** 2

            while break_count != break_value:
                self.grids[current_grid].is_visited = True
                try:
                    next_grid = random.choice(self.get_unvisited_grid(current_grid))
                except IndexError:
                    next_grid = None
                
                if next_grid:
                    self.grids[current_grid].is_visited = True

                    break_count += 1

                    DFS_stack.append(current_grid)
                    self.remove_wall_between_two_grid(current_grid= current_grid,
                                                      next_grid= next_grid)
                    
                    current_grid = next_grid
                
                elif len(DFS_stack) != 0:
                    current_grid = DFS_stack.pop()

        elif algorithm == 'HAK': # e.g Hunt and Kill
            pass
    
    def draw(self, screen):
        """For test, no use for real game"""
        for position in self.grids:
            self.grids[position].draw(screen, self.maze_grid_size)