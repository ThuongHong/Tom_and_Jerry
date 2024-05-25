import pygame
from menu_objects import button
from menu_objects import graphic

class SaveSlot:
    def __init__(self, x_coord, y_coord, frame_image, overlay_image, load_image, delete_image, sound, scale=1, hover_scale=1.1):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.frame = button.Button(x_coord, y_coord, frame_image, sound, scale, hover_scale)
        self.overlay = graphic.Graphic(self.x_coord, self.y_coord, overlay_image, scale * 0.9)
        
        frame_center_x, frame_center_y = self.frame.image_rect.center
        
        self.button_load = button.Button(frame_center_x, frame_center_y * 0.8, load_image, sound, scale=0.22, hover_scale=0.25)
        self.button_delete = button.Button(frame_center_x, frame_center_y * 1.2, delete_image, sound, scale=0.22, hover_scale=0.25)
        self.manage = False
        self.snapshot = None
        
    """ PSEUDO CODE """    
    def check_user_save(self, username):
        if username.snapshot in username.data:
            self.snapshot = graphic.Graphic(self.x_coord, self.y_coord, username.snapshot)

    def delete_save(self, username):
        self.snapshot = None
    
    def load_save(self, username):
        pass
    """"""
    
    def manage_save(self, surface, pos, event, sound_on = True):
        """ PSEUDO CODE """
        if self.snapshot is not None:
            self.snapshot.draw(surface)
        """"""
        
        if self.manage == True:
            if not self.frame.image_rect.collidepoint(pos) and pygame.mouse.get_pressed()[0] == 1:
                self.manage = False
            self.overlay.draw(surface)
            if self.button_load.draw(surface, pos, event, sound_on):
                pass
                # do something here with save file
            if self.button_delete.draw(surface, pos, event, sound_on):
                pass
                # do something here with save file
        if self.frame.draw(surface, pos, event, sound_on):# and self.snapshot == True:
            self.manage = True
            