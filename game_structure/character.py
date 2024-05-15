from game_structure.maze import Maze
from game_structure.utility import get_position_after_move, get_diffirent_coord, get_direction
from solving_maze.solving_maze import solve_maze
from algorithm.draw_utility import mark_grid


import pygame
import os

class Character(pygame.sprite.Sprite):
    def __init__(self,
                #  character_maze: Maze,,
                 start_position: tuple[int],
                 grid_size: int,
                 imgs_directory: str = None,
                 direction = None,
                 img_scale: int = 1,
                 screen= None,
                 group= None,
                 window_screen= None):
        super().__init__()

        # self.Maze = character_maze
        # self.position = self.Maze.start_position
        self.position = start_position
        # Default
        self._grid_size = grid_size
        self.scale = img_scale
        self.direction = direction
        self.screen = screen
        self.screen_vector = pygame.math.Vector2(self.screen.get_size())

        self.window_screen = window_screen

        self.scale_surface_offset = pygame.math.Vector2()

        self.step_moves = 0
        
        # Rect will be draw while we using GroupSingle then add this character
        img_tmp = pygame.image.load(r'./images/Tom/StandDown/1.png').convert_alpha()
        
        bigger_size = img_tmp.get_height() if (img_tmp.get_height() > img_tmp.get_width()) else img_tmp.get_width()
        scale_index = bigger_size / self.grid_size
        self.image = pygame.transform.rotozoom(img_tmp, 0, 1 / scale_index)

        real_img_size = (self._grid_size / 28) * bigger_size
        coord_adjust = (self._grid_size - real_img_size) / 2

        self.rect = self.image.get_rect(topleft= (self.position[0] * self._grid_size + coord_adjust,
                                                  self.position[1] * self._grid_size + 40 - coord_adjust * 2))
        
        self.is_center = False

    @property
    def grid_size(self):
        return self._grid_size * self.scale

    def set_scale(self, new_scale):
        self.scale = new_scale

    def is_valid_move(self, direction: str, grids) -> bool:
        if get_position_after_move(position= self.position,
                                   direction= direction) in grids[self.position].get_neighbors():
            return True
        return False
    
    def move(self, direction: str, maze):
        if self.is_valid_move(direction= direction, grids= maze.grids):
            self.position = get_position_after_move(position= self.position, direction= direction)
            
            move_coord = get_diffirent_coord(direction= direction, maze_grid_size= self.grid_size)
            # self.rect.topleft = self.rect.topleft + move_coord
            
            maze.update(offset_change= move_coord)

    #     # self.step_moves += 1
        
    def normal_move(self, sprites, direction: str, maze):
        if self.is_valid_move(direction= direction, grids= maze.grids): 
            self.position = get_position_after_move(position= self.position, direction= direction)
            
            move_coord = get_diffirent_coord(direction= direction, maze_grid_size= self.grid_size)
            move_coord = move_coord / self.grid_size
            
            current_sprite = 0
            # Loop 28 frame
            for _ in range(self._grid_size):
            # while int(current_sprite) < len(sprites) - 1:
                self.image = sprites[int(current_sprite)]
                self.rect.topleft = self.rect.topleft + move_coord 
                
                maze.draw(self.screen)
                self.screen.blit(self.image, self.rect)

                scale_surface = pygame.transform.scale(self.screen, self.screen_vector * self.scale)
                # scale_surface = pygame.transform.rotozoom(self.screen, 0, self.scale)
                scale_rect = scale_surface.get_rect(center= (500, 325))

                self.window_screen.blit(scale_surface, scale_rect.topleft + self.scale_surface_offset)
                                    
                pygame.display.update()
                
                current_sprite += len(sprites) / self._grid_size

                # if current_sprite > len(sprites) - 1 :
                #     break

            self.step_moves += 1

