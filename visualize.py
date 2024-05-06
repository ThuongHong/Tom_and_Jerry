from menu_objects import button
from menu_objects import graphic
from menu_objects import textbox
from data import data
import os
import pygame
from constants.INTERFACE_CONSTANTS import COLOR

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
        self.music = True
        self.sound = True
        self.login = False # do something with login system
        self.skip_login = False
        self.username = ''
        self.login_signin = 'log in'
        self.leaderboard = 'easy'
        self.click_sound_source = pygame.mixer.Sound(os.path.join(sound_source, 'click.ogg'))
        
        # load button_img and graphic_img for the game
            # main_menu
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
        background_img = create_img(self.image_source, 'background1')
        game_title_img = create_img(self.image_source, 'game_title')
        main_menu_jerry_img = create_img(self.image_source, 'main_menu_jerry')
        main_menu_tom_img = create_img(self.image_source, 'main_menu_tom')
        
            # login_signin
        button_login_img = create_img(self.image_source, 'button_login')
        button_signin_img = create_img(self.image_source, 'button_signin')
        button_box_login_img = create_img(self.image_source, 'box_login2')
        button_box_signin_img = create_img(self.image_source, 'box_signin2')
        button_back_img = create_img(self.image_source, 'button_back')
        box_login_img = create_img(self.image_source, 'box_login1')
        box_signin_img = create_img(self.image_source, 'box_signin1')

            # leaderboard
        button_leaderboard_easy_img = create_img(self.image_source, 'button_leaderboard_easy')
        button_leaderboard_medium_img = create_img(self.image_source, 'button_leaderboard_medium')
        button_leaderboard_hard_img = create_img(self.image_source, 'button_leaderboard_hard')
        button_back_img = create_img(self.image_source, 'button_back')
        leaderboard_easy_img = create_img(self.image_source, 'leaderboard_easy')
        leaderboard_medium_img = create_img(self.image_source, 'leaderboard_medium')
        leaderboard_hard_img = create_img(self.image_source, 'leaderboard_hard')
                        
            # new_game
        button_yes_img = create_img(self.image_source, 'button_yes')
        button_no_img = create_img(self.image_source, 'button_no')
        button_easy_img = create_img(self.image_source, 'button_easy')
        button_medium_img = create_img(self.image_source, 'button_medium')
        button_hard_img = create_img(self.image_source, 'button_hard')
        button_back_img = create_img(self.image_source, 'button_back')
        box_login_confirm_img = create_img(self.image_source, 'box_login_confirm')
        choose_difficulty_img = create_img(self.image_source, 'choose_difficulty')
        mood_easy_img = create_img(self.image_source, 'mood_easy')
        # mood_medium_img = create_img(self.image_source, 'mood_medium')
        # no suitable img
        mood_hard_img = create_img(self.image_source, 'mood_hard')
        # gameplay video
        
        # create button and graphic for the game
            # main menu
                # create buttons
        self.button_newgame = button.Button(545, 280, button_newgame_img, self.click_sound_source, 0.3, 0.31)
        self.button_loadgame = button.Button(545, 400, button_loadgame_img, self.click_sound_source, 0.3, 0.31)
        self.button_leaderboard = button.Button(545, 520, button_leaderboard_img, self.click_sound_source, 0.3, 0.31)
        self.button_exit = button.Button(545, 640, button_exit_img, self.click_sound_source, 0.3, 0.31)
        self.button_login_signin = button.Button(30, 690, button_login_signin_img, self.click_sound_source, 0.25, 0.26)
        self.button_logout = button.Button(30, 690, button_logout_img, self.click_sound_source, 0.25, 0.26)
        self.button_sound_on = button.Button(1110, 693, button_sound_on_img, self.click_sound_source, 0.25, 0.26)
        self.button_sound_off = button.Button(1109, 693, button_sound_off_img, self.click_sound_source, 0.25, 0.26)
        self.button_music_on = button.Button(1200, 690, button_music_on_img, self.click_sound_source, 0.25, 0.26)
        self.button_music_off = button.Button(1201, 692, button_music_off_img, self.click_sound_source, 0.25, 0.26)

                # create graphic
        self.background = graphic.Graphic(0, 0, background_img, 1.46)
        self.game_title = graphic.Graphic(100, 5, game_title_img, 0.3)
        self.main_menu_jerry = graphic.Graphic(170, 300, main_menu_jerry_img, 0.32)
        self.main_menu_tom = graphic.Graphic(900, 300, main_menu_tom_img, 0.32)
        
            # login signin
                    # create buttons
        self.button_login = button.Button(620, 500, button_login_img, self.click_sound_source, 0.3, 0.31)
        self.button_signin = button.Button(620, 500, button_signin_img, self.click_sound_source, 0.3, 0.31)
        self.button_box_login = button.Button(496, 200, button_box_login_img, self.click_sound_source, 0.3, 0.31)
        self.button_box_signin = button.Button(701, 200, button_box_signin_img, self.click_sound_source, 0.3, 0.31)
        self.button_back = button.Button(30, 690, button_back_img, self.click_sound_source, 0.3, 0.31)
                    # create login/ signin textbox
        self.username_login_textbox = textbox.TextBox(600, 335, 300, 50, self.click_sound_source)
        self.password_login_textbox = textbox.TextBox(600, 435, 300, 50, self.click_sound_source)
        self.username_signin_textbox = textbox.TextBox(600, 335, 300, 50, self.click_sound_source)
        self.password_signin_textbox = textbox.TextBox(600, 435, 300, 50, self.click_sound_source)

                    # create graphic
        self.background = graphic.Graphic(0, 0, background_img, 1.46)
        self.box_login = graphic.Graphic(450, 200, box_login_img, 0.3)
        self.box_signin = graphic.Graphic(450, 200, box_signin_img, 0.3)
        
            # leaderboard
                # create buttons
        self.button_leaderboard_easy = button.Button(892, 223, button_leaderboard_easy_img, self.click_sound_source, 0.3, 0.31)
        self.button_leaderboard_medium = button.Button(892, 383, button_leaderboard_medium_img, self.click_sound_source, 0.3, 0.31)
        self.button_leaderboard_hard = button.Button(892, 555, button_leaderboard_hard_img, self.click_sound_source, 0.3, 0.31)
        self.button_back = button.Button(30, 690, button_back_img, self.click_sound_source, 0.3, 0.31)

                # create graphic
        self.background = graphic.Graphic(0, 0, background_img, 1.46)
        self.leaderboard_easy = graphic.Graphic(330, -20, leaderboard_easy_img, 0.3)
        self.leaderboard_medium = graphic.Graphic(330, -20, leaderboard_medium_img, 0.3)
        self.leaderboard_hard = graphic.Graphic(330, -20, leaderboard_hard_img, 0.3)
        
            # new game
                # create buttons
        self.button_yes = button.Button(497, 450, button_yes_img, self.click_sound_source, 0.3, 0.31)
        self.button_no = button.Button(716, 450, button_no_img, self.click_sound_source, 0.3, 0.31)
        self.button_easy = button.Button(100, 230, button_easy_img, self.click_sound_source, 0.3, 0.31)
        self.button_medium = button.Button(100, 390, button_medium_img, self.click_sound_source, 0.3, 0.31)
        self.button_hard = button.Button(100, 550, button_hard_img, self.click_sound_source, 0.3, 0.31)
        self.button_back = button.Button(30, 690, button_back_img, self.click_sound_source, 0.3, 0.31)

                # create graphic
        self.background = graphic.Graphic(0, 0, background_img, 1.46)
        self.box_login_confirm = graphic.Graphic(425, 250, box_login_confirm_img, 0.3)
        self.choose_difficulty = graphic.Graphic(50, 0, choose_difficulty_img, 0.3)
        self.mood_easy = graphic.Graphic(800, 10, mood_easy_img, 0.3)
        # self.mood_medium = graphic.Graphic(800, 10, mood_medium_img, 0.3)
        # no suitable img
        self.mood_hard = graphic.Graphic(800, 10, mood_hard_img, 0.3)
        # gameplay video

    def draw_main_menu(self):
        self.background.draw(self.screen)
        self.game_title.draw(self.screen)
        self.main_menu_jerry.draw(self.screen)
        self.main_menu_tom.draw(self.screen)
        
        if self.button_newgame.draw(self.screen):
            self.game_state = 'new game'
        if self.button_loadgame.draw(self.screen):
            self.game_state = 'load game'
        if self.button_leaderboard.draw(self.screen):
            self.game_state = 'leaderboard'
        if self.button_exit.draw(self.screen):
            self.running = False
        if self.login == False:
            if self.button_login_signin.draw(self.screen):
                self.game_state = 'login signin'
        else:
            font = pygame.font.SysFont('The Fountain of Wishes Regular', 40)
            greeting = font.render(f'Hello {self.username}', True, (255, 255, 255))
            self.screen.blit(greeting, (180, 708))
            if self.button_logout.draw(self.screen):
                self.username = ''
                self.login = False
            
        if self.sound == True:
            if self.button_sound_on.draw(self.screen):
                self.sound = False
        else:
            if self.button_sound_off.draw(self.screen):
                self.sound = True
        if self.music == True:
            if self.button_music_on.draw(self.screen):
                self.music = False
        else:
            if self.button_music_off.draw(self.screen):
                self.music = True
        
    def draw_login_signin(self):
        self.background.draw(self.screen)
        if self.login_signin == 'log in':
            if self.button_box_signin.draw(self.screen):
                self.login_signin = 'sign in'
            self.box_login.draw(self.screen)

            self.username_login_textbox.draw(self.screen, COLOR.GREY)
            self.username_login_textbox.draw_text(self.screen, COLOR.BLACK, False)
            self.password_login_textbox.draw(self.screen, COLOR.GREY)
            self.password_login_textbox.draw_text(self.screen, COLOR.BLACK, True)

            self.username_login_textbox.get_text(self.screen)
            self.password_login_textbox.get_text(self.screen, True)

            if self.button_login.draw(self.screen):
                username = self.username_login_textbox.text
                password = self.password_login_textbox.text
                self.login = data.login(username, password)
                if self.login == True:
                    self.username = username
                    self.game_state = 'main menu'
            
        if self.login_signin == 'sign in':
            if self.button_box_login.draw(self.screen):
                self.login_signin = 'log in'
            self.box_signin.draw(self.screen)
            
            self.username_signin_textbox.draw(self.screen, COLOR.GREY)
            self.username_signin_textbox.draw_text(self.screen, COLOR.BLACK, False)
            self.password_signin_textbox.draw(self.screen, COLOR.GREY)
            self.password_signin_textbox.draw_text(self.screen, COLOR.BLACK, True)

            self.username_signin_textbox.get_text(self.screen)
            self.password_signin_textbox.get_text(self.screen, True)

            if self.button_signin.draw(self.screen):
                new_username = self.username_signin_textbox.text
                new_password = self.password_signin_textbox.text
                if new_username == "" or new_password == "":
                    pass
                else: self.login = data.register(new_username, new_password)
                if self.login == True:
                    self.username = new_username
                    self.game_state = 'main menu'
            
        if self.button_back.draw(self.screen):
            self.game_state = 'main menu'
            self.login_signin = 'log in'
            
        
    def draw_leaderboard(self):
        self.background.draw(self.screen)
        if self.leaderboard == 'easy':
            if self.button_leaderboard_medium.draw(self.screen):
                self.leaderboard = 'medium'
            if self.button_leaderboard_hard.draw(self.screen):
                self.leaderboard = 'hard'
            self.leaderboard_easy.draw(self.screen)
                
        if self.leaderboard == 'medium':
            if self.button_leaderboard_easy.draw(self.screen):
                self.leaderboard = 'easy'
            if self.button_leaderboard_hard.draw(self.screen):
                self.leaderboard = 'hard'
            self.leaderboard_medium.draw(self.screen)
                
        if self.leaderboard == 'hard':
            if self.button_leaderboard_easy.draw(self.screen):
                self.leaderboard = 'easy'
            if self.button_leaderboard_medium.draw(self.screen):
                self.leaderboard = 'medium'
            self.leaderboard_hard.draw(self.screen)
        
        if self.button_back.draw(self.screen):
            self.game_state = 'main menu'
            self.leaderboard = 'easy'
            
    def draw_new_game(self):
        # draw 
        self.background.draw(self.screen)
        if self.skip_login == False and self.login == False:
            self.box_login_confirm.draw(self.screen)
            if self.button_yes.draw(self.screen):
                self.game_state = 'login signin'
            if self.button_no.draw(self.screen):
                self.skip_login = True
        if self.skip_login == True or self.login == True:
            self.mood_hard.draw(self.screen)
            self.choose_difficulty.draw(self.screen)
            if self.button_easy.draw(self.screen):
                pass # do something here
            if self.button_medium.draw(self.screen):
                pass # do something here
            if self.button_hard.draw(self.screen):
                pass # do something here
        if self.button_back.draw(self.screen):
            self.game_state = 'main menu'
            self.skip_login = False