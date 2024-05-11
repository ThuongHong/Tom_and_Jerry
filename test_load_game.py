from game_structure.maze import Maze
from game_structure.character import Tom
from game_structure.game import GamePlay, load_GamePlay
import pygame
import time

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1000, 650))
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()

    Game = load_GamePlay(game_id= 10, screen= screen)
    i = 1
    j = 0
    
    while Game.game_state == 'in_game':
        if i:
            Game.visualize_process(algorithm= 'BFS')

            # Game.visualize_solution()
            i -= 1
        j += 1
        Game.run()

        pygame.display.update()