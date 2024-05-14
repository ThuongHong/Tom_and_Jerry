import pygame
import os
import menu_objects.saveslot as saveslot
from menu_objects import saveslot
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
run = True

def create_img(image_source, image_name):
    image_name = image_name + '.png'
    return pygame.image.load(os.path.join(image_source, image_name)).convert_alpha()

sound = pygame.mixer.Sound(os.path.join(sound_source, 'click.ogg'))

frame_img = create_img(image_source, 'frame')
overlay_img = create_img(image_source, 'overlay')
button_load = create_img(image_source, 'button_load')
button_delete = create_img(image_source, 'button_delete')


test_saveslot = saveslot.SaveSlot(300,300, frame_img, overlay_img, button_load, button_delete, sound, scale=0.4, hover_scale=0.4)

while run:
    clock.tick(DISPLAY.FPS)
    screen.fill((255,255,255))
    pos = pygame.mouse.get_pos()
    test_saveslot.manage_save(screen, pos)
        
    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # close button
            run = False
            
    pygame.display.update()
    
pygame.quit()