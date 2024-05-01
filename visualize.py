import button
import graphic
import os
import pygame

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
        self.login_signin = 'log in'
        self.leaderboard = 'easy'
        self.click_sound_source = pygame.mixer.Sound(os.path.join(sound_source, 'click.ogg'))

    def draw_main_menu(self):
        # button
        button_newgame_img = pygame.image.load(os.path.join(self.image_source, 'button_newgame.png')).convert_alpha()
        button_loadgame_img = pygame.image.load(os.path.join(self.image_source, 'button_loadgame.png')).convert_alpha()
        button_leaderboard_img = pygame.image.load(os.path.join(self.image_source, 'button_leaderboard.png')).convert_alpha()
        button_exit_img = pygame.image.load(os.path.join(self.image_source, 'button_exit.png')).convert_alpha()
        button_login_signin_img = pygame.image.load(os.path.join(self.image_source, 'button_login_signin.png')).convert_alpha()
        button_sound_on_img = pygame.image.load(os.path.join(self.image_source, 'button_sound_on.png')).convert_alpha()
        button_sound_off_img = pygame.image.load(os.path.join(self.image_source, 'button_sound_off.png')).convert_alpha()
        button_music_on_img = pygame.image.load(os.path.join(self.image_source, 'button_music_on.png')).convert_alpha()
        button_music_off_img = pygame.image.load(os.path.join(self.image_source, 'button_music_off.png')).convert_alpha()

        # graphic
        background_img = pygame.image.load(os.path.join(self.image_source, 'background1.png')).convert_alpha()
        title_img = pygame.image.load(os.path.join(self.image_source, 'game_title.png')).convert_alpha()
        mainscreen_jerry_img = pygame.image.load(os.path.join(self.image_source, 'mainscreen_jerry.png')).convert_alpha()
        mainscreen_tom_img = pygame.image.load(os.path.join(self.image_source, 'mainscreen_tom.png')).convert_alpha()

        # create buttons
        button_newgame = button.Button(545, 280, button_newgame_img, self.click_sound_source, 0.3, 0.31)
        button_loadgame = button.Button(545, 400, button_loadgame_img, self.click_sound_source, 0.3, 0.31)
        button_leaderboard = button.Button(545, 520, button_leaderboard_img, self.click_sound_source, 0.3, 0.31)
        button_exit = button.Button(545, 640, button_exit_img, self.click_sound_source, 0.3, 0.31)
        button_login_signin = button.Button(30, 690, button_login_signin_img, self.click_sound_source, 0.25, 0.26)
        button_sound_on = button.Button(1110, 693, button_sound_on_img, self.click_sound_source, 0.25, 0.26)
        button_sound_off = button.Button(1109, 693, button_sound_off_img, self.click_sound_source, 0.25, 0.26)
        button_music_on = button.Button(1200, 690, button_music_on_img, self.click_sound_source, 0.25, 0.26)
        button_music_off = button.Button(1201, 692, button_music_off_img, self.click_sound_source, 0.25, 0.26)

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
        
    def draw_login_signin(self):
        # button
        button_login_img = pygame.image.load(os.path.join(self.image_source, 'button_login.png')).convert_alpha()
        button_signin_img = pygame.image.load(os.path.join(self.image_source, 'button_signin.png')).convert_alpha()
        button_box_login_img = pygame.image.load(os.path.join(self.image_source, 'box_login2.png')).convert_alpha()
        button_box_signin_img = pygame.image.load(os.path.join(self.image_source, 'box_signin2.png')).convert_alpha()
        button_back_img = pygame.image.load(os.path.join(self.image_source, 'button_back.png')).convert_alpha()

        # graphic
        background_img = pygame.image.load(os.path.join(self.image_source, 'background1.png')).convert_alpha()
        box_login_img = pygame.image.load(os.path.join(self.image_source, 'box_login1.png')).convert_alpha()
        box_signin_img = pygame.image.load(os.path.join(self.image_source, 'box_signin1.png')).convert_alpha()

        # create buttons
        button_login = button.Button(620, 500, button_login_img, self.click_sound_source, 0.3, 0.31)
        button_signin = button.Button(620, 500, button_signin_img, self.click_sound_source, 0.3, 0.31)
        button_box_login = button.Button(496, 200, button_box_login_img, self.click_sound_source, 0.3, 0.31)
        button_box_signin = button.Button(701, 200, button_box_signin_img, self.click_sound_source, 0.3, 0.31)
        button_back = button.Button(30, 690, button_back_img, self.click_sound_source, 0.3, 0.31)

        # create graphic
        background = graphic.Graphic(0, 0, background_img, 1.46)
        box_login = graphic.Graphic(450, 200, box_login_img, 0.3)
        box_signin = graphic.Graphic(450, 200, box_signin_img, 0.3)
        
        # draw 
        background.draw(self.screen)
        if self.login_signin == 'log in':
            if button_box_signin.draw(self.screen):
                self.login_signin = 'sign in'
            box_login.draw(self.screen)
            if button_login.draw(self.screen):
                pass # do something here
            
        if self.login_signin == 'sign in':
            if button_box_login.draw(self.screen):
                self.login_signin = 'log in'
            box_signin.draw(self.screen)
            if button_signin.draw(self.screen):
                pass # do something here
            
        if button_back.draw(self.screen):
            self.game_state = 'main menu'
            self.login_signin = 'log in'
            
        
    def draw_leaderboard(self):
        # button
        button_leaderboard_easy_img = pygame.image.load(os.path.join(self.image_source, 'button_leaderboard_easy.png')).convert_alpha()
        button_leaderboard_medium_img = pygame.image.load(os.path.join(self.image_source, 'button_leaderboard_medium.png')).convert_alpha()
        button_leaderboard_hard_img = pygame.image.load(os.path.join(self.image_source, 'button_leaderboard_hard.png')).convert_alpha()
        button_back_img = pygame.image.load(os.path.join(self.image_source, 'button_back.png')).convert_alpha()

        # graphic
        background_img = pygame.image.load(os.path.join(self.image_source, 'background1.png')).convert_alpha()
        leaderboard_easy_img = pygame.image.load(os.path.join(self.image_source, 'leaderboard_easy.png')).convert_alpha()
        leaderboard_medium_img = pygame.image.load(os.path.join(self.image_source, 'leaderboard_medium.png')).convert_alpha()
        leaderboard_hard_img = pygame.image.load(os.path.join(self.image_source, 'leaderboard_hard.png')).convert_alpha()

        # create buttons
        button_leaderboard_easy = button.Button(892, 223, button_leaderboard_easy_img, self.click_sound_source, 0.3, 0.31)
        button_leaderboard_medium = button.Button(892, 383, button_leaderboard_medium_img, self.click_sound_source, 0.3, 0.31)
        button_leaderboard_hard = button.Button(892, 555, button_leaderboard_hard_img, self.click_sound_source, 0.3, 0.31)
        button_back = button.Button(30, 690, button_back_img, self.click_sound_source, 0.3, 0.31)

        # create graphic
        background = graphic.Graphic(0, 0, background_img, 1.46)
        leaderboard_easy = graphic.Graphic(330, -20, leaderboard_easy_img, 0.3)
        leaderboard_medium = graphic.Graphic(330, -20, leaderboard_medium_img, 0.3)
        leaderboard_hard = graphic.Graphic(330, -20, leaderboard_hard_img, 0.3)
        
        # draw 
        background.draw(self.screen)
        if self.leaderboard == 'easy':
            if button_leaderboard_medium.draw(self.screen):
                self.leaderboard = 'medium'
            if button_leaderboard_hard.draw(self.screen):
                self.leaderboard = 'hard'
            leaderboard_easy.draw(self.screen)
                
        if self.leaderboard == 'medium':
            if button_leaderboard_easy.draw(self.screen):
                self.leaderboard = 'easy'
            if button_leaderboard_hard.draw(self.screen):
                self.leaderboard = 'hard'
            leaderboard_medium.draw(self.screen)
                
        if self.leaderboard == 'hard':
            if button_leaderboard_easy.draw(self.screen):
                self.leaderboard = 'easy'
            if button_leaderboard_medium.draw(self.screen):
                self.leaderboard = 'medium'
            leaderboard_hard.draw(self.screen)
        
        if button_back.draw(self.screen):
            self.game_state = 'main menu'
            self.leaderboard = 'easy'
            
    def draw_newgame(self):
        # button
        button_yes_img = pygame.image.load(os.path.join(self.image_source, 'button_yes.png')).convert_alpha()
        button_no_img = pygame.image.load(os.path.join(self.image_source, 'button_no.png')).convert_alpha()
        button_easy_img = pygame.image.load(os.path.join(self.image_source, 'button_easy.png')).convert_alpha()
        button_medium_img = pygame.image.load(os.path.join(self.image_source, 'button_medium.png')).convert_alpha()
        button_hard_img = pygame.image.load(os.path.join(self.image_source, 'button_hard.png')).convert_alpha()
        button_back_img = pygame.image.load(os.path.join(self.image_source, 'button_back.png')).convert_alpha()

        # graphic
        background_img = pygame.image.load(os.path.join(self.image_source, 'background1.png')).convert_alpha()
        box_login_confirm_img = pygame.image.load(os.path.join(self.image_source, 'box_login_confirm.png')).convert_alpha()
        choose_difficulty_img = pygame.image.load(os.path.join(self.image_source, 'choose_difficulty.png')).convert_alpha()
        mood_easy_img = pygame.image.load(os.path.join(self.image_source, 'mood_easy.png')).convert_alpha()
        # mood_medium_img = pygame.image.load(os.path.join(self.image_source, 'mood_medium.png')).convert_alpha()
        # no suitable img
        mood_hard_img = pygame.image.load(os.path.join(self.image_source, 'mood_hard.png')).convert_alpha()
        # gameplay video

        # create buttons
        button_yes = button.Button(497, 450, button_yes_img, self.click_sound_source, 0.3, 0.31)
        button_no = button.Button(716, 450, button_no_img, self.click_sound_source, 0.3, 0.31)
        button_easy = button.Button(100, 230, button_easy_img, self.click_sound_source, 0.3, 0.31)
        button_medium = button.Button(100, 390, button_medium_img, self.click_sound_source, 0.3, 0.31)
        button_hard = button.Button(100, 550, button_hard_img, self.click_sound_source, 0.3, 0.31)
        button_back = button.Button(30, 690, button_back_img, self.click_sound_source, 0.3, 0.31)

        # create graphic
        background = graphic.Graphic(0, 0, background_img, 1.46)
        box_login_confirm = graphic.Graphic(425, 250, box_login_confirm_img, 0.3)
        choose_difficulty = graphic.Graphic(50, 0, choose_difficulty_img, 0.3)
        mood_easy = graphic.Graphic(800, 10, mood_easy_img, 0.3)
        # mood_medium = graphic.Graphic(800, 10, mood_medium_img, 0.3)
        # no suitable img
        mood_hard = graphic.Graphic(800, 10, mood_hard_img, 0.3)
        # gameplay video
        
        # draw 
        background.draw(self.screen)
        if self.skip_login == False and self.login == False:
            box_login_confirm.draw(self.screen)
            if button_yes.draw(self.screen):
                self.game_state = 'login signin'
            if button_no.draw(self.screen):
                self.skip_login = True
        if self.skip_login == True or self.login == True:
            mood_hard.draw(self.screen)
            choose_difficulty.draw(self.screen)
            if button_easy.draw(self.screen):
                pass
            if button_medium.draw(self.screen):
                pass
            if button_hard.draw(self.screen):
                pass
        if button_back.draw(self.screen):
            self.game_state = 'main menu'
            self.skip_login = False