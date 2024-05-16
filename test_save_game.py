from game_structure.maze import Maze
from game_structure.character import Tom
from game_structure.game import GamePlay, load_GamePlay
import pygame
import time
import os
from menu_objects.button import Button

from CONSTANTS import DISPLAY

def create_img(image_source, image_name):
    image_name = image_name + '.png'
    return pygame.image.load(os.path.join(image_source, image_name)).convert_alpha()

if __name__ == '__main__':
    pygame.init()

 

    screen = pygame.display.set_mode((DISPLAY.SCREEN_WIDTH, DISPLAY.SCREEN_HEIGHT))
    screen.fill((0, 0, 0))
    clock = pygame.time.Clock()

    Game = GamePlay(maze_size= 20,
                    grid_size= 28,
                    start_coord_screen= (0, 0),
                    end_coord_screen= (500, 500),
                    scale= 1,
                    window_screen= screen)
    Game.generate(algorithm= 'HAK', ondraw= False)
    Game.spawn_random()
    Game.game_centering()
    # pygame.time.wait(1000)
    i = 0
    j = 0 
    # Game.visualize_process('GBFS')

    button_hint_on_img = create_img('images', 'button_hint_on')
    button_hint_off_img = create_img('images', 'button_hint_off')
    button_algo_astar_img = create_img('images', 'button_algo_astar')
    button_algo_bfs_img = create_img('images', 'button_algo_bfs')
    button_algo_dfs_img = create_img('images', 'button_algo_dfs')
    button_algo_dijkstra_img = create_img('images', 'button_algo_dijkstra')
    button_algo_gbfs_img = create_img('images', 'button_algo_gbfs')

    button_hint_on = Button(DISPLAY.SCREEN_WIDTH * 0.8, DISPLAY.SCREEN_HEIGHT * 0.92, button_hint_on_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
    button_hint_off = Button(DISPLAY.SCREEN_WIDTH * 0.8, DISPLAY.SCREEN_HEIGHT * 0.92, button_hint_off_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
    button_algo_astar = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_astar_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
    button_algo_bfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_bfs_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
    button_algo_dfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_dfs_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
    button_algo_dijkstra = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_dijkstra_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
    button_algo_gbfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_gbfs_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)

    current_algo = 'AStar'
    while Game.game_state == 'in_game':
        # if Game.is_draw_solution:
        #     if button_hint_on.draw(screen, pygame.mouse.get_pos(), False):
        #         Game.visualize_solution()
        # else:
        #     if button_hint_off.draw(screen, pygame.mouse.get_pos(), False):
        #         Game.de_visualize_solution()
        Game.center_zoom_linear(100)
        Game.run()
        i += 1
        pos = pygame.mouse.get_pos()
        if not Game.is_draw_solution:
            if button_hint_off.draw_lite(screen, pos, False):
                Game.visualize_solution(algorithm=current_algo)
        else:
            if button_hint_on.draw_lite(screen, pos, False):
                Game.de_visualize_solution()

        if current_algo == 'AStar':
            if button_algo_astar.draw_lite(screen, pos, False):
                current_algo = 'BFS'
                if Game.is_draw_solution: Game.visualize_solution(algorithm=current_algo)
        elif current_algo == 'BFS':
            if button_algo_bfs.draw_lite(screen, pos, False):
                current_algo = 'DFS'
                if Game.is_draw_solution: Game.visualize_solution(algorithm=current_algo)
        elif current_algo == 'DFS':
            if button_algo_dfs.draw_lite(screen, pos, False):
                current_algo = 'GBFS'
                if Game.is_draw_solution: Game.visualize_solution(algorithm=current_algo)
        elif current_algo == 'GBFS':
            if button_algo_gbfs.draw_lite(screen, pos, False):
                current_algo = 'AStar'
                if Game.is_draw_solution: Game.visualize_solution(algorithm=current_algo)
        
        # if i == 50:
        #     Game.de_visualize_process()
        #     Game.visualize_process('DFS')
        #     Game.game_normal_view()


        pygame.display.update()