import pygame
import os
import visualize

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = int(SCREEN_WIDTH * (9 / 16)) # 787
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BEIGE = (217, 211, 186)
FPS = 60

# Font
# font = pygame.font.SysFont('The fountain of wishes', 40)

# def draw_text(text, font, text_color, x_coord, y_coord):
#     img = font.render(text, True, text_color)
#     screen.blit(img, (x_coord, y_coord))

# initialize
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tam va Gia Huy')
clock = pygame.time.Clock()

# image
image_source = 'image'
# sound
sound_source = 'sound'

# game window
game_window = visualize.GameScreen(screen, image_source, sound_source)

while game_window.running:
    clock.tick(FPS)
    if game_window.game_state == 'main menu':
        game_window.draw_main_menu()
    elif game_window.game_state == 'login signin':
        game_window.draw_login_signin()
    elif game_window.game_state == 'new game':
        game_window.draw_newgame()
    elif game_window.game_state == 'leaderboard':
        game_window.draw_leaderboard()
        
        
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # close button
            game_window.running = False
            
    pygame.display.update()
    
pygame.quit()