from game_structure.maze import Maze
from game_structure.utility import get_position_after_move, get_diffirent_coord, get_direction
from solving_maze.solving_maze import solve_maze
from algorithm.draw_utility import mark_grid
from algorithm.BDFS import BDFS


import pygame
import os

class Character(pygame.sprite.Sprite):
    def __init__(self,
                #  character_maze: Maze,,
                 start_position: tuple[int],
                 grid_size: int,
                 direction = None,
                 img_scale: int = 1,
                 screen= None,
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
                
        self.is_center = False

        self.energy_mode = False
        self.hp = 0

    @property
    def grid_size(self):
        return self._grid_size * self.scale
    
    # @property
    # def hp(self):
    #     return self._hp - self.step_moves

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

        self.step_moves += 1
        
    def normal_move(self, sprites, direction: str, maze, energy= None):
        if self.is_valid_move(direction= direction, grids= maze.grids) and self.hp >= 0: 
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
                # maze.image_draw(self.screen)
                self.screen.blit(self.image, self.rect)

                scale_surface = pygame.transform.scale(self.screen, self.screen_vector * self.scale)
                # scale_surface = pygame.transform.rotozoom(self.screen, 0, self.scale)
                scale_rect = scale_surface.get_rect(center= (500, 325))

                self.window_screen.blit(scale_surface, scale_rect.topleft + self.scale_surface_offset)
                                    
                pygame.display.update()
                
                current_sprite += len(sprites) / self._grid_size

                # if current_sprite > len(sprites) - 1 :
                #     break

            self.update()

            self.step_moves += 1

            if self.energy_mode:
                self.hp -= 1

class Tom(pygame.sprite.Sprite):
    YELLOW = (255, 255, 0)
    def __init__(self,
                #  character_maze: Maze,,
                 start_position: tuple[int],
                 grid_size: int,
                 direction = None,
                 img_scale: int = 1,
                 screen= None,
                 window_screen= None,
                 img_directory: str = r'./images/Tom'):
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
                
        self.is_center = False

        self.energy_mode = False
        self.hp = 1
        
        self.current_sprite = 0

        self.animation_images = {
            'Left': [],
            'Right': [],
            'Up': [],
            'Down': [],
            'StandLeft': [],
            'StandRight': [],
            'StandUp': [],
            'StandDown': []
        }

        # Load all the image
        for folder in os.listdir(img_directory, ):
            for file in os.listdir(os.path.join(img_directory, folder)):
                tmp_img = pygame.image.load(os.path.join(img_directory, folder, file))
                
                tmp_img_height = tmp_img.get_height()
                tmp_img_width = tmp_img.get_width()
                
                bigger_size = tmp_img_height if (tmp_img_height > tmp_img_width) else tmp_img_width
                scale_index = bigger_size / self.grid_size
                
                image = pygame.transform.scale(tmp_img, (tmp_img_width / scale_index, tmp_img_height / scale_index))
                # image = pygame.transform.rotozoom(tmp_img, 0, 1 / scale_index)

                self.animation_images[folder].append(image)
        # Set default image
        # Rect will be draw while we using GroupSingle then add this character
        self.image = self.animation_images['StandDown'][0]

        real_img_size = (self._grid_size / 28) * bigger_size
        coord_adjust = (self._grid_size - real_img_size) / 2

        self.rect = self.image.get_rect(topleft= (self.position[0] * self._grid_size + coord_adjust,
                                                  self.position[1] * self._grid_size + 40 - coord_adjust * 2))        

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

        self.step_moves += 1
        
    def normal_move(self, sprites, direction: str, maze, energy_grp= None):
        if self.is_valid_move(direction= direction, grids= maze.grids) and self.hp > 0: 
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
                if energy_grp: energy_grp.draw(self.screen)
                # maze.image_draw(self.screen)
                self.screen.blit(self.image, self.rect)

                scale_surface = pygame.transform.scale(self.screen, self.screen_vector * self.scale)
                # scale_surface = pygame.transform.rotozoom(self.screen, 0, self.scale)
                scale_rect = scale_surface.get_rect(center= (500, 325))

                self.window_screen.blit(scale_surface, scale_rect.topleft + self.scale_surface_offset)
                                    
                pygame.display.update()
                
                current_sprite += len(sprites) / self._grid_size

                # if current_sprite > len(sprites) - 1 :
                #     break

            if energy_grp:
                for energy_item in energy_grp:
                    energy_item.update(self, energy_grp)
                # for energy in pygame.sprite.spritecollide(
                #     sprite= self,
                #     group= energy,
                #     dokill= 1
                # ):
                #     self.hp += energy.hp

            self.step_moves += 1

            if self.energy_mode:
                self.hp -= 1

    def centering(self, maze):
        self.offset = pygame.math.Vector2()
        half_w = self.screen.get_size()[0] // 2
        half_h = self.screen.get_size()[1] // 2
        
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
               energy_grp= None,
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
                # pass
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
            self.normal_move(self.animation_images['Up'], direction= direction, maze= maze, energy_grp= energy_grp)
        elif direction == 'B':
            self.direction = 'B'
            self.normal_move(self.animation_images['Down'], direction= direction, maze= maze, energy_grp= energy_grp)
        elif direction == 'L':
            self.direction = 'L'
            self.normal_move(self.animation_images['Left'], direction= direction, maze= maze, energy_grp= energy_grp)
        elif direction == 'R':
            self.direction = 'R'
            self.normal_move(self.animation_images['Right'], direction= direction, maze= maze, energy_grp= energy_grp)
        elif direction == None:
            if self.direction == 'T':
                self.current_sprite += 0.1
                if int(self.current_sprite) >= len(self.animation_images['StandUp']):
                    self.current_sprite = 0
                self.image = self.animation_images['StandUp'][int(self.current_sprite)]
            elif self.direction == 'B':
                self.current_sprite += 0.1
                if int(self.current_sprite) >= len(self.animation_images['StandDown']):
                    self.current_sprite = 0
                self.image = self.animation_images['StandDown'][int(self.current_sprite)]
            elif self.direction == 'L':
                self.current_sprite += 0.1
                if int(self.current_sprite) >= len(self.animation_images['StandLeft']):
                    self.current_sprite = 0
                self.image = self.animation_images['StandLeft'][int(self.current_sprite)]
            elif self.direction == 'R':
                self.current_sprite += 0.1
                if int(self.current_sprite) >= len(self.animation_images['StandRight']):
                    self.current_sprite = 0
                self.image = self.animation_images['StandRight'][int(self.current_sprite)]
            else:
                self.current_sprite += 0.1
                if int(self.current_sprite) >= len(self.animation_images['StandDown']):
                    self.current_sprite = 0
                self.image = self.animation_images['StandDown'][int(self.current_sprite)]

        # If show_solution so draw_solution
        if show_solution:
            solution = solve_maze(player= self, 
                                  maze= maze, 
                                  algorithm= algorithm)                
            self.draw_solution(solution= solution,
                                grids= maze.grids
                                )  
           
        # print(self.hp)
        # More feature like draw, update img, state of character

    def set_hp(self, first_energy: tuple[int], grids: dict):
        self.energy_mode = True
        self.hp = len(
            BDFS(
                grids= grids,
                player_current_position= self.position,
                player_winning_position= first_energy,
                algorithm= 'BFS'
            )
        ) + 3