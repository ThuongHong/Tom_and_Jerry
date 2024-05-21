from game_structure.maze import Maze
from game_structure.character import Tom
from game_structure.game import GamePlay, load_GamePlay
import pygame
import time
import os
from menu_objects.button import Button
from menu_objects.graphic import Graphic

from CONSTANTS import DISPLAY

def create_img(image_source, image_name):
    image_name = image_name + '.png'
    return pygame.image.load(os.path.join(image_source, image_name)).convert_alpha()

images_source = 'images/UI'

class Launcher():
    def __init__(self, window_screen):
        self.window_screen = window_screen
        self.paused = False
        self.saved = False
        self.save_confirm = False

        self.box_save_confirm_img = create_img(images_source, 'box_save_confirm')
        self.font = pygame.font.Font('fonts/The Fountain of Wishes Regular.ttf', 30)
        
        self.button_theme_img = create_img(images_source, 'button_hint_on')
        self.button_hint_on_img = create_img(images_source, 'button_hint_on')
        self.button_hint_off_img = create_img(images_source, 'button_hint_off')
        self.button_algo_astarlist_img = create_img(images_source, 'button_algo_astarlist')
        self.button_algo_astarheap_img = create_img(images_source, 'button_algo_astarheap')
        self.button_algo_bfs_img = create_img(images_source, 'button_algo_bfs')
        self.button_algo_dfs_img = create_img(images_source, 'button_algo_dfs')
        self.button_algo_gbfs_img = create_img(images_source, 'button_algo_gbfs')
        self.button_pause_game_img = create_img(images_source, 'button_pause_game')
        self.button_resume_img = create_img(images_source, 'button_play')
        self.button_restart_img = create_img(images_source, 'button_restart')
        self.button_save_img = create_img(images_source, 'button_save')
        self.button_home_img = create_img(images_source, 'button_home')
        self.button_yes_img = create_img(images_source, 'button_yes')
        self.button_no_img = create_img(images_source, 'button_no')
        self.button_switch_themes_img = create_img(images_source, 'button_switch_themes')

        self.box_save_confirm = Graphic(DISPLAY.SCREEN_WIDTH * 0.5, DISPLAY.SCREEN_HEIGHT * 0.5, self.box_save_confirm_img, 0.3)
        box_save_confirm_width = self.box_save_confirm.modified_width
        box_save_confirm_height = self.box_save_confirm.modified_height
        box_save_confirm_x_coord = self.box_save_confirm.x_coord
        box_save_confirm_y_coord = self.box_save_confirm.y_coord
        

        self.button_hint_on = Button(DISPLAY.SCREEN_WIDTH * 0.81, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_hint_on_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_hint_off = Button(DISPLAY.SCREEN_WIDTH * 0.81, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_hint_off_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_astarlist = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_algo_astarlist_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_astarheap = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_algo_astarheap_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_bfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_algo_bfs_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_dfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_algo_dfs_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_gbfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_algo_gbfs_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_pause_game = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.82, self.button_pause_game_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_resume = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.82, self.button_resume_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_restart = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.72, self.button_restart_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_save_game = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.62, self.button_save_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_home = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.52, self.button_home_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_yes = Button(box_save_confirm_x_coord - box_save_confirm_width * 0.2, box_save_confirm_y_coord + box_save_confirm_height * 0.2, self.button_yes_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_no = Button(box_save_confirm_x_coord + box_save_confirm_width * 0.2, box_save_confirm_y_coord + box_save_confirm_height * 0.2, self.button_no_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_switch_themes = Button(DISPLAY.SCREEN_WIDTH * 0.75, DISPLAY.SCREEN_HEIGHT * 0.92, self.button_switch_themes_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        
    def draw_ui(self):
        pos = pygame.mouse.get_pos()
        
        time_used = self.font.render(f'Time: {self.Game.get_time}', True, (255, 255, 255))
        step_used = self.font.render(f'Steps: {self.Game.Tom.step_moves}', True, (255, 255, 255))
        self.window_screen.blit(time_used, (DISPLAY.SCREEN_WIDTH * 0.05, DISPLAY.SCREEN_HEIGHT * 0.05))
        self.window_screen.blit(step_used, (DISPLAY.SCREEN_WIDTH * 0.05, DISPLAY.SCREEN_HEIGHT * 0.10))
        if self.energy:
            energy_left = self.font.render(f'Energy: {self.Game.Tom.hp}', True, (255, 255, 255))
            self.window_screen.blit(energy_left, (DISPLAY.SCREEN_WIDTH * 0.05, DISPLAY.SCREEN_HEIGHT * 0.15))
        
        if not self.Game.is_draw_solution:
            if self.button_hint_off.draw_lite(self.window_screen, pos, False):
                self.Game.visualize_solution(algorithm=self.current_algo)
        else:
            if self.button_hint_on.draw_lite(self.window_screen, pos, False):
                self.Game.de_visualize_solution()

        if self.current_algo == 'AStar_OrderedList':
            if self.button_algo_astarlist.draw_lite(self.window_screen, pos, False):
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
                self.current_algo = 'AStar_MinBinaryHeap'
                if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
        elif self.current_algo == 'AStar_MinBinaryHeap':
            if self.button_algo_astarheap.draw_lite(self.window_screen, pos, False):
                self.current_algo = 'AStar_OrderedList'
                if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
                
        if self.paused == False:
            if self.button_pause_game.draw_lite(self.window_screen, pos, False):
                self.paused = True
        elif self.paused == True:
            if self.button_resume.draw_lite(self.window_screen, pos, False):
                self.paused = False
            if self.button_restart.draw_lite(self.window_screen, pos, False):
                """ Restart new maze """
                self.paused = False
                self.Game.set_new_game_state("start")
            if self.button_save_game.draw_lite(self.window_screen, pos, False):
                """ Save game """
                self.saved = True
                # Remember to set this to False if player moves after saved
                self.paused = False
                # self.Game.set_new_game_state("save_game")
                # self.Game.save_game()
                #            ^
                # Check this |
            if self.button_home.draw_lite(self.window_screen, pos, False):
                """ Exit to main menu """
                if self.saved == False:
                    self.save_confirm = True
                else:
                    pass
                    #            ^
                    # Check this |
        
        if self.save_confirm == True:
            self.box_save_confirm.draw(self.window_screen)
            if self.button_yes.draw_lite(self.window_screen, pos, False):
                """ Save game """
                self.save_confirm = False
                self.paused = False
                # self.Game.save_game()
                #            ^
                # Check this |
            if self.button_no.draw_lite(self.window_screen, pos, False):
                """ Exit to main menu"""
                self.save_confirm = False
                self.paused = False
                #            ^
                # Check this |
                
        if self.button_switch_themes.draw_lite(self.window_screen, pos, False):
            """ Switch themes"""
            self.current_theme = str(int(self.current_theme) + 1)
            if (self.current_theme == '6'):
                self.current_theme = '2'
            self.Game.change_theme(self.current_theme)
                
            
                

    def reset(self, maze_size, 
              start_coord_screen=(0, 0), end_coord_screen=(500, 500), 
              spawning='random', 
              energy= False,
              user_id= None,
              insane_mode: bool = False):
        self.Game = GamePlay(user_id= user_id,
                             maze_size= maze_size,
                             grid_size= 28,
                             start_coord_screen= start_coord_screen,
                             end_coord_screen= end_coord_screen,
                             scale= 1,
                             window_screen= self.window_screen,
                             energy=energy,
                             insane_mode= insane_mode)
        self.spawning = spawning
        self.current_algo = "AStar_MinBinaryHeap"
        self.current_theme = '2'
        self.energy = energy

    def launch(self):
        self.Game.generate(algorithm= 'HAK', ondraw= False)
        # Game.select_position_spawn()
        if self.spawning == 'random': self.Game.spawn_random()
        else: self.Game.select_position_spawn()
        self.Game.game_centering()

        while self.Game.game_state == 'in_game':
            
            self.Game.center_zoom_linear(100)
            self.Game.run(self, self.paused)
            self.draw_ui()

            pygame.display.update()