class Tom(Character):
    YELLOW = (255, 255, 0)

    def __init__(self,
                #  maze: Maze,
                 start_position: tuple[int],
                 grid_size: int,
                 scale: int,
                 screen= None,
                 window_screen = None
                 ):
        super().__init__(start_position= start_position,
                         grid_size= grid_size,
                         img_scale= scale,
                         screen= screen,
                         window_screen=window_screen)
        self.current_sprite = 0

        folder_left = r'./images/Tom/Left'
        folder_right = r'./images/Tom/Right'
        folder_up = r'./images/Tom/Up'
        folder_down = r'./images/Tom/Down'
        folder_stand = r'./images/Tom/Stand'

        folder_stand_left = r'./images/Tom/StandLeft'
        folder_stand_right = r'./images/Tom/StandRight'
        folder_stand_up = r'./images/Tom/StandUp'
        folder_stand_down = r'./images/Tom/StandDown'

        self.sprites_left = []
        self.sprites_right = []
        self.sprites_up = []
        self.sprites_down = []

        self.sprites_stand_left = []
        self.sprites_stand_right = []
        self.sprites_stand_up = []
        self.sprites_stand_down = []

        for file in os.listdir(folder_left):
            tmp_img = pygame.image.load(folder_left + '/' + file)
            bigger_size = tmp_img.get_height() if (tmp_img.get_height() > tmp_img.get_width()) else tmp_img.get_width()
            scale_index = bigger_size / self.grid_size
            image = pygame.transform.rotozoom(tmp_img, 0, 1 / scale_index)
            
            self.sprites_left.append(image)
        for file in os.listdir(folder_right):
            tmp_img = pygame.image.load(folder_right + '/' + file)
            bigger_size = tmp_img.get_height() if (tmp_img.get_height() > tmp_img.get_width()) else tmp_img.get_width()
            scale_index = bigger_size / self.grid_size
            image = pygame.transform.rotozoom(tmp_img, 0, 1 / scale_index)

            self.sprites_right.append(image)
        for file in os.listdir(folder_up):
            tmp_img = pygame.image.load(folder_up + '/' + file)
            bigger_size = tmp_img.get_height() if (tmp_img.get_height() > tmp_img.get_width()) else tmp_img.get_width()
            scale_index = bigger_size / self.grid_size
            image = pygame.transform.rotozoom(tmp_img, 0, 1 / scale_index)

            self.sprites_up.append(image)
        for file in os.listdir(folder_down):
            tmp_img = pygame.image.load(folder_down + '/' + file)
            bigger_size = tmp_img.get_height() if (tmp_img.get_height() > tmp_img.get_width()) else tmp_img.get_width()
            scale_index = bigger_size / self.grid_size
            image = pygame.transform.rotozoom(tmp_img, 0, 1 / scale_index)

            self.sprites_down.append(image)     

        ######## STAND ANIMATION IMPORT ########
        for file in os.listdir(folder_stand_left):
            tmp_img = pygame.image.load(folder_stand_left + '/' + file)
            bigger_size = tmp_img.get_height() if (tmp_img.get_height() > tmp_img.get_width()) else tmp_img.get_width()
            scale_index = bigger_size / self.grid_size
            image = pygame.transform.rotozoom(tmp_img, 0, 1 / scale_index)

            self.sprites_stand_left.append(image)
        for file in os.listdir(folder_stand_right):
            tmp_img = pygame.image.load(folder_stand_right + '/' + file)
            bigger_size = tmp_img.get_height() if (tmp_img.get_height() > tmp_img.get_width()) else tmp_img.get_width()
            scale_index = bigger_size / self.grid_size
            image = pygame.transform.rotozoom(tmp_img, 0, 1 / scale_index)

            self.sprites_stand_right.append(image)
        for file in os.listdir(folder_stand_up):
            tmp_img = pygame.image.load(folder_stand_up + '/' + file)
            bigger_size = tmp_img.get_height() if (tmp_img.get_height() > tmp_img.get_width()) else tmp_img.get_width()
            scale_index = bigger_size / self.grid_size
            image = pygame.transform.rotozoom(tmp_img, 0, 1 / scale_index)

            self.sprites_stand_up.append(image)
        for file in os.listdir(folder_stand_down):
            tmp_img = pygame.image.load(folder_stand_down + '/' + file)
            bigger_size = tmp_img.get_height() if (tmp_img.get_height() > tmp_img.get_width()) else tmp_img.get_width()
            scale_index = bigger_size / self.grid_size
            image = pygame.transform.rotozoom(tmp_img, 0, 1 / scale_index)

            self.sprites_stand_down.append(image)
        

    def centering(self, maze):
        self.offset = pygame.math.Vector2()
        # half_w = 1000 // 2
        half_w = self.screen.get_size()[0] // 2
        half_h = self.screen.get_size()[1] // 2
        # half_h = 650 // 2
        self.offset.x = self.rect.centerx - half_w
        self.offset.y = self.rect.centery - half_h
        
        # self.rect.topleft = self.rect.topleft - self.offset

        for grid in maze.sprites():
            grid.offset += self.offset

        self.is_center = True

    def draw_solution(self, 
                      solution: list,
                      grids = None):
        """This method will draw a line from current position of Tom to the end position

        Args:
            solution (list): This solution include move and the grid after move
            grids (_type_, optional): Take the information of grid like coord to draw. Defaults to None.
        """
        # If do not have solution a.k.a you in the right spot
        if not solution: return

        while solution:
            # Iterate for all grir and mark it
            current_grid = solution.pop(0)[1]
            mark_grid(grids= grids,
                      current_grid= current_grid,
                      screen= self.screen,
                      COLOR= (255, 255, 0))

        # pygame.display.update()
    def update(self, maze,
               scale: int = None,
               offset: int = None,
               direction: str = None, 
               show_solution: bool = False, 
               algorithm: str = 'DFS',
                **kwargs) -> bool:
        """Update state of player

        Args:
            scale (float): current_scale
            direction (str): If want to update move
            draw_solution (pygame.Surface): Given screen if want to draw solution
        """
        # May be using for loop here, update later
        # If want to zoom change the scale -> If that scale != current scale zoom player
        # if not self.is_center: 
        #     self.centering(maze)
        if offset:
            self.scale_surface_offset = offset
        if scale:
            if scale != self.scale:
                self.scale = scale
                # old_scale = self.scale

                # self.set_scale(scale)

                # self.image = pygame.transform.rotozoom(self.image, 0, self.scale / old_scale)

                # self.rect = self.image.get_rect(topleft= (self.position[0] * self.grid_size + 50,
                #                                           self.position[1] * self.grid_size + 50))
                
                # self.centering(maze)
                
        # If direction is given so move the player
        if direction == 'T':
            self.direction = 'T'
            self.normal_move(self.sprites_up, direction= direction, maze= maze)
        elif direction == 'B':
            self.direction = 'B'
            self.normal_move(self.sprites_down, direction= direction, maze= maze)
        elif direction == 'L':
            self.direction = 'L'
            self.normal_move(self.sprites_left, direction= direction, maze= maze)
        elif direction == 'R':
            self.direction = 'R'
            self.normal_move(self.sprites_right, direction= direction, maze= maze)
        elif direction == None:
            if self.direction == 'T':
                self.current_sprite += 0.1
                if int(self.current_sprite) >= len(self.sprites_stand_up):
                    self.current_sprite = 0
                self.image = self.sprites_stand_up[int(self.current_sprite)]
            elif self.direction == 'B':
                self.current_sprite += 0.1
                if int(self.current_sprite) >= len(self.sprites_stand_down):
                    self.current_sprite = 0
                self.image = self.sprites_stand_down[int(self.current_sprite)]
            elif self.direction == 'L':
                self.current_sprite += 0.1
                if int(self.current_sprite) >= len(self.sprites_stand_left):
                    self.current_sprite = 0
                self.image = self.sprites_stand_left[int(self.current_sprite)]
            elif self.direction == 'R':
                self.current_sprite += 0.1
                if int(self.current_sprite) >= len(self.sprites_stand_right):
                    self.current_sprite = 0
                self.image = self.sprites_stand_right[int(self.current_sprite)]
            else:
                self.current_sprite += 0.1
                if int(self.current_sprite) >= len(self.sprites_stand_down):
                    self.current_sprite = 0
                self.image = self.sprites_stand_down[int(self.current_sprite)]

        # If show_solution so draw_solution
        if show_solution:
            solution = solve_maze(player= self, 
                                  maze= maze, 
                                  algorithm= algorithm)                
            self.draw_solution(solution= solution,
                                grids= maze.grids
                                )  
           
        # More feature like draw, update img, state of character
