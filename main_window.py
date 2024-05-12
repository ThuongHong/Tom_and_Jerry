import pygame
import visualize
from constants.INTERFACE_CONSTANTS import DISPLAY

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
game_window = visualize.GameScreen(screen, image_source, sound_source)

while game_window.running:
    clock.tick(DISPLAY.FPS)
    if game_window.game_state == 'main menu':
        game_window.draw_main_menu()
    elif game_window.game_state == 'new game':
        game_window.draw_new_game()
    elif game_window.game_state == 'load game':
        game_window.draw_load_game()
    elif game_window.game_state == 'leaderboard':
        game_window.draw_leaderboard()
    elif game_window.game_state == 'login signin':
        game_window.draw_login_signin()
        
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_window.running = False
            
    pygame.display.update()
    
pygame.quit()