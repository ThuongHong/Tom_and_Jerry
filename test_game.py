from game_structure.maze import Maze
from game_structure.character import Tom
from game_structure.game import GamePlay
import pygame
import time

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1000, 650))
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()

    Game = GamePlay(maze_size= 20,
                    grid_size= 30,
                    start_coord_screen= (0, 0),
                    end_coord_screen= (500, 500),
                    screen= screen,
                    scale= 1)
    Game.generate(ondraw= False)
    Game.spawn_random()
    i = 1
    j = 0
    while True:
        if i:
            Game.visualize_process(algorithm= 'AStar')

            # Game.visualize_solution()
            i -= 1
        j += 1
        Game.run()

        if j == 400:
            Game.de_visualize_process()
            Game.de_visualize_solution()
            Game.update_screen()
            Game.visualize_process(algorithm= 'BFS')
        if j == 800:
            Game.de_visualize_process()
            Game.de_visualize_solution()
            Game.update_screen()
            Game.visualize_process(algorithm= 'GBFS')
        if j == 1200:    
            Game.de_visualize_process()
            Game.de_visualize_solution()
            Game.update_screen()
            Game.visualize_process(algorithm= 'DFS')

        # if j == 200:
        #     Game.de_visualize_process()
        # Game.de_visualize_process()
        # Game.de_visualize_solution()


        pygame.display.update()