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

    # Game = GamePlay(maze_size= 20,
    #                 grid_size= 15,
    #                 start_coord_screen= (0, 0),
    #                 end_coord_screen= (500, 500),
    #                 screen= screen,
    #                 scale= 1)
    # Game.generate(ondraw= False)
    # Game.spawn_random()
    Game = load_GamePlay(game_id= 8)
    i = 1
    j = 0
    # Game.save_game()
    Game.scale = 2
    
    while Game.game_state == 'in_game':
        if i:
            Game.visualize_process(algorithm= 'BFS')
            print("BFS")
            # Game.visualize_solution()
            i -= 1
        j += 1
        Game.run()
        if j == 400:
            Game.de_visualize_process()
            Game.de_visualize_solution()
            Game.update_screen()
            Game.visualize_process(algorithm= 'AStar')
            print("AStar")
        if j == 800:    
            Game.de_visualize_process()
            Game.de_visualize_solution()
            Game.update_screen()
            Game.visualize_process(algorithm= 'Dijkstra')
            print("Dijkstra")

        # if j == 200:
        #     Game.de_visualize_process()
        # Game.de_visualize_process()
        # Game.de_visualize_solution()


        pygame.display.update()