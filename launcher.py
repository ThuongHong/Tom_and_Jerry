from game_structure.maze import Maze
from game_structure.character import Tom
from game_structure.game import GamePlay, load_GamePlay
import pygame
import time
import os
from menu_objects.button import Button
from menu_objects.graphic import Graphic

from CONSTANTS import DISPLAY

def create_img(images_source, image_name):
    image_name = image_name + '.png'
    return pygame.image.load(os.path.join(images_source, image_name)).convert_alpha()

images_source = 'images/UI'

class Launcher():
    def __init__(self, window_screen):
        self.window_screen = window_screen

        box_save_confirm_img = create_img(images_source, 'box_save_confirm')
        box_game_win_img = create_img(images_source, 'box_game_win')
        box_game_lose_img = create_img(images_source, 'box_game_lose')
        self.font = pygame.font.Font('fonts/The Fountain of Wishes Regular.ttf', 30)
        self.end_font = pygame.font.Font('fonts/The Fountain of Wishes Regular.ttf', 50)
        
        button_hint_on_img = create_img(images_source, 'button_hint_on')
        button_hint_off_img = create_img(images_source, 'button_hint_off')
        button_algo_astarlist_img = create_img(images_source, 'button_algo_astarlist')
        button_algo_astarheap_img = create_img(images_source, 'button_algo_astarheap')
        button_algo_bfs_img = create_img(images_source, 'button_algo_bfs')
        button_algo_dfs_img = create_img(images_source, 'button_algo_dfs')
        button_algo_gbfs_img = create_img(images_source, 'button_algo_gbfs')
        button_pause_game_img = create_img(images_source, 'button_pause_game')
        button_resume_img = create_img(images_source, 'button_play')
        button_restart_img = create_img(images_source, 'button_restart')
        button_save_img = create_img(images_source, 'button_save')
        button_home_img = create_img(images_source, 'button_home')
        button_yes_img = create_img(images_source, 'button_yes')
        button_no_img = create_img(images_source, 'button_no')
        button_switch_themes_img = create_img(images_source, 'button_switch_themes')
        button_box_game_home_img = create_img(images_source, 'button_box_game_home')
        button_box_game_restart_img = create_img(images_source, 'button_box_game_restart')
        
        
        self.box_save_confirm = Graphic(DISPLAY.SCREEN_WIDTH * 0.5, DISPLAY.SCREEN_HEIGHT * 0.5, box_save_confirm_img, 0.3)
        box_save_confirm_width = self.box_save_confirm.modified_width
        box_save_confirm_height = self.box_save_confirm.modified_height
        box_save_confirm_x_coord = self.box_save_confirm.x_coord
        box_save_confirm_y_coord = self.box_save_confirm.y_coord
        self.box_game_win = Graphic(DISPLAY.SCREEN_WIDTH * 0.5, DISPLAY.SCREEN_HEIGHT * 0.5, box_game_win_img, 0.3)
        box_game_win_width = self.box_game_win.modified_width
        box_game_win_height = self.box_game_win.modified_height
        box_game_win_x_coord = self.box_game_win.x_coord
        box_game_win_y_coord = self.box_game_win.y_coord
        self.box_game_lose = Graphic(DISPLAY.SCREEN_WIDTH * 0.5, DISPLAY.SCREEN_HEIGHT * 0.5, box_game_lose_img, 0.3)
        

        self.button_hint_on = Button(DISPLAY.SCREEN_WIDTH * 0.81, DISPLAY.SCREEN_HEIGHT * 0.92, button_hint_on_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_hint_off = Button(DISPLAY.SCREEN_WIDTH * 0.81, DISPLAY.SCREEN_HEIGHT * 0.92, button_hint_off_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_astarlist = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_astarlist_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_astarheap = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_astarheap_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_bfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_bfs_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_dfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_dfs_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_algo_gbfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_gbfs_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_pause_game = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.82, button_pause_game_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_resume = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.82, button_resume_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_restart = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.72, button_restart_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_save_game = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.52, button_save_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_home = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.62, button_home_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_yes = Button(box_save_confirm_x_coord - box_save_confirm_width * 0.2, box_save_confirm_y_coord + box_save_confirm_height * 0.2, button_yes_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_no = Button(box_save_confirm_x_coord + box_save_confirm_width * 0.2, box_save_confirm_y_coord + box_save_confirm_height * 0.2, button_no_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_switch_themes = Button(DISPLAY.SCREEN_WIDTH * 0.75, DISPLAY.SCREEN_HEIGHT * 0.92, button_switch_themes_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_box_game_restart = Button(box_game_win_x_coord - box_game_win_width * 0.2, box_game_win_y_coord + box_game_win_height * 0.48, button_box_game_restart_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        self.button_box_game_home = Button(box_game_win_x_coord + box_game_win_width * 0.2, box_game_win_y_coord + box_game_win_height * 0.48, button_box_game_home_img, pygame.mixer.Sound(os.path.join('sounds', 'click.ogg')), 0.25, 0.26)
        
        self.load_background()

    def load_background(self):
        self.background_images = []
        num_of_images = 4
        for i in range(num_of_images):
            img = create_img('images/Ingame_background', str(i))
            self.background_images.append(img)
            
        self.background = Graphic(DISPLAY.SCREEN_WIDTH * 0.5, DISPLAY.SCREEN_HEIGHT * 0.5, self.background_images[0], 1)
        self.current_background = 0
        
    def draw_ui(self):
        pos = pygame.mouse.get_pos()
        if self.win == False and self.lose == False:
            if self.paused:
                time_used = self.font.render(f'Time  : {self.time_at_pause}', True, (255, 255, 255))
            else:
                time_used = self.font.render(f'Time  : {self.Game.get_time}', True, (255, 255, 255))
            step_used = self.font.render(f'Steps: {self.Game.Tom.step_moves}', True, (255, 255, 255))
            self.window_screen.blit(time_used, (DISPLAY.SCREEN_WIDTH * 0.05, DISPLAY.SCREEN_HEIGHT * 0.05))
            self.window_screen.blit(step_used, (DISPLAY.SCREEN_WIDTH * 0.05, DISPLAY.SCREEN_HEIGHT * 0.10))
            
            if self.energy:
                energy_left = self.font.render(f'Energy: {self.Game.Tom.hp}', True, (255, 255, 255))
                self.window_screen.blit(energy_left, (DISPLAY.SCREEN_WIDTH * 0.05, DISPLAY.SCREEN_HEIGHT * 0.15))
            
            if not self.Game.is_draw_solution:
                if self.button_hint_off.draw_lite(self.window_screen, pos, self.sound_on):
                    self.Game.visualize_solution(algorithm=self.current_algo)
            else:
                if self.button_hint_on.draw_lite(self.window_screen, pos, self.sound_on):
                    self.Game.de_visualize_solution()

            if self.current_algo == 'AStar_OrderedList':
                if self.button_algo_astarlist.draw_lite(self.window_screen, pos, self.sound_on):
                    self.current_algo = 'BFS'
                    if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
            elif self.current_algo == 'BFS':
                if self.button_algo_bfs.draw_lite(self.window_screen, pos, self.sound_on):
                    self.current_algo = 'DFS'
                    if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
            elif self.current_algo == 'DFS':
                if self.button_algo_dfs.draw_lite(self.window_screen, pos, self.sound_on):
                    self.current_algo = 'GBFS'
                    if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
            elif self.current_algo == 'GBFS':
                if self.button_algo_gbfs.draw_lite(self.window_screen, pos, self.sound_on):
                    self.current_algo = 'AStar_MinBinaryHeap'
                    if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
            elif self.current_algo == 'AStar_MinBinaryHeap':
                if self.button_algo_astarheap.draw_lite(self.window_screen, pos, self.sound_on):
                    self.current_algo = 'AStar_OrderedList'
                    if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
                    
            if self.paused == False:
                if self.button_pause_game.draw_lite(self.window_screen, pos, self.sound_on):
                    self.paused = True
                    self.time_at_pause = self.Game.pause_time()
                    
            elif self.paused == True:
                if self.button_resume.draw_lite(self.window_screen, pos, self.sound_on):
                    self.paused = False
                    self.Game.resume_time()
                if self.button_restart.draw_lite(self.window_screen, pos, self.sound_on):
                    """ Restart new maze """
                    self.paused = False
                    self.Game.resume_time()
                    self.Game.set_new_game_state("start")
                if self.former_user_id is not None and self.button_save_game.draw_lite(self.window_screen, pos, self.sound_on):
                    """ Save game """
                    self.saved = True
                    # Remember to set this to False if player moves after saved
                    self.paused = False
                    # self.Game.set_new_game_state("save_game")
                    self.Game.save_game()
                    #            ^
                    # Check this |
                if self.button_home.draw_lite(self.window_screen, pos, self.sound_on):
                    """ Exit to main menu """
                    if self.saved == False and self.former_user_id is not None:
                        self.save_confirm = True
                    else:
                        self.Game.set_new_game_state("back_menu")
                        #            ^
                        # Check this |
            
            if self.save_confirm == True:
                self.box_save_confirm.draw(self.window_screen)
                if self.button_yes.draw_lite(self.window_screen, pos, self.sound_on):
                    """ Save game """
                    self.save_confirm = False
                    self.paused = False
                    self.Game.save_game()
                    self.Game.set_new_game_state("back_menu")
                    # self.Game.save_game()
                    #            ^
                    # Check this |
                if self.button_no.draw_lite(self.window_screen, pos, self.sound_on):
                    """ Exit to main menu"""
                    self.save_confirm = False
                    self.paused = False
                    self.Game.set_new_game_state("back_menu")
                    #            ^
                    # Check this |
                    
            if self.button_switch_themes.draw_lite(self.window_screen, pos, self.sound_on):
                """ Switch themes"""
                self.current_theme = str(int(self.current_theme) + 1)
                if (self.current_theme == '8'):
                    self.current_theme = '1'
                self.Game.change_theme(self.current_theme)
                
                self.current_background = self.current_background + 1
                if (self.current_background == 4):
                    self.current_background = 0
                self.background.change_image(self.background_images[self.current_background])
                
        
        if self.win == True:
            time_end = self.end_font.render(f'Time  :        {self.Game.end_time}', True, (0, 0, 0))
            step_end = self.end_font.render(f'Steps:        {self.Game.Tom.step_moves}', True, (0, 0, 0))
            self.box_game_win.draw(self.window_screen)
            self.window_screen.blit(time_end, (self.box_game_win.x_coord - self.box_game_win.modified_width * 0.18, self.box_game_win.y_coord - self.box_game_win.modified_height * 0.01))
            self.window_screen.blit(step_end, (self.box_game_win.x_coord - self.box_game_win.modified_width * 0.18, self.box_game_win.y_coord + self.box_game_win.modified_height * 0.2))

            if self.button_box_game_home.draw_lite(self.window_screen, pos, self.sound_on):
                self.save_confirm = False
                self.paused = False
                self.Game.set_new_game_state("back_menu")
            if self.button_box_game_restart.draw_lite(self.window_screen, pos, self.sound_on):
                self.paused = False
                self.Game.resume_time()
                self.Game.set_new_game_state("start")
                
        if self.lose == True:
            time_end = self.end_font.render(f'Time  :        {self.Game.end_time}', True, (0, 0, 0))
            step_end = self.end_font.render(f'Steps:        {self.Game.Tom.step_moves}', True, (0, 0, 0))
            self.box_game_lose.draw(self.window_screen)
            self.window_screen.blit(time_end, (self.box_game_lose.x_coord - self.box_game_lose.modified_width * 0.18, self.box_game_lose.y_coord - self.box_game_win.modified_height * 0.01))
            self.window_screen.blit(step_end, (self.box_game_lose.x_coord - self.box_game_lose.modified_width * 0.18, self.box_game_lose.y_coord + self.box_game_win.modified_height * 0.2))

            if self.button_box_game_home.draw_lite(self.window_screen, pos, self.sound_on):
                self.save_confirm = False
                self.paused = False
                self.Game.set_new_game_state("back_menu")
            if self.button_box_game_restart.draw_lite(self.window_screen, pos, self.sound_on):
                self.paused = False
                self.Game.resume_time()
                self.Game.set_new_game_state("start")
        
        pygame.display.update()
        
    def init_setting(self, maze_size, 
                     sound_on,
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
        
        self.current_algo = "AStar_MinBinaryHeap"
        self.current_theme = '2'
        self.spawning = spawning
        self.energy = energy
        self.insane_mode = insane_mode
        self.time_at_pause = ''
        self.paused = False
        self.saved = False
        self.save_confirm = False
        self.win = False
        self.lose = False
        self.is_restared = False
        self.sound_on = sound_on
        
        # For restart game
        self.former_user_id = user_id
        self.former_maze_size = maze_size
        self.former_start_coord_screen = start_coord_screen
        self.former_end_coord_screen = end_coord_screen
        
    def restart(self):
        self.Game = GamePlay(user_id= self.former_user_id,
                             maze_size= self.former_maze_size,
                             grid_size= 28,
                             start_coord_screen= self.former_start_coord_screen,
                             end_coord_screen= self.former_end_coord_screen,
                             scale= 1,
                             window_screen= self.window_screen,
                             energy=self.energy,
                             insane_mode= self.insane_mode)
        self.paused = False
        self.saved = False
        self.save_confirm = False
        self.win = False
        self.lose = False

    def launch(self):
        if self.is_restared: 
            self.restart()
            self.is_restared = False
        self.Game.generate(algorithm= 'HAK', ondraw= False)
        # Game.select_position_spawn()
        if self.spawning == 'random': self.Game.spawn_random()
        else: self.Game.select_position_spawn(self)
        self.Game.game_centering()

        while True:
            
            self.Game.center_zoom_linear(100)
            # if self.Game.game_state == 'in_game':
            self.Game.run(self)
            self.draw_ui()
            
            
            if self.Game.game_state == 'win_game':
                self.win = True
                
            if self.Game.game_state == 'lose_game':
                self.lose = True

            if self.Game.game_state == 'back_menu':
                break
            
            if self.Game.game_state == 'start':
                self.is_restared = True
                self.launch()
                break
              
        return