from solving_maze.solving_maze import solve_maze
from game_structure.maze import Maze
from game_structure.character import Tom
import pygame
from sys import exit


def draw_solution(solution: list[tuple[str, tuple[int]]], screen):
    print(list(solution))
    # for action, state in solution:
    #     print(state, action)

if __name__ == '__main__':
    pygame.init()

    screen = pygame.display.set_mode((1000, 650))
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()

    maze = Maze(maze_size= 25, maze_grid_size= 20)

    maze.generate_new_maze(algorithm= 'HAK', 
                           is_multiple_way= True, 
                           draw= True, 
                           screen= screen, 
                           draw_speed= 'SLOW')
    maze.spawn_start_end_position()

    tom = Tom(maze)

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
        
        # This one use for blit background
        screen.fill((0, 0, 0))

        maze.draw(screen)
        player.update(draw_solution= screen, algorithm= 'DFS')
        player.draw(screen)

        pygame.display.update()
        clock.tick(60)