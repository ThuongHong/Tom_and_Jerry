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
FPS = 30

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

# images
images_source = 'images'


# sound
s = 'sound'
click_sound = pygame.mixer.Sound(os.path.join(s, 'click.ogg'))

# game window
game_window = visualize.GameScreen(screen, images_source)

while game_window.running:
    clock.tick(FPS)
    if game_window.game_state == 'main menu':
        game_window.draw_main_menu(click_sound)
    elif game_window.game_state == 'login signin':
        game_window.draw_login_signin(click_sound)
        
        
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # close button
            game_window.running = False
            
    pygame.display.update()
    
pygame.quit()