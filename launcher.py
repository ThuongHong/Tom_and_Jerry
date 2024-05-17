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

class Launcher():
    def __init__(self, window_screen):
        self.window_screen = window_screen

        self.button_hint_on_img = create_img('images', 'button_hint_on')
        self.button_hint_off_img = create_img('images', 'button_hint_off')
        self.button_algo_astar_img = create_img('images', 'button_algo_astar')
        self.button_algo_bfs_img = create_img('images', 'button_algo_bfs')
        self.button_algo_dfs_img = create_img('images', 'button_algo_dfs')
        self.button_algo_dijkstra_img = create_img('images', 'button_algo_dijkstra')
        self.button_algo_gbfs_img = create_img('images', 'button_algo_gbfs')

        self.button_hint_on = Button(DISPLAY.SCREEN_WIDTH * 0.8, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_hint_on_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_hint_off = Button(DISPLAY.SCREEN_WIDTH * 0.8, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_hint_off_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_astar = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_algo_astar_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_bfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_algo_bfs_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_dfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_algo_dfs_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_dijkstra = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_algo_dijkstra_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_gbfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_algo_gbfs_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)

    def draw_ui(self):
        pos = pygame.mouse.get_pos()
        if not self.Game.is_draw_solution:
            if self.button_hint_off.draw_lite(self.window_screen, pos, False):
                self.Game.visualize_solution(algorithm=self.current_algo)
        else:
            if self.button_hint_on.draw_lite(self.window_screen, pos, False):
                self.Game.de_visualize_solution()

        if self.current_algo == 'AStar_OrderedList':
            if self.button_algo_astar.draw_lite(self.window_screen, pos, False):
                self.current_algo = 'BFS'
                if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
        elif self.current_algo == 'BFS':
            if self.button_algo_bfs.draw_lite(self.window_screen, pos, False):
                self.current_algo = 'DFS'
                if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
        elif self.current_algo == 'DFS':
            if self.button_algo_dfs.draw_lite(self.window_screen, pos, False):
                self.current_algo = 'GBFS'
                if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
        elif self.current_algo == 'GBFS':
            if self.button_algo_gbfs.draw_lite(self.window_screen, pos, False):
                self.current_algo = 'AStar_OrderedList'
                if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)

    def reset(self, maze_size, start_coord_screen=(0, 0), end_coord_screen=(500, 500)):
        self.Game = GamePlay(maze_size= maze_size,
                             grid_size= 28,
                             start_coord_screen= start_coord_screen,
                             end_coord_screen= end_coord_screen,
                             scale= 1,
                             window_screen= self.window_screen)
        self.current_algo = "BFS"

    def launch(self):
        self.Game.generate(algorithm= 'HAK', ondraw= False)
        # Game.select_position_spawn()
        self.Game.spawn_random()
        self.Game.game_centering()

        while self.Game.game_state == 'in_game':
            self.Game.center_zoom_linear(100)
            self.Game.run()
            self.draw_ui()

            pygame.display.update()