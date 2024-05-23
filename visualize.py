from menu_objects import button
from menu_objects import graphic
from menu_objects import textbox
from menu_objects import music
from menu_objects import saveslot
from data import data
import os
import pygame



from CONSTANTS import COLOR
from CONSTANTS import DISPLAY
from CONSTANTS import DIFFICULTY

SCREEN_WIDTH = DISPLAY.SCREEN_WIDTH
SCREEN_HEIGHT = DISPLAY.SCREEN_HEIGHT
HALF_SCREEN_WIDTH = SCREEN_WIDTH * 0.5
HALF_SCREEN_HEIGHT = SCREEN_HEIGHT * 0.5


def create_img(image_source, image_name):
    image_name = image_name + ".png"
    return pygame.image.load(os.path.join(image_source, image_name)).convert_alpha()


class GameScreen:
    def __init__(self, screen, image_source, sound_source):
        self.screen = screen
        self.image_source = image_source
        self.sound_source = sound_source
        self.running = True
        # self.font = pygame.font.SysFont('The Fountain of Wishes Regular', 40)
        self.font = pygame.font.Font("fonts/The Fountain of Wishes Regular.ttf", 40)
        self.leaderboard_font = pygame.font.Font(
            "fonts/The Fountain of Wishes Regular.ttf", 30
        )
        self.load_game_difficulty_font = pygame.font.Font('fonts/The Fountain of Wishes Regular.ttf', 150)
        self.load_game_content_font = pygame.font.Font('fonts/The Fountain of Wishes Regular.ttf', 70)
        self.game_state = "main menu"
        self.help_state = False
        self.difficulty = ""
        self.login_signin_state = "log in"
        self.leaderboard_state = "easy"
        self.new_game_state = "choose difficulty"
        self.spawning = ""
        self.energy_mode = False
        self.insane_mode = False
        self.maze_visualizer = False
        self.maze_generate_algo = 'HAK'
        self.load_game_state = 'list'
        self.load_id = DISPLAY.SAVE_LIMIT
        self.load_game_snapshots = None # check this
        self.music = True
        self.sound = True
        self.login = False  # do something with login system
        self.skip_login = False
        self.username = ""
        self.user_id = None

        # music and sound player
        self.click_sound_source = pygame.mixer.Sound(
            os.path.join(sound_source, "click.ogg")
        )
        self.music_player = music.MusicController()
        self.music_player.play_music(self.game_state)

        """ load button_img and graphic_img for the game """
        """ MAIN MENU """
        button_newgame_img = create_img(self.image_source, "button_newgame")
        button_loadgame_img = create_img(self.image_source, "button_loadgame")
        button_leaderboard_img = create_img(self.image_source, "button_leaderboard")
        button_exit_img = create_img(self.image_source, "button_exit")
        button_login_signin_img = create_img(self.image_source, "button_login_signin")
        button_logout_img = create_img(self.image_source, "button_logout")
        button_sound_on_img = create_img(self.image_source, "button_sound_on")
        button_sound_off_img = create_img(self.image_source, "button_sound_off")
        button_music_on_img = create_img(self.image_source, "button_music_on")
        button_music_off_img = create_img(self.image_source, "button_music_off")
        button_help_img = create_img(self.image_source, "button_help")
        button_close_img = create_img(self.image_source, "button_close")
        background_main_menu_img = create_img(self.image_source, "background_main_menu")
        game_title_img = create_img(self.image_source, "game_title")
        main_menu_jerry_img = create_img(self.image_source, "main_menu_jerry")
        main_menu_tom_img = create_img(self.image_source, "main_menu_tom")
        game_description_img = create_img(self.image_source, "game_description")

        """ LOGIN SIGNIN """
        button_login_img = create_img(self.image_source, "button_login")
        button_signin_img = create_img(self.image_source, "button_signin")
        button_box_login_img = create_img(self.image_source, "box_login2")
        button_box_signin_img = create_img(self.image_source, "box_signin2")
        button_back_img = create_img(self.image_source, "button_back")
        background_login_signin_img = create_img(
            self.image_source, "background_login_signin"
        )
        box_login_signin_img = create_img(self.image_source, "box_login_signin")
        box_login_img = create_img(self.image_source, "box_login1")
        box_signin_img = create_img(self.image_source, "box_signin1")

        """ LEADERBOARD """
        button_leaderboard_easy_img = create_img(
            self.image_source, "button_leaderboard_easy"
        )
        button_leaderboard_medium_img = create_img(
            self.image_source, "button_leaderboard_medium"
        )
        button_leaderboard_hard_img = create_img(
            self.image_source, "button_leaderboard_hard"
        )
        background_leaderboard_img = create_img(
            self.image_source, "background_leaderboard"
        )
        leaderboard_img = create_img(self.image_source, "leaderboard")
        leaderboard_easy_img = create_img(self.image_source, "leaderboard_easy")
        leaderboard_medium_img = create_img(self.image_source, "leaderboard_medium")
        leaderboard_hard_img = create_img(self.image_source, "leaderboard_hard")

        """ NEW GAME """
        button_yes_img = create_img(self.image_source, "button_yes")
        button_no_img = create_img(self.image_source, "button_no")
        button_easy_img = create_img(self.image_source, "button_easy")
        button_medium_img = create_img(self.image_source, "button_medium")
        button_hard_img = create_img(self.image_source, "button_hard")
        button_random_img = create_img(self.image_source, "button_random")
        button_manual_img = create_img(self.image_source, "button_manual")
        button_uncheck_img = create_img(self.image_source, "button_uncheck")
        button_check_img = create_img(self.image_source, "button_check")
        background_new_game_img = create_img(self.image_source, "background_new_game")
        box_login_confirm_img = create_img(self.image_source, "box_login_confirm")
        choose_difficulty_img = create_img(self.image_source, "choose_difficulty")
        box_choose_spawn_point_img = create_img(
            self.image_source, "box_choose_spawn_point"
        )
        box_choose_settings_img = create_img(self.image_source, "box_choose_settings")
        mood_easy_img = create_img(self.image_source, "mood_easy")
        mood_medium_img = create_img(self.image_source, "mood_medium")
        mood_hard_img = create_img(self.image_source, "mood_hard")
        # gameplay video

        """ LOAD GAME """
        button_save_img = create_img(self.image_source, 'button_save')
        button_load_img = create_img(self.image_source, 'button_load')
        button_delete_img = create_img(self.image_source, 'button_delete')
        background_load_game_img = create_img(self.image_source, 'background_load_game')
        overlay_img = create_img(self.image_source, 'overlay')
        easy_snapshot_1_img = create_img(self.image_source, 'temp_maze_snapshot')
        self.test_snapshot_img = create_img('database/save_game_images', 'Game_7')
        box_save_frame_img = create_img(self.image_source, 'box_save_frame')
        box_save_profile_img = create_img(self.image_source, 'box_save_profile')
        
        """ create button and graphic for the game """
        """ MAIN MENU """
        # create graphic
        self.background_main_menu = graphic.Graphic(
            HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, background_main_menu_img, 1.46
        )
        self.game_title = graphic.Graphic(
            HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.15, game_title_img, 0.3
        )
        self.main_menu_jerry = graphic.Graphic(
            SCREEN_WIDTH * 0.25, SCREEN_HEIGHT * 0.67, main_menu_jerry_img, 0.32
        )
        self.main_menu_tom = graphic.Graphic(
            SCREEN_WIDTH * 0.77, SCREEN_HEIGHT * 0.63, main_menu_tom_img, 0.32
        )
        self.game_description = graphic.Graphic(
            HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, game_description_img, 0.3
        )
        # game_description_width = self.game_description.modified_width
        game_description_height = self.game_description.modified_height

        # create buttons
        self.button_newgame = button.Button(
            HALF_SCREEN_WIDTH,
            SCREEN_HEIGHT * 0.4,
            button_newgame_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_loadgame = button.Button(
            HALF_SCREEN_WIDTH,
            SCREEN_HEIGHT * 0.55,
            button_loadgame_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_leaderboard = button.Button(
            HALF_SCREEN_WIDTH,
            SCREEN_HEIGHT * 0.7,
            button_leaderboard_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_exit = button.Button(
            HALF_SCREEN_WIDTH,
            SCREEN_HEIGHT * 0.85,
            button_exit_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_login_signin = button.Button(
            SCREEN_WIDTH * 0.09,
            SCREEN_HEIGHT * 0.92,
            button_login_signin_img,
            self.click_sound_source,
            0.25,
            0.26,
        )
        self.button_logout = button.Button(
            SCREEN_WIDTH * 0.09,
            SCREEN_HEIGHT * 0.92,
            button_logout_img,
            self.click_sound_source,
            0.25,
            0.26,
        )
        self.button_sound_on = button.Button(
            SCREEN_WIDTH * 0.8,
            SCREEN_HEIGHT * 0.92,
            button_sound_on_img,
            self.click_sound_source,
            0.25,
            0.26,
        )
        self.button_sound_off = button.Button(
            SCREEN_WIDTH * 0.8,
            SCREEN_HEIGHT * 0.92,
            button_sound_off_img,
            self.click_sound_source,
            0.25,
            0.26,
        )
        self.button_music_on = button.Button(
            SCREEN_WIDTH * 0.87,
            SCREEN_HEIGHT * 0.92,
            button_music_on_img,
            self.click_sound_source,
            0.25,
            0.26,
        )
        self.button_music_off = button.Button(
            SCREEN_WIDTH * 0.87,
            SCREEN_HEIGHT * 0.92,
            button_music_off_img,
            self.click_sound_source,
            0.25,
            0.26,
        )
        self.button_help = button.Button(
            SCREEN_WIDTH * 0.73,
            SCREEN_HEIGHT * 0.92,
            button_help_img,
            self.click_sound_source,
            0.25,
            0.26,
        )
        self.button_close = button.Button(
            HALF_SCREEN_WIDTH,
            HALF_SCREEN_HEIGHT + game_description_height * 0.38,
            button_close_img,
            self.click_sound_source,
            0.3,
            0.31,
        )

        """ LOGIN SIGNIN """
        # create graphic
        self.background_login_signin = graphic.Graphic(
            HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, background_login_signin_img, 1.46
        )
        self.box_login_signin = graphic.Graphic(
            HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, box_login_signin_img, 0.3
        )
        box_width = self.box_login_signin.modified_width
        box_height = self.box_login_signin.modified_height
        self.box_login = graphic.Graphic(
            HALF_SCREEN_WIDTH - box_width * 0.21,
            HALF_SCREEN_HEIGHT - box_height * 0.52,
            box_login_img,
            0.3,
        )
        self.box_signin = graphic.Graphic(
            HALF_SCREEN_WIDTH + box_width * 0.21,
            HALF_SCREEN_HEIGHT - box_height * 0.52,
            box_signin_img,
            0.3,
        )

        # create buttons
        self.button_login = button.Button(
            HALF_SCREEN_WIDTH,
            HALF_SCREEN_HEIGHT + box_height * 0.33,
            button_login_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_signin = button.Button(
            HALF_SCREEN_WIDTH,
            HALF_SCREEN_HEIGHT + box_height * 0.33,
            button_signin_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_box_login = button.Button(
            HALF_SCREEN_WIDTH - box_width * 0.21,
            HALF_SCREEN_HEIGHT - box_height * 0.52,
            button_box_login_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_box_signin = button.Button(
            HALF_SCREEN_WIDTH + box_width * 0.21,
            HALF_SCREEN_HEIGHT - box_height * 0.52,
            button_box_signin_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_back = button.Button(
            SCREEN_WIDTH * 0.05,
            SCREEN_HEIGHT * 0.92,
            button_back_img,
            self.click_sound_source,
            0.3,
            0.31,
        )

        # create login/ signin textbox
        self.username_login_textbox = textbox.TextBox(
            HALF_SCREEN_WIDTH - box_width * 0.21,
            HALF_SCREEN_HEIGHT - box_height * 0.37,
            300,
            50,
            self.image_source,
            self.click_sound_source,
        )
        self.password_login_textbox = textbox.TextBox(
            HALF_SCREEN_WIDTH - box_width * 0.21,
            HALF_SCREEN_HEIGHT - box_height * 0.11,
            300,
            50,
            self.image_source,
            self.click_sound_source,
        )
        self.username_signin_textbox = textbox.TextBox(
            HALF_SCREEN_WIDTH - box_width * 0.21,
            HALF_SCREEN_HEIGHT - box_height * 0.37,
            300,
            50,
            self.image_source,
            self.click_sound_source,
        )
        self.password_signin_textbox = textbox.TextBox(
            HALF_SCREEN_WIDTH - box_width * 0.21,
            HALF_SCREEN_HEIGHT - box_height * 0.11,
            300,
            50,
            self.image_source,
            self.click_sound_source,
        )

        """ LEADERBOARD """
        # create graphic
        self.background_leaderboard = graphic.Graphic(
            HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, background_leaderboard_img, 1.1
        )
        self.leaderboard = graphic.Graphic(
            HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.47, leaderboard_img, 0.3
        )
        leaderbboard_width = self.leaderboard.modified_width
        leaderbboard_height = self.leaderboard.modified_height
        self.leaderboard_easy = graphic.Graphic(
            HALF_SCREEN_WIDTH + leaderbboard_width * 0.367,
            HALF_SCREEN_HEIGHT - leaderbboard_height * 0.12,
            leaderboard_easy_img,
            0.3,
        )
        self.leaderboard_medium = graphic.Graphic(
            HALF_SCREEN_WIDTH + leaderbboard_width * 0.367,
            HALF_SCREEN_HEIGHT + leaderbboard_height * 0.1,
            leaderboard_medium_img,
            0.3,
        )
        self.leaderboard_hard = graphic.Graphic(
            HALF_SCREEN_WIDTH + leaderbboard_width * 0.367,
            HALF_SCREEN_HEIGHT + leaderbboard_height * 0.32,
            leaderboard_hard_img,
            0.3,
        )

        # create buttons
        self.button_leaderboard_easy = button.Button(
            HALF_SCREEN_WIDTH + leaderbboard_width * 0.367,
            HALF_SCREEN_HEIGHT - leaderbboard_height * 0.12,
            button_leaderboard_easy_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_leaderboard_medium = button.Button(
            HALF_SCREEN_WIDTH + leaderbboard_width * 0.367,
            HALF_SCREEN_HEIGHT + leaderbboard_height * 0.1,
            button_leaderboard_medium_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_leaderboard_hard = button.Button(
            HALF_SCREEN_WIDTH + leaderbboard_width * 0.367,
            HALF_SCREEN_HEIGHT + leaderbboard_height * 0.32,
            button_leaderboard_hard_img,
            self.click_sound_source,
            0.3,
            0.31,
        )

        """ NEW GAME"""
        # create graphic
        self.background_new_game = graphic.Graphic(
            HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, background_new_game_img, 1.46
        )
        self.box_login_confirm = graphic.Graphic(
            HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, box_login_confirm_img, 0.3
        )
        box_login_confirm_width = self.box_login_confirm.modified_width
        box_login_confirm_height = self.box_login_confirm.modified_height
        self.choose_difficulty = graphic.Graphic(
            SCREEN_WIDTH * 0.27, SCREEN_HEIGHT * 0.15, choose_difficulty_img, 0.3
        )
        self.box_choose_settings = graphic.Graphic(
            SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.6, box_choose_settings_img, 0.3
        )
        box_choose_settings_width = self.box_choose_settings.modified_width
        box_choose_settings_height = self.box_choose_settings.modified_height
        box_choose_settings_x_coord = self.box_choose_settings.x_coord
        box_choose_settings_y_coord = self.box_choose_settings.y_coord
        self.mood_easy = graphic.Graphic(
            SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.13, mood_easy_img, 0.3
        )
        self.mood_medium = graphic.Graphic(
            SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.13, mood_medium_img, 0.3
        )
        self.mood_hard = graphic.Graphic(
            SCREEN_WIDTH * 0.7, SCREEN_HEIGHT * 0.13, mood_hard_img, 0.3
        )

        # create buttons
        self.button_yes = button.Button(
            HALF_SCREEN_WIDTH - box_login_confirm_width * 0.2,
            HALF_SCREEN_HEIGHT + box_login_confirm_height * 0.25,
            button_yes_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_no = button.Button(
            HALF_SCREEN_WIDTH + box_login_confirm_width * 0.2,
            HALF_SCREEN_HEIGHT + box_login_confirm_height * 0.25,
            button_no_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_easy = button.Button(
            SCREEN_WIDTH * 0.24,
            SCREEN_HEIGHT * 0.35,
            button_easy_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_medium = button.Button(
            SCREEN_WIDTH * 0.24,
            SCREEN_HEIGHT * 0.55,
            button_medium_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_hard = button.Button(
            SCREEN_WIDTH * 0.24,
            SCREEN_HEIGHT * 0.75,
            button_hard_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_random = button.Button(
            box_choose_settings_x_coord - box_choose_settings_width * 0.2,
            box_choose_settings_y_coord + box_choose_settings_height * 0.35,
            button_random_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_manual = button.Button(
            box_choose_settings_x_coord + box_choose_settings_width * 0.2,
            box_choose_settings_y_coord + box_choose_settings_height * 0.35,
            button_manual_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_uncheck_energy_mode = button.Button(
            box_choose_settings_x_coord - box_choose_settings_width * 0.21,
            box_choose_settings_y_coord - box_choose_settings_height * 0.285,
            button_uncheck_img,
            self.click_sound_source,
            0.3,
            0.3,
        )
        self.button_uncheck_insane_mode = button.Button(
            box_choose_settings_x_coord + box_choose_settings_width * 0.21,
            box_choose_settings_y_coord - box_choose_settings_height * 0.285, button_uncheck_img, self.click_sound_source, 0.3, 0.3)
        self.button_uncheck_hak = button.Button(box_choose_settings_x_coord - box_choose_settings_width * 0.255, box_choose_settings_y_coord - box_choose_settings_height * 0.054, button_uncheck_img, self.click_sound_source, 0.3, 0.3)
        self.button_uncheck_dfs = button.Button(box_choose_settings_x_coord + box_choose_settings_width * 0.115, box_choose_settings_y_coord - box_choose_settings_height * 0.054,
            button_uncheck_img,
            self.click_sound_source,
            0.3,
            0.3,
        )
        self.button_uncheck_visualizer = button.Button(
            box_choose_settings_x_coord - box_choose_settings_width * 0.16,
            box_choose_settings_y_coord + box_choose_settings_height * 0.057,
            button_uncheck_img,
            self.click_sound_source,
            0.3,
            0.3,
        )
        self.button_check_energy_mode = button.Button(
            box_choose_settings_x_coord - box_choose_settings_width * 0.21,
            box_choose_settings_y_coord - box_choose_settings_height * 0.285,
            button_check_img,
            self.click_sound_source,
            0.3,
            0.3,
        )
        self.button_check_insane_mode = button.Button(
            box_choose_settings_x_coord + box_choose_settings_width * 0.21,
            box_choose_settings_y_coord - box_choose_settings_height * 0.285, button_check_img, self.click_sound_source, 0.3, 0.3)
        self.button_check_hak = button.Button(box_choose_settings_x_coord - box_choose_settings_width * 0.255, box_choose_settings_y_coord - box_choose_settings_height * 0.054, button_check_img, self.click_sound_source, 0.3, 0.3)
        self.button_check_dfs = button.Button(box_choose_settings_x_coord + box_choose_settings_width * 0.115, box_choose_settings_y_coord - box_choose_settings_height * 0.054,
            button_check_img,
            self.click_sound_source,
            0.3,
            0.3,
        )
        self.button_check_visualizer = button.Button(
            box_choose_settings_x_coord - box_choose_settings_width * 0.16,
            box_choose_settings_y_coord + box_choose_settings_height * 0.057,
            button_check_img,
            self.click_sound_source,
            0.3,
            0.3,
        )

        """ LOAD GAME """
                # create graphic
        self.snapshots = []
        self.saved_games = []
        self.background_load_game = graphic.Graphic(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, background_load_game_img, 1.5)
        self.easy_snapshot_1 = graphic.Graphic(450, 440, easy_snapshot_1_img, 2.5)
        self.test_snapshot = graphic.Graphic(450, 440, self.test_snapshot_img, 0.7)
        self.box_save_profile = graphic.Graphic(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, box_save_profile_img, 0.3)
        box_save_profile_img_width = self.box_save_profile.modified_width
        box_save_profile_img_height = self.box_save_profile.modified_height
        box_save_profile_img_x_coord = self.box_save_profile.x_coord
        box_save_profile_img_y_coord = self.box_save_profile.y_coord
        
        
        box_choose_settings_width = self.box_choose_settings.modified_width
        box_choose_settings_height = self.box_choose_settings.modified_height
        box_choose_settings_x_coord = self.box_choose_settings.x_coord
        box_choose_settings_y_coord = self.box_choose_settings.y_coord
        
                # create buttons
        self.button_easy_load_game = button.Button(HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.15, button_easy_img, self.click_sound_source, 0.3, 0.31)
        self.button_medium_load_game = button.Button(HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.15, button_medium_img, self.click_sound_source, 0.3, 0.31)
        self.button_hard_load_game = button.Button(HALF_SCREEN_WIDTH, SCREEN_HEIGHT * 0.15, button_hard_img, self.click_sound_source, 0.3, 0.31)
        self.box_save_frame_1 = button.Button(HALF_SCREEN_WIDTH  - 400, HALF_SCREEN_HEIGHT - 200, box_save_frame_img, self.click_sound_source, 0.3, 0.31)
        self.box_save_frame_2 = button.Button(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT - 200, box_save_frame_img, self.click_sound_source, 0.3, 0.31)
        self.box_save_frame_3 = button.Button(HALF_SCREEN_WIDTH + 400, HALF_SCREEN_HEIGHT - 200, box_save_frame_img, self.click_sound_source, 0.3, 0.31)
        self.box_save_frame_4 = button.Button(HALF_SCREEN_WIDTH  - 400, HALF_SCREEN_HEIGHT + 200, box_save_frame_img, self.click_sound_source, 0.3, 0.31)
        self.box_save_frame_5 = button.Button(HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT + 200, box_save_frame_img, self.click_sound_source, 0.3, 0.31)
        self.box_save_frame_6 = button.Button(HALF_SCREEN_WIDTH  + 400, HALF_SCREEN_HEIGHT + 200, box_save_frame_img, self.click_sound_source, 0.3, 0.31)
        self.box_save_list = [self.box_save_frame_1, self.box_save_frame_2, self.box_save_frame_3, self.box_save_frame_4, self.box_save_frame_5, self.box_save_frame_6]
        self.button_load = button.Button(box_save_profile_img_x_coord + box_save_profile_img_width * 0.1, box_save_profile_img_y_coord + box_save_profile_img_height * 0.3, button_load_img, self.click_sound_source, 0.3, 0.31)
        self.button_delete = button.Button(box_save_profile_img_x_coord + box_save_profile_img_width * 0.3, box_save_profile_img_y_coord + box_save_profile_img_height * 0.3, button_delete_img, self.click_sound_source, 0.3, 0.31)
        
        # create graphic
        self.background_load_game = graphic.Graphic(
            HALF_SCREEN_WIDTH, HALF_SCREEN_HEIGHT, background_load_game_img, 1.5
        )
        # self.saveslot_easy_1 = saveslot.SaveSlot(
        #     HALF_SCREEN_WIDTH * 0.6,
        #     HALF_SCREEN_HEIGHT,
        #     frame_img,
        #     overlay_img,
        #     button_load_img,
        #     button_delete_img,
        #     self.click_sound_source,
        #     0.4,
        #     0.4,
        # )
        # self.saveslot_easy_2 = saveslot.SaveSlot(
        #     HALF_SCREEN_WIDTH * 1.3,
        #     HALF_SCREEN_HEIGHT,
        #     frame_img,
        #     overlay_img,
        #     button_load_img,
        #     button_delete_img,
        #     self.click_sound_source,
        #     0.4,
        #     0.4,
        # )
        # self.saveslot_medium_1 = saveslot.SaveSlot(
        #     HALF_SCREEN_WIDTH * 0.6,
        #     HALF_SCREEN_HEIGHT,
        #     frame_img,
        #     overlay_img,
        #     button_load_img,
        #     button_delete_img,
        #     self.click_sound_source,
        #     0.4,
        #     0.4,
        # )
        # self.saveslot_medium_2 = saveslot.SaveSlot(
        #     HALF_SCREEN_WIDTH * 1.3,
        #     HALF_SCREEN_HEIGHT,
        #     frame_img,
        #     overlay_img,
        #     button_load_img,
        #     button_delete_img,
        #     self.click_sound_source,
        #     0.4,
        #     0.4,
        # )
        # self.saveslot_hard_1 = saveslot.SaveSlot(
        #     HALF_SCREEN_WIDTH * 0.6,
        #     HALF_SCREEN_HEIGHT,
        #     frame_img,
        #     overlay_img,
        #     button_load_img,
        #     button_delete_img,
        #     self.click_sound_source,
        #     0.4,
        #     0.4,
        # )
        # self.saveslot_hard_2 = saveslot.SaveSlot(
        #     HALF_SCREEN_WIDTH * 1.3,
        #     HALF_SCREEN_HEIGHT,
        #     frame_img,
        #     overlay_img,
        #     button_load_img,
        #     button_delete_img,
        #     self.click_sound_source,
        #     0.4,
        #     0.4,
        # )
        self.easy_snapshot_1 = graphic.Graphic(
            HALF_SCREEN_WIDTH * 0.6, HALF_SCREEN_HEIGHT, easy_snapshot_1_img, 1.5
        )

        # create buttons
        self.button_easy_load_game = button.Button(
            HALF_SCREEN_WIDTH,
            SCREEN_HEIGHT * 0.15,
            button_easy_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_medium_load_game = button.Button(
            HALF_SCREEN_WIDTH,
            SCREEN_HEIGHT * 0.15,
            button_medium_img,
            self.click_sound_source,
            0.3,
            0.31,
        )
        self.button_hard_load_game = button.Button(
            HALF_SCREEN_WIDTH,
            SCREEN_HEIGHT * 0.15,
            button_hard_img,
            self.click_sound_source,
            0.3,
            0.31,
        )

    def draw_main_menu(self, event):
        pos = pygame.mouse.get_pos()
        self.background_main_menu.draw(self.screen)
        if self.help_state == False:
            self.game_title.draw(self.screen)
            self.main_menu_jerry.draw(self.screen)
            self.main_menu_tom.draw(self.screen)
            if self.button_newgame.draw(self.screen, pos, event, self.sound):
                self.game_state = "new game"
            if self.button_loadgame.draw(self.screen, pos, event, self.sound):
                self.game_state = "load game"
            if self.button_leaderboard.draw(self.screen, pos, event, self.sound):
                self.game_state = "leaderboard"
            if self.button_exit.draw(self.screen, pos, event, self.sound):
                self.running = False
            if self.login == False:
                if self.button_login_signin.draw(self.screen, pos, event, self.sound):
                    self.game_state = "login signin"
            else:
                greeting = self.font.render(
                    f"Hello {self.username}", True, (255, 255, 255)
                )
                self.screen.blit(greeting, (SCREEN_WIDTH * 0.15, SCREEN_HEIGHT * 0.9))
                if self.button_logout.draw(self.screen, pos, event, self.sound):
                    self.username = ""
                    self.user_id = None
                    self.login = False
                    self.login_signin_state = "log in"

            if self.sound == True:
                if self.button_sound_on.draw(self.screen, pos, event, self.sound):
                    self.sound = False
            else:
                if self.button_sound_off.draw(self.screen, pos, event, self.sound):
                    self.sound = True
            if self.music == True:
                if self.button_music_on.draw(self.screen, pos, event, self.sound):
                    self.music_player.pause_music()
                    self.music = False
            else:
                if self.button_music_off.draw(self.screen, pos, event, self.sound):
                    self.music_player.unpause_music()
                    self.music = True
            if self.button_help.draw(self.screen, pos, event, self.sound):
                self.help_state = True
        else:
            self.game_description.draw(self.screen)
            if self.button_close.draw(self.screen, pos, event, self.sound):
                self.game_state = "main menu"
                self.help_state = False

    def get_saved_data(self):
        self.saved_games = data.get_saved_game(self.user_id)
        self.snapshots = []
        for i in range(min(len(self.saved_games), DISPLAY.SAVE_LIMIT)):
            snapshot_img = create_img('database/save_game_images', 'Game_' + str(self.saved_games[i][0]))
            list_snapshot_xcoord = self.box_save_list[i].x_coord
            list_snapshot_ycoord = self.box_save_list[i].y_coord
            # detail coord = (450, 440)
            self.snapshots.append([graphic.Graphic(list_snapshot_xcoord, list_snapshot_ycoord, snapshot_img, 0.5), 
                                   graphic.Graphic(450, 440, snapshot_img, 0.7)])

    def draw_login_signin(self, event):
        pos = pygame.mouse.get_pos()

        self.background_login_signin.draw(self.screen)
        state = None

        if self.login_signin_state == "log in":
            if self.button_box_signin.draw(self.screen, pos, event, self.sound):
                self.login_signin_state = "sign in"
                self.username_login_textbox.text = ""
                self.password_login_textbox.text = ""
            self.box_login_signin.draw(self.screen)
            self.box_login.draw(self.screen)

            # Draw Textbox
            self.username_login_textbox.draw(self.screen, COLOR.GREY)
            self.username_login_textbox.draw_text(
                self.screen,
                COLOR.BLACK,
                is_password=False,
                censored=False,
                activated=False,
            )
            self.password_login_textbox.draw(self.screen, COLOR.GREY)
            self.password_login_textbox.draw_text(
                self.screen,
                COLOR.BLACK,
                is_password=True,
                censored=True,
                activated=False,
            )

            # Get input
            state = self.username_login_textbox.get_text(
                self.screen,
                self.button_back,
                self.button_login,
                event,
                sound_on=self.sound,
            )
            state = self.password_login_textbox.get_text(
                self.screen,
                self.button_back,
                self.button_login,
                event,
                is_password=True,
                censored=True,
                sound_on=self.sound,
            )

            if (
                self.button_login.draw(self.screen, pos, event, self.sound)
                or state == "submit"
            ):
                username = self.username_login_textbox.text
                password = self.password_login_textbox.text
                self.login, self.user_id = data.login(username, password)
                if self.login == True:
                    self.username = username
                    self.game_state = "main menu"
                    self.get_saved_data()
                    # Update snapshots here
                else:
                    notification_text = self.font.render(
                        "Incorrect username or password.", True, COLOR.RED
                    )
                    self.screen.blit(
                        notification_text, (SCREEN_WIDTH * 0.36, SCREEN_HEIGHT * 0.52)
                    )
                    pygame.display.update()
                    pygame.time.wait(1000)

        if self.login_signin_state == "sign in":
            if self.button_box_login.draw(self.screen, pos, event, self.sound):
                self.login_signin_state = "log in"
                self.username_signin_textbox.text = ""
                self.password_signin_textbox.text = ""
            self.box_login_signin.draw(self.screen)
            self.box_signin.draw(self.screen)

            # Draw Textbox
            self.username_signin_textbox.draw(self.screen, COLOR.GREY)
            self.username_signin_textbox.draw_text(
                self.screen,
                COLOR.BLACK,
                is_password=False,
                censored=False,
                activated=False,
            )
            self.password_signin_textbox.draw(self.screen, COLOR.GREY)
            self.password_signin_textbox.draw_text(
                self.screen,
                COLOR.BLACK,
                is_password=True,
                censored=False,
                activated=False,
            )

            # Get input
            state = self.username_signin_textbox.get_text(
                self.screen,
                self.button_back,
                self.button_signin,
                event,
                sound_on=self.sound,
            )
            state = self.password_signin_textbox.get_text(
                self.screen,
                self.button_back,
                self.button_signin,
                event,
                is_password=True,
                censored=True,
                sound_on=self.sound,
            )

            if (
                self.button_signin.draw(self.screen, pos, event, self.sound)
                or state == "submit"
            ):
                new_username = self.username_signin_textbox.text
                new_password = self.password_signin_textbox.text
                if new_username == "" or new_password == "":
                    notification_text = self.font.render(
                        "Type something!", True, COLOR.RED
                    )
                    self.screen.blit(
                        notification_text, (SCREEN_WIDTH * 0.435, SCREEN_HEIGHT * 0.52)
                    )
                    pygame.display.update()
                    pygame.time.wait(1000)
                else:
                    self.login, self.user_id = data.register(new_username, new_password)

                    if self.login == True:
                        self.username = new_username
                        self.game_state = "main menu"
                        # self.get_saved_data()
                    else:
                        notification_text1 = self.font.render(
                            "This username is already in use.", True, COLOR.RED
                        )
                        notification_text2 = self.font.render(
                            "Please pick another.", True, COLOR.RED
                        )
                        self.screen.blit(
                            notification_text1,
                            (SCREEN_WIDTH * 0.37, SCREEN_HEIGHT * 0.52),
                        )
                        self.screen.blit(
                            notification_text2,
                            (SCREEN_WIDTH * 0.42, SCREEN_HEIGHT * 0.56),
                        )
                        pygame.display.update()
                        pygame.time.wait(1000)

        if (
            self.button_back.draw(self.screen, pos, event, self.sound)
            or state == "back"
        ):
            self.game_state = "main menu"
            self.login_signin_state = "log in"

        if self.game_state == "main menu":
            self.username_login_textbox.text = ""
            self.username_signin_textbox.text = ""
            self.password_login_textbox.text = ""
            self.password_signin_textbox.text = ""

    def draw_leaderboard(self, event):
        pos = pygame.mouse.get_pos()

        self.background_leaderboard.draw(self.screen)
        if self.leaderboard_state == "easy":
            if self.button_leaderboard_medium.draw(self.screen, pos, event, self.sound):
                self.leaderboard_state = "medium"
            if self.button_leaderboard_hard.draw(self.screen, pos, event, self.sound):
                self.leaderboard_state = "hard"
            self.leaderboard.draw(self.screen)
            self.leaderboard_easy.draw(self.screen)
            records = data.leaderboard(mode="EASY")
            for i in range(min(len(records), DISPLAY.RECORD_LIMIT)):
                username = self.font.render(records[i][0], True, COLOR.BLACK)
                time = self.font.render(records[i][1], True, COLOR.BLACK)
                steps = self.font.render(str(records[i][2]), True, COLOR.BLACK)
                self.screen.blit(
                    username,
                    (
                        (
                            self.leaderboard.x_coord
                            - username.get_rect().width * 0.5
                            - self.leaderboard.modified_width * 0.22,
                            self.leaderboard.y_coord
                            - self.leaderboard.modified_height * 0.13
                            + self.background_leaderboard.modified_height * 0.07 * i,
                        )
                    ),
                )
                self.screen.blit(
                    steps,
                    (
                        (
                            self.leaderboard.x_coord
                            + self.leaderboard.modified_width * 0.01,
                            self.leaderboard.y_coord
                            - self.leaderboard.modified_height * 0.13
                            + self.background_leaderboard.modified_height * 0.07 * i,
                        )
                    ),
                )
                self.screen.blit(
                    time,
                    (
                        (
                            self.leaderboard.x_coord
                            + self.leaderboard.modified_width * 0.2,
                            self.leaderboard.y_coord
                            - self.leaderboard.modified_height * 0.13
                            + self.background_leaderboard.modified_height * 0.07 * i,
                        )
                    ),
                )

        if self.leaderboard_state == "medium":
            if self.button_leaderboard_easy.draw(self.screen, pos, event, self.sound):
                self.leaderboard_state = "easy"
            if self.button_leaderboard_hard.draw(self.screen, pos, event, self.sound):
                self.leaderboard_state = "hard"
            self.leaderboard.draw(self.screen)
            self.leaderboard_medium.draw(self.screen)
            records = data.leaderboard(mode="MEDIUM")
            for i in range(min(len(records), DISPLAY.RECORD_LIMIT)):
                username = self.font.render(records[i][0], True, COLOR.BLACK)
                time = self.font.render(records[i][1], True, COLOR.BLACK)
                steps = self.font.render(str(records[i][2]), True, COLOR.BLACK)
                self.screen.blit(
                    username,
                    (
                        (
                            self.leaderboard.x_coord
                            - username.get_rect().width * 0.5
                            - self.leaderboard.modified_width * 0.22,
                            self.leaderboard.y_coord
                            - self.leaderboard.modified_height * 0.13
                            + self.background_leaderboard.modified_height * 0.07 * i,
                        )
                    ),
                )
                self.screen.blit(
                    steps,
                    (
                        (
                            self.leaderboard.x_coord
                            + self.leaderboard.modified_width * 0.01,
                            self.leaderboard.y_coord
                            - self.leaderboard.modified_height * 0.13
                            + self.background_leaderboard.modified_height * 0.07 * i,
                        )
                    ),
                )
                self.screen.blit(
                    time,
                    (
                        (
                            self.leaderboard.x_coord
                            + self.leaderboard.modified_width * 0.2,
                            self.leaderboard.y_coord
                            - self.leaderboard.modified_height * 0.13
                            + self.background_leaderboard.modified_height * 0.07 * i,
                        )
                    ),
                )

        if self.leaderboard_state == "hard":
            if self.button_leaderboard_easy.draw(self.screen, pos, event, self.sound):
                self.leaderboard_state = "easy"
            if self.button_leaderboard_medium.draw(self.screen, pos, event, self.sound):
                self.leaderboard_state = "medium"
            self.leaderboard.draw(self.screen)
            self.leaderboard_hard.draw(self.screen)
            records = data.leaderboard(mode="HARD")
            for i in range(min(len(records), DISPLAY.RECORD_LIMIT)):
                username = self.font.render(records[i][0], True, COLOR.BLACK)
                time = self.font.render(records[i][1], True, COLOR.BLACK)
                steps = self.font.render(str(records[i][2]), True, COLOR.BLACK)
                self.screen.blit(
                    username,
                    (
                        (
                            self.leaderboard.x_coord
                            - username.get_rect().width * 0.5
                            - self.leaderboard.modified_width * 0.22,
                            self.leaderboard.y_coord
                            - self.leaderboard.modified_height * 0.13
                            + self.background_leaderboard.modified_height * 0.07 * i,
                        )
                    ),
                )
                self.screen.blit(
                    steps,
                    (
                        (
                            self.leaderboard.x_coord
                            + self.leaderboard.modified_width * 0.01,
                            self.leaderboard.y_coord
                            - self.leaderboard.modified_height * 0.13
                            + self.background_leaderboard.modified_height * 0.07 * i,
                        )
                    ),
                )
                self.screen.blit(
                    time,
                    (
                        (
                            self.leaderboard.x_coord
                            + self.leaderboard.modified_width * 0.2,
                            self.leaderboard.y_coord
                            - self.leaderboard.modified_height * 0.13
                            + self.background_leaderboard.modified_height * 0.07 * i,
                        )
                    ),
                )

        if self.button_back.draw(self.screen, pos, event, self.sound):
            self.game_state = "main menu"
            self.leaderboard_state = "easy"

    def draw_new_game(self, event):
        pos = pygame.mouse.get_pos()

        self.background_new_game.draw(self.screen)
        if self.skip_login == False and self.login == False:
            self.box_login_confirm.draw(self.screen)
            if self.button_yes.draw(self.screen, pos, event, self.sound):
                self.game_state = "login signin"
            if self.button_no.draw(self.screen, pos, event, self.sound):
                self.skip_login = True
            if self.button_back.draw(self.screen, pos, event, self.sound):
                self.game_state = "main menu"
                self.skip_login = False
        else:
            if self.new_game_state == "choose difficulty":
                self.choose_difficulty.draw(self.screen)
                if self.spawning == "":
                    if self.button_easy.image_rect.collidepoint(pos):
                        self.mood_easy.draw(self.screen)
                    if self.button_medium.image_rect.collidepoint(pos):
                        self.mood_medium.draw(self.screen)
                    if self.button_hard.image_rect.collidepoint(pos):
                        self.mood_hard.draw(self.screen)

                if self.button_easy.draw(self.screen, pos, event, self.sound):
                    self.spawning = "choose mode"
                    self.difficulty = DIFFICULTY.EASY
                elif self.button_medium.draw(self.screen, pos, event, self.sound):
                    self.spawning = "choose mode"
                    self.difficulty = DIFFICULTY.MEDIUM
                elif self.button_hard.draw(self.screen, pos, event, self.sound):
                    self.spawning = "choose mode"
                    self.difficulty = DIFFICULTY.HARD

                if self.difficulty == DIFFICULTY.EASY:
                    self.mood_easy.draw(self.screen)
                if self.difficulty == DIFFICULTY.MEDIUM:
                    self.mood_medium.draw(self.screen)
                if self.difficulty == DIFFICULTY.HARD:
                    self.mood_hard.draw(self.screen)

                if self.spawning == "choose mode":
                    self.box_choose_settings.draw(self.screen)
                    if self.button_random.draw(self.screen, pos, event, self.sound):
                        self.spawning = "random"
                        self.game_state = "ingame"
                        if self.music == True:
                            if self.difficulty == DIFFICULTY.EASY:
                                self.music_player.play_music("easy mode")
                            if self.difficulty == DIFFICULTY.MEDIUM:
                                self.music_player.play_music("medium mode")
                            if self.difficulty == DIFFICULTY.HARD:
                                self.music_player.play_music("hard mode")

                    if self.button_manual.draw(self.screen, pos, event, self.sound):
                        self.spawning = "manual"
                        self.game_state = "ingame"
                        if self.music == True:
                            if self.difficulty == DIFFICULTY.EASY:
                                self.music_player.play_music("easy mode")
                            if self.difficulty == DIFFICULTY.MEDIUM:
                                self.music_player.play_music("medium mode")
                            if self.difficulty == DIFFICULTY.HARD:
                                self.music_player.play_music("hard mode")

                    if self.energy_mode == False:
                        if self.button_uncheck_energy_mode.draw(
                            self.screen, pos, event, self.sound
                        ):
                            self.energy_mode = True
                            if self.insane_mode == True:
                                self.button_uncheck_insane_mode.draw(
                                    self.screen, pos, event, self.sound
                                )
                                self.insane_mode = False

                    else:
                        if self.button_check_energy_mode.draw(
                            self.screen, pos, event, self.sound
                        ):
                            self.energy_mode = False

                    if self.insane_mode == False:
                        if self.button_uncheck_insane_mode.draw(
                            self.screen, pos, event, self.sound
                        ):
                            self.insane_mode = True
                            if self.energy_mode == True:
                                self.button_uncheck_energy_mode.draw(
                                    self.screen, pos, event, self.sound
                                )
                                self.energy_mode = False
                    else:
                        if self.button_check_insane_mode.draw(
                            self.screen, pos, event, self.sound
                        ):
                            self.insane_mode = False

                    if self.maze_visualizer == False:
                        if self.button_uncheck_visualizer.draw(
                            self.screen, pos, event, self.sound
                        ):
                            self.maze_visualizer = True
                    else:
                        if self.button_check_visualizer.draw(
                            self.screen, pos, event, self.sound
                        ):
                            self.maze_visualizer = False
                    
                    if self.maze_generate_algo == 'HAK':
                        self.button_check_hak.draw(self.screen, pos, event, self.sound)
                        if self.button_uncheck_dfs.draw(self.screen, pos, event, self.sound):
                            self.maze_generate_algo = 'DFS'
                    elif self.maze_generate_algo == 'DFS':
                        self.button_check_dfs.draw(self.screen, pos, event, self.sound)
                        if self.button_uncheck_hak.draw(self.screen, pos, event, self.sound):
                            self.maze_generate_algo = 'HAK'

                if self.button_back.draw(self.screen, pos, event, self.sound):
                    self.game_state = "main menu"
                    self.skip_login = False
                    self.energy_mode = False
                    self.insane_mode = False
                    self.maze_generate_algo = 'HAK'
                    self.maze_visualizer = False
                    self.spawning = ""

    def draw_load_game(self, event):
        pos = pygame.mouse.get_pos()

        self.background_load_game.draw(self.screen)
        # if self.load_game_state == "easy":
        #     self.easy_snapshot_1.draw(self.screen)
        #     self.saveslot_easy_1.manage_save(self.screen, pos, event)
        #     self.saveslot_easy_2.manage_save(self.screen, pos, event)
        #     if self.button_easy_load_game.draw(self.screen, pos, event, self.sound):
        #         self.load_game_state = "medium"
        # if self.load_game_state == "medium":
        #     self.saveslot_medium_1.manage_save(self.screen, pos, event)
        #     self.saveslot_medium_2.manage_save(self.screen, pos, event)
        #     if self.button_medium_load_game.draw(self.screen, pos, event, self.sound):
        #         self.load_game_state = "hard"
        # if self.load_game_state == "hard":
        #     self.saveslot_hard_1.manage_save(self.screen, pos, event)
        #     self.saveslot_hard_2.manage_save(self.screen, pos, event)
        #     if self.button_hard_load_game.draw(self.screen, pos, event, self.sound):
        #         self.load_game_state = "easy"
        # if self.button_back.draw(self.screen, pos, event, self.sound):
        #     self.game_state = 'main menu'
        #     self.music_player.play_music(self.game_state)
        #     self.skip_login = False
        
        
        # snapshots = [snapshot]
        
        if self.load_game_state == 'list':
            # for snapshot in snapshots:
            # calculate coordinates of snapshots to blit
 
            if self.box_save_frame_1.draw(self.screen, pos, event):
                self.load_game_state = 'detail'
                self.load_id = 0
            if self.box_save_frame_2.draw(self.screen, pos, event):
                self.load_game_state = 'detail'
                self.load_id = 1
            if self.box_save_frame_3.draw(self.screen, pos, event):
                self.load_game_state = 'detail'
                self.load_id = 2
            if self.box_save_frame_4.draw(self.screen, pos, event):
                self.load_game_state = 'detail'
                self.load_id = 3
            if self.box_save_frame_5.draw(self.screen, pos, event):
                self.load_game_state = 'detail'
                self.load_id = 4
            if self.box_save_frame_6.draw(self.screen, pos, event):
                self.load_game_state = 'detail'
                self.load_id = 5
            for snapshot in self.snapshots:
                snapshot[0].draw(self.screen)
        
        if self.load_id >= len(self.saved_games):
                self.load_game_state = 'list'
                self.load_id = DISPLAY.SAVE_LIMIT
        
        if self.load_game_state == 'detail':
                
            self.box_save_profile.draw(self.screen)

            difficulty = self.load_game_difficulty_font.render(self.saved_games[self.load_id][3], True, COLOR.BLACK)
            
            game_id = self.load_game_content_font.render(f'Game ID:\t{self.saved_games[self.load_id][0]}', True, COLOR.BLACK)
            
            time = self.load_game_content_font.render(f'Time :\t{self.saved_games[self.load_id][1]}', True, COLOR.BLACK)
            
            steps = self.load_game_content_font.render(f'Steps:\t{self.saved_games[self.load_id][2]}', True, COLOR.BLACK)
            
            
            mode = "Normal" 
            if self.saved_games[self.load_id][4]: mode = "Energy"
            if self.saved_games[self.load_id][5]: mode = "Insane"
            game_mode = self.load_game_content_font.render(f'Mode: {mode}', True, COLOR.BLACK)
           
            
            self.screen.blit(difficulty, (self.box_save_profile.x_coord - self.box_save_profile.modified_width * 0.25 - difficulty.get_rect().width * 0.5, self.box_save_profile.y_coord - self.box_save_profile.modified_height * 0.475))
            self.screen.blit(game_id, (self.box_save_profile.x_coord + self.box_save_profile.modified_width * 0.07, self.box_save_profile.y_coord - self.box_save_profile.modified_height * 0.4))
            self.screen.blit(time, (self.box_save_profile.x_coord + self.box_save_profile.modified_width * 0.07, self.box_save_profile.y_coord - self.box_save_profile.modified_height * 0.25))
            self.screen.blit(steps, (self.box_save_profile.x_coord + self.box_save_profile.modified_width * 0.07, self.box_save_profile.y_coord - self.box_save_profile.modified_height * 0.1))
            self.screen.blit(game_mode, (self.box_save_profile.x_coord + self.box_save_profile.modified_width * 0.07, self.box_save_profile.y_coord + self.box_save_profile.modified_height * 0.05))

            self.snapshots[self.load_id][1].draw(self.screen)
            if self.button_load.draw(self.screen, pos, event, self.sound):
                """ LOAD SAVE """
                self.load_game_state = 'list'
                return self.saved_games[self.load_id][0]
            if self.button_delete.draw(self.screen, pos, event, self.sound):
                data.remove_game_save(self.saved_games[self.load_id][0])
                self.get_saved_data()
                self.load_game_state = 'list'
                """ DELETE SAVE """
            
        if self.button_back.draw(self.screen, pos, event, self.sound):
            if self.load_game_state == 'list':
                self.game_state = 'main menu'
                self.music_player.play_music(self.game_state)
                self.skip_login = False
            if self.load_game_state == 'detail':
                self.load_game_state = 'list'
        
        return None
        
    def fade_transition(self, image_1, image_2):
        for i in range(0, 255, 3):
            image_1.set_alpha(i)
            image_2.set_alpha(255 - i)

            image_1.draw(self.screen)
            image_2.draw(self.screen)

            pygame.display.update()
            
        image_2.set_alpha(255) 
        image_1.set_alpha(255) 
        
