from game_structure.maze import Maze
from game_structure.character import Character
import pygame
from sys import exit

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((500, 500))
    clock = pygame.time.Clock()

    maze = Maze(maze_size= 20, maze_grid_size= 30)
    maze.generate_new_maze()

    tom = Character(maze)

    player = pygame.sprite.GroupSingle()
    player.add(tom)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.update(direction= 'L')
                elif event.key == pygame.K_RIGHT:
                    player.update(direction= 'R')
                elif event.key == pygame.K_UP:
                    player.update(direction= 'T')
                elif event.key == pygame.K_DOWN:
                    player.update(direction= 'B')
        
        screen.fill((0, 0, 0))

        maze.draw(screen)
        player.draw(screen)

        pygame.display.update()
        clock.tick(60)