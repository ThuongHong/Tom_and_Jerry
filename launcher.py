import pygame
import os
import gc

from game_structure.game_play import GamePlay
from game_structure.game_play import load_GamePlay

from database import data

from menu_objects.button import Button
from menu_objects.graphic import Graphic

from CONSTANTS import DISPLAY
from CONSTANTS import COLOR


def create_img(images_source, image_name):
    image_name = image_name + '.png'
    return pygame.image.load(os.path.join(images_source, image_name)).convert_alpha()

images_source = 'images/UI'

class Launcher():
    def __init__(self, window_screen):
        click_sound = pygame.mixer.Sound(os.path.join('sounds', 'click.ogg'))
        self.window_screen = window_screen

        # self.music_player = MusicController()
        
        box_save_confirm_img = create_img(images_source, 'box_save_confirm')
        box_game_win_img = create_img(images_source, 'box_game_win')
        box_game_lose_img = create_img(images_source, 'box_game_lose')
        box_confirm_overwrite_img = create_img(images_source, 'box_confirm_overwrite')
        self.font = pygame.font.Font('fonts/The Fountain of Wishes Regular.ttf', 50)
        
        button_visualize_process_on_img = create_img(images_source, 'button_visualize_process_on')
        button_visualize_process_off_img = create_img(images_source, 'button_visualize_process_off')
        button_hint_on_img = create_img(images_source, 'button_hint_on')
        button_hint_off_img = create_img(images_source, 'button_hint_off')
        button_algo_astarlist_img = create_img(images_source, 'button_algo_astarlist')
        button_algo_astarheap_img = create_img(images_source, 'button_algo_astarheap')
        button_algo_bfs_img = create_img(images_source, 'button_algo_bfs')
        button_algo_dfs_img = create_img(images_source, 'button_algo_dfs')
        button_algo_gbfs_img = create_img(images_source, 'button_algo_gbfs')
        button_pause_img = create_img(images_source, 'button_pause')
        button_resume_img = create_img(images_source, 'button_resume')
        button_restart_img = create_img(images_source, 'button_restart')
        button_save_img = create_img(images_source, 'button_save')
        button_home_img = create_img(images_source, 'button_home')
        button_yes_img = create_img(images_source, 'button_yes')
        button_no_img = create_img(images_source, 'button_no')
        button_switch_themes_img = create_img(images_source, 'button_switch_themes')
        button_auto_on_img = create_img(images_source, 'button_auto_on')
        button_auto_off_img = create_img(images_source, 'button_auto_off')
        button_box_game_home_img = create_img(images_source, 'button_box_game_home')
        button_box_game_restart_img = create_img(images_source, 'button_box_game_restart')
        button_overwrite_img = create_img(images_source, 'button_overwrite')
        button_cancel_img = create_img(images_source, 'button_cancel')
        
        
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
        self.box_confirm_overwrite = Graphic(DISPLAY.SCREEN_WIDTH * 0.5, DISPLAY.SCREEN_HEIGHT * 0.5, box_confirm_overwrite_img, 0.3)
        box_confirm_overwrite_width = self.box_confirm_overwrite.modified_width
        box_confirm_overwrite_height = self.box_confirm_overwrite.modified_height
        box_confirm_overwrite_x_coord = self.box_confirm_overwrite.x_coord
        box_confirm_overwrite_y_coord = self.box_confirm_overwrite.y_coord
        
        self.button_visualize_process_on = Button(DISPLAY.SCREEN_WIDTH * 0.74, DISPLAY.SCREEN_HEIGHT * 0.92, button_visualize_process_on_img, click_sound, 0.25, 0.26)
        self.button_visualize_process_off = Button(DISPLAY.SCREEN_WIDTH * 0.74, DISPLAY.SCREEN_HEIGHT * 0.92, button_visualize_process_off_img, click_sound, 0.25, 0.26)
        self.button_hint_on = Button(DISPLAY.SCREEN_WIDTH * 0.80, DISPLAY.SCREEN_HEIGHT * 0.92, button_hint_on_img, click_sound, 0.25, 0.26)
        self.button_hint_off = Button(DISPLAY.SCREEN_WIDTH * 0.80, DISPLAY.SCREEN_HEIGHT * 0.92, button_hint_off_img, click_sound, 0.25, 0.26)
        self.button_algo_astarlist = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_astarlist_img, click_sound, 0.25, 0.26)
        self.button_algo_astarheap = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_astarheap_img, click_sound, 0.25, 0.26)
        self.button_algo_bfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_bfs_img, click_sound, 0.25, 0.26)
        self.button_algo_dfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_dfs_img, click_sound, 0.25, 0.26)
        self.button_algo_gbfs = Button(DISPLAY.SCREEN_WIDTH * 0.90, DISPLAY.SCREEN_HEIGHT * 0.92, button_algo_gbfs_img, click_sound, 0.25, 0.26)
        self.button_pause = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.82, button_pause_img, click_sound, 0.25, 0.26)
        self.button_resume = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.82, button_resume_img, click_sound, 0.25, 0.26)
        self.button_auto_on = Button(DISPLAY.SCREEN_WIDTH * 0.87, DISPLAY.SCREEN_HEIGHT * 0.82, button_auto_on_img, click_sound, 0.25, 0.26)
        self.button_auto_off = Button(DISPLAY.SCREEN_WIDTH * 0.87, DISPLAY.SCREEN_HEIGHT * 0.82, button_auto_off_img, click_sound, 0.25, 0.26)
        self.button_restart = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.72, button_restart_img, click_sound, 0.25, 0.26)
        self.button_save_game = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.52, button_save_img, click_sound, 0.25, 0.26)
        self.button_home = Button(DISPLAY.SCREEN_WIDTH * 0.93, DISPLAY.SCREEN_HEIGHT * 0.62, button_home_img, click_sound, 0.25, 0.26)
        self.button_yes = Button(box_save_confirm_x_coord - box_save_confirm_width * 0.2, box_save_confirm_y_coord + box_save_confirm_height * 0.2, button_yes_img, click_sound, 0.25, 0.26)
        self.button_no = Button(box_save_confirm_x_coord + box_save_confirm_width * 0.2, box_save_confirm_y_coord + box_save_confirm_height * 0.2, button_no_img, click_sound, 0.25, 0.26)
        self.button_switch_themes = Button(DISPLAY.SCREEN_WIDTH * 0.65, DISPLAY.SCREEN_HEIGHT * 0.92, button_switch_themes_img, click_sound, 0.25, 0.26)
        self.button_box_game_restart_win = Button(box_game_win_x_coord - box_game_win_width * 0.2, box_game_win_y_coord + box_game_win_height * 0.48, button_box_game_restart_img, click_sound, 0.25, 0.26)
        self.button_box_game_home_win = Button(box_game_win_x_coord + box_game_win_width * 0.2, box_game_win_y_coord + box_game_win_height * 0.48, button_box_game_home_img, click_sound, 0.25, 0.26)
        self.button_box_game_restart_lose = Button(box_game_win_x_coord - box_game_win_width * 0.2, box_game_win_y_coord + box_game_win_height * 0.43, button_box_game_restart_img, click_sound, 0.25, 0.26)
        self.button_box_game_home_lose = Button(box_game_win_x_coord + box_game_win_width * 0.2, box_game_win_y_coord + box_game_win_height * 0.43, button_box_game_home_img, click_sound, 0.25, 0.26)
        self.button_overwrite = Button(box_confirm_overwrite_x_coord - box_confirm_overwrite_width * 0.24, box_confirm_overwrite_y_coord + box_confirm_overwrite_height * 0.24, button_overwrite_img, click_sound, 0.3, 0.31)
        self.button_cancel = Button(box_confirm_overwrite_x_coord + box_confirm_overwrite_width * 0.24, box_confirm_overwrite_y_coord + box_confirm_overwrite_height * 0.24, button_cancel_img, click_sound, 0.3, 0.31)
        
        self.load_background()

    def load_background(self):
        self.background_images = []
        self.num_of_background_images = 12
        for i in range(self.num_of_background_images):
            img = create_img('images/Ingame_background', str(i))
            self.background_images.append(img)
            
        self.background = Graphic(DISPLAY.SCREEN_WIDTH * 0.5, DISPLAY.SCREEN_HEIGHT * 0.5, self.background_images[0], 1)
        
    def draw_ui(self, event=None):
        pos = pygame.mouse.get_pos()
        if self.win == False and self.lose == False:
            if self.paused:
                time_used = self.font.render(f'Time  : {self.time_at_pause}', True, COLOR.WHITE)
            else:
                time_used = self.font.render(f'Time  : {self.Game.format_time(self.Game.get_time)}', True, COLOR.WHITE)
            step_used = self.font.render(f'Steps: {self.Game.Tom.step_moves}', True, COLOR.WHITE)
            self.window_screen.blit(time_used, (DISPLAY.SCREEN_WIDTH * 0.05, DISPLAY.SCREEN_HEIGHT * 0.05))
            self.window_screen.blit(step_used, (DISPLAY.SCREEN_WIDTH * 0.05, DISPLAY.SCREEN_HEIGHT * 0.10))
            
            if self.energy:
                energy_left = self.font.render(f'Energy: {self.Game.Tom.hp}', True, COLOR.WHITE)
                self.window_screen.blit(energy_left, (DISPLAY.SCREEN_WIDTH * 0.05, DISPLAY.SCREEN_HEIGHT * 0.15))
            
            if self.Game.is_stop_process:
                if self.button_visualize_process_off.draw(self.window_screen, pos, event, self.sound_on):
                    self.Game.visualize_process(algorithm=self.current_algo)
                    self.Game.de_visualize_solution()
                    self.Game.de_auto_move()
            else:
                if self.button_visualize_process_on.draw(self.window_screen, pos, event, self.sound_on):
                    self.Game.de_visualize_process()
            
            if not self.Game.is_draw_solution:
                if self.button_hint_off.draw(self.window_screen, pos, event, self.sound_on) and self.Game.is_stop_process:
                    self.Game.visualize_solution(algorithm=self.current_algo)
            else:
                if self.button_hint_on.draw(self.window_screen, pos, event, self.sound_on):
                    self.Game.de_visualize_solution()

            if self.current_algo == 'AStar_OrderedList':
                if self.button_algo_astarlist.draw(self.window_screen, pos, event, self.sound_on):
                    self.current_algo = 'BFS'
                    self.Game.set_solution(algorithm=self.current_algo)
                    if self.Game.is_auto_move: self.Game.solution = None
                    if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
                    if not self.Game.is_stop_process: 
                        self.Game.visualize_process(algorithm=self.current_algo)
                        self.Game.de_visualize_solution()
            elif self.current_algo == 'BFS':
                if self.button_algo_bfs.draw(self.window_screen, pos, event, self.sound_on):
                    self.current_algo = 'DFS'
                    self.Game.set_solution(algorithm=self.current_algo)
                    if self.Game.is_auto_move: self.Game.solution = None
                    if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
                    if not self.Game.is_stop_process: 
                        self.Game.visualize_process(algorithm=self.current_algo)
                        self.Game.de_visualize_solution()
            elif self.current_algo == 'DFS':
                if self.button_algo_dfs.draw(self.window_screen, pos, event, self.sound_on):
                    self.current_algo = 'GBFS'
                    self.Game.set_solution(algorithm=self.current_algo)
                    if self.Game.is_auto_move: self.Game.solution = None
                    if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
                    if not self.Game.is_stop_process: 
                        self.Game.visualize_process(algorithm=self.current_algo)
                        self.Game.de_visualize_solution()
            elif self.current_algo == 'GBFS':
                if self.button_algo_gbfs.draw(self.window_screen, pos, event, self.sound_on):
                    self.current_algo = 'AStar_MinBinaryHeap'
                    self.Game.set_solution(algorithm=self.current_algo)
                    if self.Game.is_auto_move: self.Game.solution = None
                    if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
                    if not self.Game.is_stop_process: 
                        self.Game.visualize_process(algorithm=self.current_algo)
                        self.Game.de_visualize_solution()
            elif self.current_algo == 'AStar_MinBinaryHeap':
                if self.button_algo_astarheap.draw(self.window_screen, pos, event, self.sound_on):
                    self.current_algo = 'AStar_OrderedList'
                    self.Game.set_solution(algorithm=self.current_algo)
                    if self.Game.is_auto_move: self.Game.solution = None
                    if self.Game.is_draw_solution: self.Game.visualize_solution(algorithm=self.current_algo)
                    if not self.Game.is_stop_process: 
                        self.Game.visualize_process(algorithm=self.current_algo)
                        self.Game.de_visualize_solution()
                    
            if self.paused == False:
                if self.button_pause.draw(self.window_screen, pos, event, self.sound_on):
                    self.Game.is_auto_move = False
                    self.paused = True
                    self.time_at_pause = self.Game.format_time(self.Game.pause_time())
                    
            elif self.paused == True:
                if self.button_resume.draw(self.window_screen, pos, event, self.sound_on):
                    self.paused = False
                    self.Game.resume_time()
                if self.button_restart.draw(self.window_screen, pos, event, self.sound_on):
                    """ Restart new maze """
                    self.paused = False
                    self.Game.resume_time()
                    self.Game.set_new_game_state("start")
                if self.user_id is not None and self.button_save_game.draw(self.window_screen, pos, event, self.sound_on):
                    """ Save game """
                    if self.full_save == True:
                        self.overwrite_confirm = True

                    else:
                        self.Game.save_game(self.Game.time_at_pause, self.current_background, int(self.current_theme))
                        self.Game.resume_time()
                        # self.Game.save_game()
                        self.saved = True
                        # Remember to set this to False if player moves after saved
                        self.paused = False
                if self.button_home.draw(self.window_screen, pos, event, self.sound_on):
                    """ Exit to main menu """
                    if self.saved == False and self.user_id is not None:
                        self.save_confirm = True
                    else:
                        self.Game.set_new_game_state("back_menu")
            
            if self.save_confirm == True:
                self.box_save_confirm.draw(self.window_screen)
                if self.button_yes.draw(self.window_screen, pos, event, self.sound_on):
                    """ Save game """
                    if self.full_save == True:
                        self.overwrite_confirm = True
                        self.save_confirm = False
                    else:
                        self.saved = True
                        self.save_confirm = False
                        self.paused = False
                        self.Game.save_game(self.Game.time_at_pause, self.current_background, int(self.current_theme))
                        self.Game.set_new_game_state("back_menu")
                if self.button_no.draw(self.window_screen, pos, event, self.sound_on):
                    """ Exit to main menu """
                    self.save_confirm = False
                    self.paused = False
                    self.Game.set_new_game_state("back_menu")
                    
            if self.overwrite_confirm == True:
                self.box_confirm_overwrite.draw(self.window_screen)
                if self.button_overwrite.draw(self.window_screen, pos, event, self.sound_on):
                    self.Game.save_game(self.Game.time_at_pause, self.current_background, int(self.current_theme))
                    data.remove_game_save(self.first_game_id)
                    self.saved = True
                    # Remember to set this to False if player moves after saved
                    self.paused = False
                    self.save_confirm = False
                    self.overwrite_confirm = False
                if self.button_cancel.draw(self.window_screen, pos, event, self.sound_on):
                    self.paused = False
                    self.save_confirm = False
                    self.overwrite_confirm = False
                    
            if self.button_switch_themes.draw(self.window_screen, pos, event, self.sound_on):
                """ Switch themes"""
                self.current_theme = str(int(self.current_theme) + 1)
                if (self.current_theme == '7'):
                    self.current_theme = '1'
                self.Game.change_theme(self.current_theme)
                
                self.current_background = self.current_background + 1
                if (self.current_background == self.num_of_background_images):
                    self.current_background = 0
                self.background.change_image(self.background_images[self.current_background])
                
            if self.Game.is_auto_move:
                if self.button_auto_on.draw(self.window_screen, pos, event, self.sound_on):
                    self.Game.de_auto_move()
            else:
                if self.button_auto_off.draw(self.window_screen, pos, event, self.sound_on):
                    self.Game.visualize_solution(algorithm=self.current_algo)
                    self.Game.de_visualize_process()
                    self.Game.is_auto_move = True
                    self.paused = False
                    self.Game.solution = None
                    
        
        if self.win == True:
            step_end = self.font.render(f'Steps:        {self.Game.Tom.step_moves}', True, COLOR.BLACK)
            time_end = self.font.render(f'Time  :        {self.Game.format_time(self.Game.end_time)}', True, COLOR.BLACK)
            score = self.font.render(f'Score:        {self.Game.score}', True, COLOR.BLACK)
            self.box_game_win.draw(self.window_screen)
            self.window_screen.blit(step_end, (self.box_game_win.x_coord - self.box_game_win.modified_width * 0.18, self.box_game_win.y_coord - self.box_game_win.modified_height * 0.08))
            self.window_screen.blit(time_end, (self.box_game_win.x_coord - self.box_game_win.modified_width * 0.18, self.box_game_win.y_coord + self.box_game_win.modified_height * 0.09))
            self.window_screen.blit(score, (self.box_game_win.x_coord - self.box_game_win.modified_width * 0.18, self.box_game_win.y_coord + self.box_game_win.modified_height * 0.26))

            if self.button_box_game_home_win.draw(self.window_screen, pos, event, self.sound_on):
                self.save_confirm = False
                self.paused = False
                self.Game.set_new_game_state("back_menu")
            if self.button_box_game_restart_win.draw(self.window_screen, pos, event, self.sound_on):
                self.paused = False
                self.Game.resume_time()
                self.Game.set_new_game_state("start")
                
        if self.lose == True:
            step_end = self.font.render(f'Steps:        {self.Game.Tom.step_moves}', True, COLOR.BLACK)
            time_end = self.font.render(f'Time  :        {self.Game.format_time(self.Game.end_time)}', True, COLOR.BLACK)
            self.box_game_lose.draw(self.window_screen)
            self.window_screen.blit(step_end, (self.box_game_lose.x_coord - self.box_game_lose.modified_width * 0.18, self.box_game_lose.y_coord - self.box_game_win.modified_height * 0.01))
            self.window_screen.blit(time_end, (self.box_game_lose.x_coord - self.box_game_lose.modified_width * 0.18, self.box_game_lose.y_coord + self.box_game_win.modified_height * 0.17))

            if self.button_box_game_home_lose.draw(self.window_screen, pos, event, self.sound_on):
                self.save_confirm = False
                self.paused = False
                self.Game.set_new_game_state("back_menu")
            if self.button_box_game_restart_lose.draw(self.window_screen, pos, event, self.sound_on):
                self.paused = False
                self.Game.resume_time()
                self.Game.set_new_game_state("start")
        
        pygame.display.update()
    
    def load_game(self, game_id, generate_algorithm, is_visualize_generator, background, theme, spawn_mode, sound_on=True, music_on=True):
        self.Game = load_GamePlay(game_id)
        self.current_algo = "AStar_MinBinaryHeap"
        self.current_background = background
        self.background.change_image(self.background_images[self.current_background])
        self.current_theme = str(theme)
        self.Game.change_theme(self.current_theme)
        self.spawning = spawn_mode
        self.maze_visualizer = is_visualize_generator
        self.maze_generate_algo = generate_algorithm
        self.energy = self.Game.energy
        self.insane_mode = self.Game.insane_mode
        
        self.sound_on = sound_on
        self.music_on = music_on
        self.restart()
        self.full_save = False

        self.sound_on = sound_on
        self.is_loaded = True
        
        # For restart game
        self.user_id = self.Game.user_id
        self.maze_size = self.Game.maze_size
        
    def new_game(self, maze_size, 
                     sound_on,
                     music_on,
                     spawning='random', 
                     energy= False,
                     user_id= None,
                     insane_mode: bool = False,
                     maze_visualizer=False,
                     maze_generate_algo="HAK",
                     full_save=False,
                     first_game_id=None):
        
        self.Game = GamePlay(user_id= user_id,
                             maze_size= maze_size,
                             grid_size= 28,
                             scale= 1,
                             window_screen= self.window_screen,
                             energy=energy,
                             insane_mode= insane_mode)
        
        self.restart()
        self.current_algo = "AStar_MinBinaryHeap"
        self.current_theme = '2'
        self.current_background = 0
        self.spawning = spawning
        self.energy = energy
        self.insane_mode = insane_mode
        self.sound_on = sound_on
        self.music_on = music_on
        self.maze_visualizer = maze_visualizer
        self.maze_generate_algo = maze_generate_algo
        self.full_save = full_save
        self.is_loaded = False
        self.first_game_id = first_game_id # for remove first file if it is full storage
        self.Game.create_new_game_id(self.maze_visualizer, self.maze_generate_algo)
        self.background.change_image(self.background_images[self.current_background])
        self.Game.change_theme(self.current_theme)
        
        # For restart game
        self.user_id = user_id
        self.first_game_id = first_game_id
        self.maze_size = maze_size
        
    def restart(self):
        self.time_at_pause = ''
        self.paused = False
        self.saved = False
        self.save_confirm = False
        self.overwrite_confirm = False
        self.win = False
        self.lose = False
        self.Game.de_visualize_solution()
        self.Game.de_visualize_process()
        self.Game.de_auto_move()
        self.Game.scale = 1
        self.Game.frame = 0
        self.Game.solution = None
        if self.Game.Energy_Items:
            self.Game.Energy_Items.remove(self.Game.Energy_Items.sprites())
            del self.Game.energy_lst
            self.Game.energy_lst = []
        # self.Game.change_theme(self.current_theme)
        
        # self.Game.game_normal_view()

    def launch(self):

        if self.is_loaded == True: self.is_loaded = False
        else:
            if self.maze_visualizer:
                self.background.draw(self.window_screen)
                self.Game.generate(algorithm= self.maze_generate_algo, ondraw=self.maze_visualizer, skinset=self.current_theme)
            else:
                self.Game.generate(algorithm= self.maze_generate_algo, ondraw= False, skinset=self.current_theme)
                
            if self.spawning.lower() == 'random': self.Game.spawn_random()
            else: 
                self.Game.select_position_spawn(self)
            
            self.Game.tom_centering()


        while True:
            event = pygame.event.wait(10)
            
            
            self.Game.center_zoom_linear(100)
            
            self.Game.update_ingame(event, self)
            self.Game.get_action(event, self)
            self.draw_ui(event)
            
            
            
            if self.Game.game_state == 'win_game':
                # self.music_player.play_music('win game')
                self.paused = True
                self.win = True
                
            if self.Game.game_state == 'lose_game':
                self.paused = True
                self.lose = True

            if self.Game.game_state == 'back_menu':
                del self.Game
                gc.collect()
                break
            
            if self.Game.game_state == 'start':
                
                self.restart()
                self.launch()
                break
              
        return
