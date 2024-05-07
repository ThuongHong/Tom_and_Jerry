from Game_Structure.maze import Maze
from Game_Structure.character import Tom
from Game_Structure.game import GamePlay
import pygame
import time

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1000, 650))
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()

    Game = GamePlay(20, 30, (0, 0), (500, 500), [True, False], screen, 1)

    while True:
        # If anytime we want to draw solution or process
        Game.visualize_process()

        # Game.visualize_solution()

        Game.run()


        pygame.display.update()