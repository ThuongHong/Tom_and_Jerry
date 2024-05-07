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

    Game = GamePlay(10, 30, (0, 0), (500, 500), [True, False], screen, 1)

    Game.run(screen)

    pygame.display.update()