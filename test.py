import pygame
import random

class MyConstant:
    TILE_SIZE = 30
    MAZE_SIZE = 10
    BOLDER_WIDTH = 4
    def __init__(self):
        pass

class Cell:
    def __init__(self,
                 x_position: int,
                 y_position: int,
                 bolder_width: int,
                 parent = None
                 ):
        self.x = x_position
        self.y = y_position
        self.bolder_width = bolder_width
        self.is_visited = False
        self.parent = parent
        self.walls = {
            "top": True,
            "right": True,
            "bottom": True,
            "left": True
        }

    def __str__(self) -> str:
        return f"""
        Block at {self.x}, {self.y}
        Top: {self.walls["top"]}
        Right: {self.walls["right"]}
        Bottom: {self.walls["bottom"]}
        Left: {self.walls["left"]}
        """
    
    def _draw(self, sc, tile):
        x, y = self.x * tile, self.y * tile
        if self.walls['top']:
            pygame.draw.line(sc, pygame.Color((255, 255, 255)), (x, y), (x + tile, y), self.bolder_width)
        if self.walls['right']:
            pygame.draw.line(sc, pygame.Color((255, 255, 255)), (x + tile, y), (x + tile, y + tile), self.bolder_width)
        if self.walls['bottom']:
            pygame.draw.line(sc, pygame.Color((255, 255, 255)), (x + tile, y + tile), (x , y + tile), self.bolder_width)
        if self.walls['left']:
            pygame.draw.line(sc, pygame.Color((255, 255, 255)), (x, y + tile), (x, y), self.bolder_width)
            
    def _get_position(self):
        return (self.x, self.y)

class Maze:
    def __init__(self,
                 maze_size: int):
        self.size = maze_size
        
        self.maze = {}
        for i in range(self.size):
            for j in range(self.size):
                self.maze[(i, j)] = Cell(x_position= i,
                                         y_position= j,
                                         bolder_width= MyConstant.BOLDER_WIDTH)
        
    @classmethod
    def _get_random_cell(cls, size: int) -> tuple[int]:
        x_position = random.randint(0, size - 1)
        y_position = random.randint(0, size - 1)
        return (x_position, y_position)

    def _check_cell_exist(self, 
                          position: tuple[int]
                          ) -> Cell:
        x_position, y_position = position
        if x_position < 0 or y_position < 0 or x_position > self.size - 1 or y_position > self.size - 1:
            return False
        return (x_position, y_position)
        # return self.maze[(x_position, y_position)]
    
    def _check_neighbors_cell(self, 
                              position: tuple[int]
                              ) -> Cell:
        neighbors = []
        x_position, y_position = position
        top_cell = self._check_cell_exist((x_position, y_position - 1))
        right_cell = self._check_cell_exist((x_position + 1, y_position))
        bottom_cell = self._check_cell_exist((x_position, y_position + 1))
        left_cell = self._check_cell_exist((x_position - 1, y_position))
        if top_cell and not self.maze[top_cell].is_visited:
            neighbors.append(top_cell)
        if right_cell and not self.maze[right_cell].is_visited:
            neighbors.append(right_cell)
        if bottom_cell and not self.maze[bottom_cell].is_visited:
            neighbors.append(bottom_cell)
        if left_cell and not self.maze[left_cell].is_visited:
            neighbors.append(left_cell)
        return random.choice(neighbors) if neighbors else None
    
    def _remove_wall_in_cell(self, 
                             current_position: tuple[int], 
                             next_position: tuple[int]
                             ) -> None:
        _delta_x = current_position[0] - next_position[0]
        _delta_y = current_position[1] - next_position[1]

        if _delta_x == 1:
            self.maze[current_position].walls["left"] = False
            self.maze[next_position].walls["right"] = False
        elif _delta_x == -1:
            self.maze[current_position].walls["right"] = False
            self.maze[next_position].walls["left"] = False
        
        if _delta_y == 1:
            self.maze[current_position].walls["top"] = False
            self.maze[next_position].walls["bottom"] = False
        elif _delta_y == -1:
            self.maze[current_position].walls["bottom"] = False
            self.maze[next_position].walls["top"] = False

    def _generate_maze(self):
        _index_current_cell = (0, 0)
        _index_current_cell = Maze._get_random_cell(size= self.size)
        self._start_position = _index_current_cell
        self._end_position_lst = []
        _stack_of_cell = []
        break_count = 1
        size_flatten = self.size ** 2
        while break_count != size_flatten:
            self.maze[_index_current_cell].is_visited = True
            _index_next_cell = self._check_neighbors_cell(_index_current_cell)

            if _index_next_cell:
                self.maze[_index_next_cell].is_visited = True
                self.maze[_index_next_cell].parent = _index_current_cell

                break_count += 1

                _stack_of_cell.append(_index_current_cell)
                self._remove_wall_in_cell(
                    current_position= _index_current_cell,
                    next_position= _index_next_cell
                )

                _index_current_cell = _index_next_cell

            elif _stack_of_cell:
                self._end_position_lst.append(_index_current_cell)
                _index_current_cell = _stack_of_cell.pop()
                        
        self._end_position = random.choice(self._end_position_lst)
    
    def _draw_maze(self, 
                   sc: pygame.Surface, 
                   tile_size: int
                   ):
        for position in self.maze:
            self.maze[position]._draw(sc, tile_size)
    
    def _draw_start_end(self,
                        sc: pygame.Surface,
                        tile_size: int = 30
                        ):
        pygame.draw.circle(sc, pygame.Color(255, 0, 0), 
                           center= (self._start_position[0] * tile_size + tile_size // 2, 
                                    self._start_position[1] * tile_size + tile_size // 2), 
                           radius= 8)
        pygame.draw.circle(sc, pygame.Color(0, 255, 0), 
                           center= (self._end_position[0] * tile_size + tile_size // 2, 
                                    self._end_position[1] * tile_size + tile_size // 2), 
                           radius= 8)
        
    def _draw_result(self,
                     sc: pygame.Surface,
                     tile_size: int):
        last_cell = self.maze[self._end_position].parent
        
        while last_cell != self._start_position:
            pygame.draw.circle(sc, pygame.Color(0, 0, 255), 
                               center= (last_cell[0] * tile_size + tile_size // 2, 
                                        last_cell[1] * tile_size + tile_size // 2), 
                                        radius= 3)
            last_cell = self.maze[last_cell].parent

if __name__ == "__main__":       
    window_size = (700, 700)
    screen = (window_size[0] + 150, window_size[-1])

    screen = pygame.display.set_mode(screen)
    pygame.display.set_caption("Maze")


    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()

    m = Maze(maze_size= MyConstant.MAZE_SIZE)
    m._generate_maze()
    print(type(m._start_position))