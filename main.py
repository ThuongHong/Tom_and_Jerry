import pygame

from menu_objects.game_menu import GameMenu
from launcher import Launcher

from CONSTANTS import DISPLAY

# initialize
pygame.init()
screen = pygame.display.set_mode((DISPLAY.SCREEN_WIDTH, DISPLAY.SCREEN_HEIGHT))
pygame.display.set_caption("Tam va Gia Huy")
clock = pygame.time.Clock()

# images
image_source = "images/UI"
# sounds
sound_source = "sounds"

# game window
game_menu = GameMenu(screen, image_source, sound_source)
game_launcher = Launcher(screen)

# load game handle
load_data = None

while game_menu.running:
    clock.tick(DISPLAY.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_menu.running = False

    if game_menu.game_state == "main menu":
        game_menu.draw_main_menu(event)
    elif game_menu.game_state == "new game":
        game_menu.draw_new_game(event)
    elif game_menu.game_state == "load game":
        load_data = game_menu.draw_load_game(event)
        if load_data is not None:
            game_menu.game_state = "ingame"
    elif game_menu.game_state == "leaderboard":
        game_menu.draw_leaderboard(event)
    elif game_menu.game_state == "login signin":
        game_menu.draw_login_signin(event)
    elif game_menu.game_state == "ingame":

        # Load game | New game
        if load_data is not None:
            game_launcher.load_game(
                *load_data, sound_on=game_menu.sound, music_on=game_menu.music
            )
            load_data = None
        else:
            game_launcher.new_game(
                maze_size=game_menu.difficulty,
                sound_on=game_menu.sound,
                music_on=game_menu.music,
                spawning=game_menu.spawning,
                energy=game_menu.energy_mode,
                user_id=game_menu.user_id,
                insane_mode=game_menu.insane_mode,
                maze_visualizer=game_menu.maze_visualizer,
                maze_generate_algo=game_menu.maze_generate_algo,
                full_save=game_menu.full_save,
                first_game_id=game_menu.first_game_id,
            )

        # Launch game
        game_launcher.launch()

        # Back to menu
        if game_launcher.saved:
            game_menu.get_saved_data()
        game_menu.game_state = "main menu"
        game_menu.skip_login = False
        game_menu.difficulty = ""
        game_menu.full_save = False
        game_menu.energy_mode = False
        game_menu.insane_mode = False
        game_menu.maze_generate_algo = "HAK"
        game_menu.maze_visualizer = False
        if game_menu.music:
            game_menu.music_player.play_music(game_menu.game_state)
        game_menu.fade_transition(
            game_menu.background_main_menu, game_launcher.background
        )

    pygame.display.update()

pygame.quit()
