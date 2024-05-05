import pygame
from game_structure.maze import Maze

class GamePlay():
    def __init__(self,
                 screen,                 
                 maze_size: int,
                 maze_grid_size: int,
                 clock: pygame.time.Clock, 
                 is_generate: bool = True,
                 generate_algorithm: str = None,
                 show_generate_process: bool = True,
                 ):
        pygame.init()
        self.screen = screen

        self.game_clock = clock

        self.game_clock.tick()

        self.maze = Maze(maze_size= maze_size, maze_grid_size= int)

        if is_generate:
            self.maze.generate_new_maze(algorithm= generate_algorithm, 
                                        draw= show_generate_process,
                                        draw_speed= 'NORMAL')
