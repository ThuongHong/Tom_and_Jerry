import pygame
import visualize
from launcher import Launcher

from CONSTANTS import DISPLAY

# initialize
pygame.init()
screen = pygame.display.set_mode((DISPLAY.SCREEN_WIDTH, DISPLAY.SCREEN_HEIGHT))
pygame.display.set_caption('Tam va Gia Huy')
clock = pygame.time.Clock()

# images
image_source = 'images/UI'
# sounds
sound_source = 'sounds'

# game window
game_menu = visualize.GameScreen(screen, image_source, sound_source)
game_launcher = Launcher(screen)

while game_menu.running:
    clock.tick(DISPLAY.FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_menu.running = False

    if game_menu.game_state == 'main menu':
        game_menu.draw_main_menu(event)
    elif game_menu.game_state == 'new game':
        game_menu.draw_new_game(event)
    elif game_menu.game_state == 'load game':
        game_menu.draw_load_game(event)
    elif game_menu.game_state == 'leaderboard':
        game_menu.draw_leaderboard(event)
    elif game_menu.game_state == 'login signin':
        game_menu.draw_login_signin(event)
    elif game_menu.game_state == 'ingame':
        game_launcher.init_setting(maze_size=game_menu.difficulty, sound_on=game_menu.sound,
                                   spawning=game_menu.spawning, 
                                   energy=game_menu.energy_mode, user_id= game_menu.user_id)
        game_launcher.launch()
        
        game_menu.game_state = 'main menu'
        game_menu.energy_mode = False
        game_menu.insane_mode = False
        game_menu.maze_visualizer = False
        game_menu.fade_transition(game_menu.background_main_menu, game_launcher.background)
            
    pygame.display.update()
    
pygame.quit()