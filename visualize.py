from menu_objects import button
from menu_objects import graphic
from menu_objects import textbox
from menu_objects import saveslot
from menu_objects import music
from data import data
import os
import pygame

from CONSTANTS import COLOR
from CONSTANTS import DISPLAY

SCREEN_WIDTH = DISPLAY.SCREEN_WIDTH
SCREEN_HEIGHT = DISPLAY.SCREEN_HEIGHT
HALF_SCREEN_WIDTH = SCREEN_WIDTH * 0.5
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT * 0.5

def create_img(image_source, image_name):
    image_name = image_name + '.png'
    return pygame.image.load(os.path.join(image_source, image_name)).convert_alpha()

class GameScreen:
    def __init__(self, screen, image_source, sound_source):
        self.screen = screen
        self.image_source = image_source
        self.sound_source = sound_source
        self.running = True
        
        self.game_state = 'main menu'
        self.help_state = False
        self.difficulty = ''
        self.login_signin_state = 'log in'
        self.leaderboard_state = 'easy'
        self.new_game_state = 'choose difficulty'
        self.load_game_state = 'easy'
        self.music = True
        self.sound = True
        self.login = False # do something with login system
        self.skip_login = False
        self.username = ''

        # music and sound player
        self.click_sound_source = pygame.mixer.Sound(os.path.join(sound_source, 'click.ogg'))
        self.music_player = music.MusicController()
        self.music_player.play_music(self.game_state)
        
        """ load button_img and graphic_img for the game """
        """ MAIN MENU """
        button_newgame_img = create_img(self.image_source, 'button_newgame')
        button_loadgame_img = create_img(self.image_source, 'button_loadgame')
        button_leaderboard_img = create_img(self.image_source, 'button_leaderboard')
        button_exit_img = create_img(self.image_source, 'button_exit')
        button_login_signin_img = create_img(self.image_source, 'button_login_signin')
        button_logout_img = create_img(self.image_source, 'button_logout')
        button_sound_on_img = create_img(self.image_source, 'button_sound_on')
        button_sound_off_img = create_img(self.image_source, 'button_sound_off')
        button_music_on_img = create_img(self.image_source, 'button_music_on')
        button_music_off_img = create_img(self.image_source, 'button_music_off')
        button_help_img = create_img(self.image_source, 'button_help')
        button_close_img = create_img(self.image_source, 'button_close')
        background_main_menu_img = create_img(self.image_source, 'background_main_menu')
        game_title_img = create_img(self.image_source, 'game_title')
        main_menu_jerry_img = create_img(self.image_source, 'main_menu_jerry')
        main_menu_tom_img = create_img(self.image_source, 'main_menu_tom')
        game_description_img = create_img(self.image_source, 'game_description')
        
        """ LOGIN SIGNIN """
        button_login_img = create_img(self.image_source, 'button_login')
        button_signin_img = create_img(self.image_source, 'button_signin')
        button_box_login_img = create_img(self.image_source, 'box_login2')
        button_box_signin_img = create_img(self.image_source, 'box_signin2')
        button_back_img = create_img(self.image_source, 'button_back')
        background_login_signin_img = create_img(self.image_source, 'background_login_signin')
        box_login_signin_img = create_img(self.image_source, 'box_login_signin')
        box_login_img = create_img(self.image_source, 'box_login1')
        box_signin_img = create_img(self.image_source, 'box_signin1')


        """ LEADERBOARD """
        button_leaderboard_easy_img = create_img(self.image_source, 'button_leaderboard_easy')
        button_leaderboard_medium_img = create_img(self.image_source, 'button_leaderboard_medium')
        button_leaderboard_hard_img = create_img(self.image_source, 'button_leaderboard_hard')
        background_leaderboard_img = create_img(self.image_source, 'background_leaderboard')
        leaderboard_img = create_img(self.image_source, 'leaderboard')
        leaderboard_easy_img = create_img(self.image_source, 'leaderboard_easy')
        leaderboard_medium_img = create_img(self.image_source, 'leaderboard_medium')
        leaderboard_hard_img = create_img(self.image_source, 'leaderboard_hard')

        """ NEW GAME """
        button_yes_img = create_img(self.image_source, 'button_yes')
        button_no_img = create_img(self.image_source, 'button_no')
        button_easy_img = create_img(self.image_source, 'button_easy')
        button_medium_img = create_img(self.image_source, 'button_medium')
        button_hard_img = create_img(self.image_source, 'button_hard')
        background_new_game_img = create_img(self.image_source, 'background_new_game')
        box_login_confirm_img = create_img(self.image_source, 'box_login_confirm')
        choose_difficulty_img = create_img(self.image_source, 'choose_difficulty')
        mood_easy_img = create_img(self.image_source, 'mood_easy')
        # mood_medium_img = create_img(self.image_source, 'mood_medium')
        # no suitable img
        mood_hard_img = create_img(self.image_source, 'mood_hard')
        # gameplay video
        
        """ LOAD GAME """
        button_save_img = create_img(self.image_source, 'button_save')
        button_load_img = create_img(self.image_source, 'button_load')
        button_delete_img = create_img(self.image_source, 'button_delete')
        background_load_game_img = create_img(self.image_source, 'background_load_game')
        frame_img = create_img(self.image_source, 'frame')
        overlay_img = create_img(self.image_source, 'overlay')
        easy_snapshot_1_img = create_img(self.image_source, 'temp_maze_snapshot')
        
        """ create button and graphic for the game """
        """ MAIN MENU """
                # create graphic
        self.background_main_menu = graphic.Graphic(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, background_main_menu_img, 1.46)
        self.game_title = graphic.Graphic(HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.15, game_title_img, 0.3)
        self.main_menu_jerry = graphic.Graphic(SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.67, main_menu_jerry_img, 0.32)
        self.main_menu_tom = graphic.Graphic(SCREEN_WIDTH * 0.77, SCREEN_HEIGHT * 0.63, main_menu_tom_img, 0.32)
        self.game_description = graphic.Graphic(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, game_description_img, 0.3)
        # game_description_width = self.game_description.modified_width
        game_description_height = self.game_description.modified_height
        
                # create buttons
        self.button_newgame = button.Button(HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.4, button_newgame_img, self.click_sound_source, 0.3, 0.31)
        self.button_loadgame = button.Button(HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.55, button_loadgame_img, self.click_sound_source, 0.3, 0.31)
        self.button_leaderboard = button.Button(HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.7, button_leaderboard_img, self.click_sound_source, 0.3, 0.31)
        self.button_exit = button.Button(HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.85, button_exit_img, self.click_sound_source,  0.3, 0.31)
        self.button_login_signin = button.Button(SCREEN_WIDTH * 0.09, SCREEN_HEIGHT * 0.92, button_login_signin_img, self.click_sound_source, 0.25, 0.26)
        self.button_logout = button.Button(SCREEN_WIDTH * 0.09, SCREEN_HEIGHT * 0.92, button_logout_img, self.click_sound_source, 0.25, 0.26)
        self.button_sound_on = button.Button(SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.92, button_sound_on_img, self.click_sound_source, 0.25, 0.26)
        self.button_sound_off = button.Button(SCREEN_WIDTH * 0.8, SCREEN_HEIGHT * 0.92, button_sound_off_img, self.click_sound_source, 0.25, 0.26)
        self.button_music_on = button.Button(SCREEN_WIDTH * 0.87, SCREEN_HEIGHT * 0.92, button_music_on_img, self.click_sound_source, 0.25, 0.26)
        self.button_music_off = button.Button(SCREEN_WIDTH * 0.87, SCREEN_HEIGHT * 0.92, button_music_off_img, self.click_sound_source, 0.25, 0.26)
        self.button_help = button.Button(SCREEN_WIDTH * 0.73, SCREEN_HEIGHT * 0.92, button_help_img, self.click_sound_source, 0.25, 0.26)
        self.button_close = button.Button(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT + game_description_height * 0.38, button_close_img, self.click_sound_source, 0.3, 0.31)

        
        """ LOGIN SIGNIN """
                # create graphic
        self.background_login_signin = graphic.Graphic(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, background_login_signin_img, 1.46)
        self.box_login_signin = graphic.Graphic(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, box_login_signin_img, 0.3)
        box_width = self.box_login_signin.modified_width
        box_height = self.box_login_signin.modified_height
        self.box_login = graphic.Graphic(HALF_SCREEN_WIDTH - box_width * 0.21, HALF_SCREEN_HEIGHT - box_height * 0.53, box_login_img, 0.3)
        self.box_signin = graphic.Graphic(HALF_SCREEN_WIDTH + box_width * 0.21, HALF_SCREEN_HEIGHT - box_height * 0.53, box_signin_img, 0.3)
        
                # create buttons
        self.button_login = button.Button(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT + box_height * 0.3, button_login_img, self.click_sound_source, 0.3, 0.31)
        self.button_signin = button.Button(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT + box_height * 0.3, button_signin_img, self.click_sound_source, 0.3, 0.31)
        self.button_box_login = button.Button(HALF_SCREEN_WIDTH - box_width * 0.21, HALF_SCREEN_HEIGHT - box_height * 0.53, button_box_login_img, self.click_sound_source, 0.3, 0.31)
        self.button_box_signin = button.Button(HALF_SCREEN_WIDTH + box_width * 0.21, HALF_SCREEN_HEIGHT - box_height * 0.53, button_box_signin_img, self.click_sound_source, 0.3, 0.31)
        self.button_back = button.Button(SCREEN_WIDTH * 0.05, SCREEN_HEIGHT * 0.92, button_back_img, self.click_sound_source, 0.3, 0.31)

                # create login/ signin textbox
        self.username_login_textbox = textbox.TextBox(HALF_SCREEN_WIDTH - box_width * 0.21, HALF_SCREEN_HEIGHT - box_height * 0.33, 300, 50, self.image_source, self.click_sound_source)
        self.password_login_textbox = textbox.TextBox(HALF_SCREEN_WIDTH - box_width * 0.21, HALF_SCREEN_HEIGHT - box_height * 0.02, 300, 50, self.image_source, self.click_sound_source)
        self.username_signin_textbox = textbox.TextBox(HALF_SCREEN_WIDTH - box_width * 0.21, HALF_SCREEN_HEIGHT - box_height * 0.33, 300, 50, self.image_source, self.click_sound_source)
        self.password_signin_textbox = textbox.TextBox(HALF_SCREEN_WIDTH - box_width * 0.21, HALF_SCREEN_HEIGHT - box_height * 0.02, 300, 50, self.image_source, self.click_sound_source)
        
        """ LEADERBOARD """
                # create graphic
        self.background_leaderboard = graphic.Graphic(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, background_leaderboard_img, 1.1)
        self.leaderboard = graphic.Graphic(HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.47, leaderboard_img, 0.3)
        leaderbboard_width = self.leaderboard.modified_width
        leaderbboard_height = self.leaderboard.modified_height
        self.leaderboard_easy = graphic.Graphic(HALF_SCREEN_WIDTH + leaderbboard_width * 0.367, HALF_SCREEN_HEIGHT - leaderbboard_height * 0.12, leaderboard_easy_img, 0.3)
        self.leaderboard_medium = graphic.Graphic(HALF_SCREEN_WIDTH + leaderbboard_width * 0.367, HALF_SCREEN_HEIGHT + leaderbboard_height * 0.1, leaderboard_medium_img, 0.3)
        self.leaderboard_hard = graphic.Graphic(HALF_SCREEN_WIDTH + leaderbboard_width * 0.367, HALF_SCREEN_HEIGHT + leaderbboard_height * 0.32, leaderboard_hard_img, 0.3)
        
                # create buttons
        self.button_leaderboard_easy = button.Button(HALF_SCREEN_WIDTH + leaderbboard_width * 0.367, HALF_SCREEN_HEIGHT - leaderbboard_height * 0.12, button_leaderboard_easy_img, self.click_sound_source, 0.3, 0.31)
        self.button_leaderboard_medium = button.Button(HALF_SCREEN_WIDTH + leaderbboard_width * 0.367, HALF_SCREEN_HEIGHT + leaderbboard_height * 0.1, button_leaderboard_medium_img, self.click_sound_source, 0.3, 0.31)
        self.button_leaderboard_hard = button.Button(HALF_SCREEN_WIDTH + leaderbboard_width * 0.367, HALF_SCREEN_HEIGHT + leaderbboard_height * 0.32, button_leaderboard_hard_img, self.click_sound_source, 0.3, 0.31)

        
        """ NEW GAME"""
                # create graphic
        self.background_new_game = graphic.Graphic(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, background_new_game_img, 1.46)
        self.box_login_confirm = graphic.Graphic(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, box_login_confirm_img, 0.3)
        box_login_confirm_width = self.box_login_confirm.modified_width
        box_login_confirm_height = self.box_login_confirm.modified_height
        self.choose_difficulty = graphic.Graphic(SCREEN_WIDTH * 0.27, SCREEN_HEIGHT * 0.15, choose_difficulty_img, 0.3)
        self.mood_easy = graphic.Graphic(SCREEN_WIDTH * 0.64, SCREEN_HEIGHT * 0.15, mood_easy_img, 0.3)
        # self.mood_medium = graphic.Graphic(800, 10, mood_medium_img, 0.3)
        # no suitable img
        self.mood_hard = graphic.Graphic(SCREEN_WIDTH * 0.64, SCREEN_HEIGHT * 0.15, mood_hard_img, 0.3)
        # gameplay video
        
                # create buttons
        self.button_yes = button.Button(HALF_SCREEN_WIDTH - box_login_confirm_width * 0.2, HALF_SCREEN_HEIGHT + box_login_confirm_height * 0.25, button_yes_img, self.click_sound_source, 0.3, 0.31)
        self.button_no = button.Button(HALF_SCREEN_WIDTH + box_login_confirm_width * 0.2, HALF_SCREEN_HEIGHT + box_login_confirm_height * 0.25, button_no_img, self.click_sound_source, 0.3, 0.31)
        self.button_easy = button.Button(SCREEN_WIDTH * 0.24, SCREEN_HEIGHT * 0.35, button_easy_img, self.click_sound_source, 0.3, 0.31)
        self.button_medium = button.Button(SCREEN_WIDTH * 0.24, SCREEN_HEIGHT * 0.55, button_medium_img, self.click_sound_source, 0.3, 0.31)
        self.button_hard = button.Button(SCREEN_WIDTH * 0.24, SCREEN_HEIGHT * 0.75, button_hard_img, self.click_sound_source, 0.3, 0.31)

        """ LOAD GAME """
                # create graphic
        self.background_load_game = graphic.Graphic(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, background_load_game_img, 1.5)
        self.saveslot_easy_1 = saveslot.SaveSlot(HALF_SCREEN_WIDTH * 0.6, HALF_SCREEN_HEIGHT, frame_img, overlay_img, button_load_img, button_delete_img, self.click_sound_source, 0.4, 0.4)
        self.saveslot_easy_2 = saveslot.SaveSlot(HALF_SCREEN_WIDTH * 1.3, HALF_SCREEN_HEIGHT, frame_img, overlay_img, button_load_img, button_delete_img, self.click_sound_source, 0.4, 0.4)
        self.saveslot_medium_1 = saveslot.SaveSlot(HALF_SCREEN_WIDTH * 0.6, HALF_SCREEN_HEIGHT, frame_img, overlay_img, button_load_img, button_delete_img, self.click_sound_source, 0.4, 0.4)
        self.saveslot_medium_2 = saveslot.SaveSlot(HALF_SCREEN_WIDTH * 1.3, HALF_SCREEN_HEIGHT, frame_img, overlay_img, button_load_img, button_delete_img, self.click_sound_source, 0.4, 0.4)
        self.saveslot_hard_1 = saveslot.SaveSlot(HALF_SCREEN_WIDTH * 0.6, HALF_SCREEN_HEIGHT, frame_img, overlay_img, button_load_img, button_delete_img, self.click_sound_source, 0.4, 0.4)
        self.saveslot_hard_2 = saveslot.SaveSlot(HALF_SCREEN_WIDTH * 1.3, HALF_SCREEN_HEIGHT, frame_img, overlay_img, button_load_img, button_delete_img, self.click_sound_source, 0.4, 0.4)
        self.easy_snapshot_1 = graphic.Graphic(HALF_SCREEN_WIDTH * 0.6, HALF_SCREEN_HEIGHT, easy_snapshot_1_img, 1.5)

                # create buttons
        self.button_easy_load_game = button.Button(HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.15, button_easy_img, self.click_sound_source, 0.3, 0.31)
        self.button_medium_load_game = button.Button(HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.15, button_medium_img, self.click_sound_source, 0.3, 0.31)
        self.button_hard_load_game = button.Button(HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.15, button_hard_img, self.click_sound_source, 0.3, 0.31)
        
        
    def draw_main_menu(self):
        pos = pygame.mouse.get_pos()
        self.background_main_menu.draw(self.screen)
        
        
        if self.help_state == False:
            self.game_title.draw(self.screen)
            self.main_menu_jerry.draw(self.screen)
            self.main_menu_tom.draw(self.screen)
            if self.button_newgame.draw(self.screen, pos, self.sound):
                self.game_state = 'new game'
            if self.button_loadgame.draw(self.screen, pos, self.sound):
                self.game_state = 'load game'
            if self.button_leaderboard.draw(self.screen, pos, self.sound):
                self.game_state = 'leaderboard'
            if self.button_exit.draw(self.screen, pos, self.sound):
                self.running = False
            if self.login == False:
                if self.button_login_signin.draw(self.screen, pos, self.sound):
                    self.game_state = 'login signin'
            else:
                font = pygame.font.SysFont('The Fountain of Wishes Regular', 40)
                greeting = font.render(f'Hello {self.username}', True, (255, 255, 255))
                self.screen.blit(greeting, (SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.9))
                if self.button_logout.draw(self.screen, pos, self.sound):
                    self.username = ''
                    self.login = False
                    self.login_signin_state = 'log in'

            if self.sound == True:
                if self.button_sound_on.draw(self.screen, pos, self.sound):
                    self.sound = False
            else:
                if self.button_sound_off.draw(self.screen, pos, self.sound):
                    self.sound = True
            if self.music == True:
                if self.button_music_on.draw(self.screen, pos, self.sound):
                    self.music_player.pause_music()
                    self.music = False
            else:
                if self.button_music_off.draw(self.screen, pos, self.sound):
                    self.music_player.unpause_music()
                    self.music = True
            if self.button_help.draw(self.screen, pos, self.sound):
                self.help_state = True    
        if self.help_state == True:
            self.game_description.draw(self.screen)
            if self.button_close.draw(self.screen, pos, self.sound):
                self.game_state = 'main menu'
                self.help_state = False
        
    def draw_login_signin(self):
        pos = pygame.mouse.get_pos()
        
        self.background_login_signin.draw(self.screen)
        state = None

        if self.login_signin_state == 'log in':
            if self.button_box_signin.draw(self.screen, pos, self.sound):
                self.login_signin_state = 'sign in'
                self.username_login_textbox.text = ''
                self.password_login_textbox.text = ''
            self.box_login_signin.draw(self.screen)
            self.box_login.draw(self.screen)

            # Draw Textbox
            self.username_login_textbox.draw(self.screen, COLOR.GREY)
            self.username_login_textbox.draw_text(self.screen, COLOR.BLACK, 
                                                  is_password=False, censored=False, activated=False)
            self.password_login_textbox.draw(self.screen, COLOR.GREY)
            self.password_login_textbox.draw_text(self.screen, COLOR.BLACK, 
                                                  is_password=True, censored=True, activated=False)

            # Get input
            state = self.username_login_textbox.get_text(self.screen, 
                                                 self.button_back, self.button_login, sound_on = self.sound)
            state = self.password_login_textbox.get_text(self.screen, 
                                                 self.button_back, self.button_login,
                                                 is_password=True, censored=True, sound_on = self.sound)

            if self.button_login.draw(self.screen, pos, self.sound) or state == 'submit':
                username = self.username_login_textbox.text
                password = self.password_login_textbox.text
                self.login = data.login(username, password)
                if self.login == True:
                    self.username = username
                    self.game_state = 'main menu'
            
        if self.login_signin_state == 'sign in':
            if self.button_box_login.draw(self.screen, pos, self.sound):
                self.login_signin_state = 'log in'
                self.username_signin_textbox.text = ''
                self.password_signin_textbox.text = ''
            self.box_login_signin.draw(self.screen)
            self.box_signin.draw(self.screen)
            
            # Draw Textbox
            self.username_signin_textbox.draw(self.screen, COLOR.GREY)
            self.username_signin_textbox.draw_text(self.screen, COLOR.BLACK, 
                                                   is_password=False, censored=False, activated=False)
            self.password_signin_textbox.draw(self.screen, COLOR.GREY)
            self.password_signin_textbox.draw_text(self.screen, COLOR.BLACK, 
                                                   is_password=True, censored=False, activated=False)

            # Get input
            state = self.username_signin_textbox.get_text(self.screen, 
                                                  self.button_back, self.button_signin, sound_on = self.sound)
            state = self.password_signin_textbox.get_text(self.screen, 
                                                  self.button_back, self.button_signin, 
                                                  is_password=True, censored=True, sound_on = self.sound)

            if self.button_signin.draw(self.screen, pos, self.sound) or state == 'submit':
                new_username = self.username_signin_textbox.text
                new_password = self.password_signin_textbox.text
                if new_username == "" or new_password == "":
                    pass
                else: self.login = data.register(new_username, new_password)
                if self.login == True:
                    self.username = new_username
                    self.game_state = 'main menu'
            
        if self.button_back.draw(self.screen, pos, self.sound) or state == 'back':
            self.game_state = 'main menu'
            self.login_signin_state = 'log in'
            
        if self.game_state == 'main menu':
            self.username_login_textbox.text = ''
            self.username_signin_textbox.text = ''
            self.password_login_textbox.text = ''
            self.password_signin_textbox.text = ''

    def draw_leaderboard(self):
        pos = pygame.mouse.get_pos()
        
        self.background_leaderboard.draw(self.screen)
        if self.leaderboard_state == 'easy':
            if self.button_leaderboard_medium.draw(self.screen, pos, self.sound):
                self.leaderboard_state = 'medium'
            if self.button_leaderboard_hard.draw(self.screen, pos, self.sound):
                self.leaderboard_state = 'hard'
            self.leaderboard.draw(self.screen)
            self.leaderboard_easy.draw(self.screen)
                
        if self.leaderboard_state == 'medium':
            if self.button_leaderboard_easy.draw(self.screen, pos, self.sound):
                self.leaderboard_state = 'easy'
            if self.button_leaderboard_hard.draw(self.screen, pos, self.sound):
                self.leaderboard_state = 'hard'
            self.leaderboard.draw(self.screen)
            self.leaderboard_medium.draw(self.screen)
                
        if self.leaderboard_state == 'hard':
            if self.button_leaderboard_easy.draw(self.screen, pos, self.sound):
                self.leaderboard_state = 'easy'
            if self.button_leaderboard_medium.draw(self.screen, pos, self.sound):
                self.leaderboard_state = 'medium'
            self.leaderboard.draw(self.screen)
            self.leaderboard_hard.draw(self.screen)
        
        if self.button_back.draw(self.screen, pos, self.sound):
            self.game_state = 'main menu'
            self.leaderboard_state = 'easy'
            
    def draw_new_game(self):
        pos = pygame.mouse.get_pos()
       
        self.background_new_game.draw(self.screen)
        if self.skip_login == False and self.login == False:
            self.box_login_confirm.draw(self.screen)
            if self.button_yes.draw(self.screen, pos, self.sound):
                self.game_state = 'login signin'
            if self.button_no.draw(self.screen, pos, self.sound):
                self.skip_login = True
            if self.button_back.draw(self.screen, pos, self.sound):
                    self.game_state = 'main menu'
                    self.skip_login = False
        else:
            if self.new_game_state == 'choose difficulty':
                self.choose_difficulty.draw(self.screen)
                if self.button_easy.image_rect.collidepoint(pos):
                    self.mood_easy.draw(self.screen)
                # if self.button_medium.image_rect.collidepoint(pos):
                #     self.mood_medium.draw(self.screen)
                if self.button_hard.image_rect.collidepoint(pos):
                    self.mood_hard.draw(self.screen)
                    
                if self.button_easy.draw(self.screen, pos, self.sound):
                    pass # do something here
                if self.button_medium.draw(self.screen, pos, self.sound):
                    pass # do something here
                if self.button_hard.draw(self.screen, pos, self.sound):
                    pass # do something here
                if self.button_back.draw(self.screen, pos, self.sound):
                    self.game_state = 'main menu'
                    self.skip_login = False
            
            
    def draw_load_game(self):
        pos = pygame.mouse.get_pos()
        
        self.background_load_game.draw(self.screen)
        if self.load_game_state == 'easy':
            self.easy_snapshot_1.draw(self.screen)
            self.saveslot_easy_1.manage_save(self.screen, pos)
            self.saveslot_easy_2.manage_save(self.screen, pos)
            if self.button_easy_load_game.draw(self.screen, pos, self.sound):
                self.load_game_state = 'medium'
        if self.load_game_state == 'medium':
            self.saveslot_medium_1.manage_save(self.screen, pos)
            self.saveslot_medium_2.manage_save(self.screen, pos)
            if self.button_medium_load_game.draw(self.screen, pos, self.sound):
                self.load_game_state = 'hard'
        if self.load_game_state == 'hard':
            self.saveslot_hard_1.manage_save(self.screen, pos)
            self.saveslot_hard_2.manage_save(self.screen, pos)
            if self.button_hard_load_game.draw(self.screen, pos, self.sound):
                self.load_game_state = 'easy'
        if self.button_back.draw(self.screen, pos, self.sound):
            self.game_state = 'main menu'
            self.music_player.play_music(self.game_state)
            self.skip_login = False