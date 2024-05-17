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
image_source = 'images'
# sounds
sound_source = 'sounds'

# game window
game_menu = visualize.GameScreen(screen, image_source, sound_source)
game_launcher = Launcher(screen)

while game_menu.running:
    clock.tick(DISPLAY.FPS)
    if game_menu.game_state == 'main menu':
        game_menu.draw_main_menu()
    elif game_menu.game_state == 'new game':
        game_menu.draw_new_game()
    elif game_menu.game_state == 'load game':
        game_menu.draw_load_game()
    elif game_menu.game_state == 'leaderboard':
        game_menu.draw_leaderboard()
    elif game_menu.game_state == 'login signin':
        game_menu.draw_login_signin()
    elif game_menu.game_state == 'ingame':
        game_launcher.reset(game_menu.difficulty)
        game_launcher.launch()
        
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_menu.running = False
            
    pygame.display.update()
    
pygame.quit()