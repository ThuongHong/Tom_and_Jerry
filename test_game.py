from game_structure.maze import Maze
from game_structure.character import Tom
from game_structure.game import GamePlay
import pygame
import time

if __name__ == '__main__':
    pygame.init()

    m = Maze(10, 30)
    screen = pygame.display.set_mode((1000, 650))
    screen.fill((0, 0, 0))
    m.generate_new_maze('HAK', True, screen, 'FAST')
    m.spawn_start_end_position()

    p = pygame.sprite.GroupSingle()
    p.add(Tom(m))

    g = GamePlay(p)

    g.run(screen)

