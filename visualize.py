import button
import graphic
import os
import pygame

class GameScreen:
    def __init__(self, screen, images_source):
        self.screen = screen
        self.images_source = images_source
        self.running = True
        
        self.game_state = 'main menu'
        self.music = True
        self.sound = True
        self.login = True

    def draw_main_menu(self, click_sound):
        # button
        button_newgame_img = pygame.image.load(os.path.join(self.images_source, 'button_newgame.png')).convert_alpha()
        button_loadgame_img = pygame.image.load(os.path.join(self.images_source, 'button_loadgame.png')).convert_alpha()
        button_leaderboard_img = pygame.image.load(os.path.join(self.images_source, 'button_leaderboard.png')).convert_alpha()
        button_exit_img = pygame.image.load(os.path.join(self.images_source, 'button_exit.png')).convert_alpha()
        button_login_signin_img = pygame.image.load(os.path.join(self.images_source, 'button_login_signin.png')).convert_alpha()
        button_sound_on_img = pygame.image.load(os.path.join(self.images_source, 'button_sound_on.png')).convert_alpha()
        button_sound_off_img = pygame.image.load(os.path.join(self.images_source, 'button_sound_off.png')).convert_alpha()
        button_music_on_img = pygame.image.load(os.path.join(self.images_source, 'button_music_on.png')).convert_alpha()
        button_music_off_img = pygame.image.load(os.path.join(self.images_source, 'button_music_off.png')).convert_alpha()

        # graphic
        background_img = pygame.image.load(os.path.join(self.images_source, 'background1.png')).convert_alpha()
        title_img = pygame.image.load(os.path.join(self.images_source, 'game_title.png')).convert_alpha()
        mainscreen_jerry_img = pygame.image.load(os.path.join(self.images_source, 'mainscreen_jerry.png')).convert_alpha()
        mainscreen_tom_img = pygame.image.load(os.path.join(self.images_source, 'mainscreen_tom.png')).convert_alpha()

        # create buttons
        button_newgame = button.Button(545, 280, button_newgame_img, click_sound, 0.3, 0.31)
        button_loadgame = button.Button(545, 400, button_loadgame_img, click_sound, 0.3, 0.31)
        button_leaderboard = button.Button(545, 520, button_leaderboard_img, click_sound, 0.3, 0.31)
        button_exit = button.Button(545, 640, button_exit_img, click_sound, 0.3, 0.31)
        button_login_signin = button.Button(30, 690, button_login_signin_img, click_sound, 0.25, 0.26)
        button_sound_on = button.Button(1110, 693, button_sound_on_img, click_sound, 0.25, 0.26)
        button_sound_off = button.Button(1109, 693, button_sound_off_img, click_sound, 0.25, 0.26)
        button_music_on = button.Button(1200, 690, button_music_on_img, click_sound, 0.25, 0.26)
        button_music_off = button.Button(1201, 692, button_music_off_img, click_sound, 0.25, 0.26)

        # create graphic
        background = graphic.Graphic(0, 0, background_img, 1.46)
        title = graphic.Graphic(100, 5, title_img, 0.3)
        mainscreen_jerry = graphic.Graphic(170, 300, mainscreen_jerry_img, 0.32)
        mainscreen_tom = graphic.Graphic(900, 300, mainscreen_tom_img, 0.32)
        
        # draw 
        background.draw(self.screen)
        title.draw(self.screen)
        mainscreen_jerry.draw(self.screen)
        mainscreen_tom.draw(self.screen)
        
        if button_newgame.draw(self.screen):
            self.game_state = 'new game'
        elif button_loadgame.draw(self.screen):
            self.game_state = 'load game'
        elif button_leaderboard.draw(self.screen):
            self.game_state = 'leaderboard'
        elif button_exit.draw(self.screen):
            self.running = False
        elif button_login_signin.draw(self.screen):
            self.game_state = 'login signin'
            
        if self.sound == True:
            if button_sound_on.draw(self.screen):
                self.sound = False
        else:
            if button_sound_off.draw(self.screen):
                self.sound = True
        if self.music == True:
            if button_music_on.draw(self.screen):
                self.music = False
        else:
            if button_music_off.draw(self.screen):
                self.music = True
        
    def draw_login_signin(self, click_sound):
        # button
        button_login_img = pygame.image.load(os.path.join(self.images_source, 'button_login.png')).convert_alpha()
        button_signin_img = pygame.image.load(os.path.join(self.images_source, 'button_signin.png')).convert_alpha()
        button_box_login_img = pygame.image.load(os.path.join(self.images_source, 'box_login2.png')).convert_alpha()
        button_box_signin_img = pygame.image.load(os.path.join(self.images_source, 'box_signin2.png')).convert_alpha()
        button_back_img = pygame.image.load(os.path.join(self.images_source, 'button_back.png')).convert_alpha()

        # graphic
        background_img = pygame.image.load(os.path.join(self.images_source, 'background1.png')).convert_alpha()
        box_login_img = pygame.image.load(os.path.join(self.images_source, 'box_login1.png')).convert_alpha()
        box_signin_img = pygame.image.load(os.path.join(self.images_source, 'box_signin1.png')).convert_alpha()

        # create buttons
        button_login = button.Button(620, 500, button_login_img, click_sound, 0.3, 0.31)
        button_signin = button.Button(620, 500, button_signin_img, click_sound, 0.3, 0.31)
        button_box_login = button.Button(496, 200, button_box_login_img, click_sound, 0.3, 0.31)
        button_box_signin = button.Button(701, 200, button_box_signin_img, click_sound, 0.3, 0.31)
        button_back = button.Button(30, 690, button_back_img, click_sound, 0.3, 0.31)

        # create graphic
        background = graphic.Graphic(0, 0, background_img, 1.46)
        box_login = graphic.Graphic(450, 200, box_login_img, 0.3)
        box_signin = graphic.Graphic(450, 200, box_signin_img, 0.3)
        
        # draw 
        background.draw(self.screen)
        if button_back.draw(self.screen):
            self.game_state = 'main menu'
        if self.login == True:
            if button_box_signin.draw(self.screen):
                self.login = False
            box_login.draw(self.screen)
            if button_login.draw(self.screen):
                pass # do something here
        if self.login == False:
            if button_box_login.draw(self.screen):
                self.login = True
            box_signin.draw(self.screen)
            if button_signin.draw(self.screen):
                pass # do something here