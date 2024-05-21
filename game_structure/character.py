from game_structure.maze import Maze
from game_structure.utility import get_position_after_move, get_diffirent_coord, mahathan_distance
from solving_maze.solving_maze import solve_maze
from algorithm.draw_utility import mark_grid
from algorithm.BDFS import BDFS

import pygame
import os

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
                 tom_img_directory: str = r'./images/Tom',
                 footprint_img_directory: str = r'./images/Footprint'):
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

        self.footprint_images = {
            'One': []
        }

        if footprint_img_directory:
            for folder in os.listdir(footprint_img_directory, ):
                for file in os.listdir(os.path.join(footprint_img_directory, folder)):
                    tmp_img = pygame.image.load(os.path.join(footprint_img_directory, folder, file))
                    
                    tmp_img_height = tmp_img.get_height()
                    tmp_img_width = tmp_img.get_width()
                    
                    bigger_size = tmp_img_height if (tmp_img_height > tmp_img_width) else tmp_img_width
                    scale_index = bigger_size / self.grid_size
                    
                    # image = pygame.transform.scale(tmp_img, (self.grid_size * 0.75, self.grid_size * 0.75))
                    image = pygame.transform.rotozoom(tmp_img, 0, 0.75)

                    self.footprint_images[folder].append(image)
            self.foot = self.footprint_images['One'][0]

        # Load all the image
        for folder in os.listdir(tom_img_directory, ):
            for file in os.listdir(os.path.join(tom_img_directory, folder)):
                tmp_img = pygame.image.load(os.path.join(tom_img_directory, folder, file))
                
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

        self.rect = self.image.get_rect(topleft= (self.position[0] * self._grid_size + coord_adjust * 2,
                                                  self.position[1] * self._grid_size - coord_adjust * 2))        

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
        
    def normal_move(self, sprites, direction: str, maze, energy_grp= None, jerrgy_grp= None, ui_grp= None):
        if self.is_valid_move(direction= direction, grids= maze.grids) and self.hp > 0: 
            self.position = get_position_after_move(position= self.position, direction= direction)
            
            move_coord = get_diffirent_coord(direction= direction, maze_grid_size= self.grid_size)
            move_coord = move_coord / self.grid_size
            pygame.event.clear()
            current_sprite = 0
            # Loop 28 frame
            for _ in range(self._grid_size):
            # while int(current_sprite) < len(sprites) - 1:
                ui_grp.background.draw(self.window_screen)
                self.image = sprites[int(current_sprite)]
                self.rect.topleft = self.rect.topleft + move_coord 
                
                maze.draw(self.screen)
                if energy_grp: energy_grp.draw(self.screen)
                jerrgy_grp.update()
                jerrgy_grp.draw(self.screen)
                
                # maze.image_draw(self.screen)
                self.screen.blit(self.image, self.rect)
                
                scale_surface = pygame.transform.scale(self.screen, self.screen_vector * self.scale)
                # scale_surface = pygame.transform.rotozoom(self.screen, 0, self.scale)
                scale_rect = scale_surface.get_rect(center= (self.window_screen.get_width() / 2, self.window_screen.get_height() / 2))

                self.window_screen.blit(scale_surface, scale_rect.topleft + self.scale_surface_offset) ###
                
                ui_grp.draw_ui()
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
                      grids = None,
                      footprint = None):
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
            if len(solution) > 0:
                mark_grid(grids= grids,
                        current_grid= current_grid,
                        screen= self.screen,
                        footprint= footprint,
                        COLOR= (255, 255, 0))

        # pygame.display.update()
    
    def update(self, 
               maze = None,
               scale: int = None,
               offset: int = None,
               direction: str = None, 
               show_solution: bool = False, 
               algorithm: str = 'DFS',
               energy_grp= None,
               jerry_grp= None,
               ui_grp= None,
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
            self.normal_move(self.animation_images['Up'], direction= direction, maze= maze, 
                             energy_grp= energy_grp, jerrgy_grp= jerry_grp, ui_grp= ui_grp)
        elif direction == 'B':
            self.direction = 'B'
            self.normal_move(self.animation_images['Down'], direction= direction, maze= maze, 
                             energy_grp= energy_grp, jerrgy_grp= jerry_grp, ui_grp= ui_grp)
        elif direction == 'L':
            self.direction = 'L'
            self.normal_move(self.animation_images['Left'], direction= direction, maze= maze, 
                             energy_grp= energy_grp, jerrgy_grp= jerry_grp, ui_grp= ui_grp)
        elif direction == 'R':
            self.direction = 'R'
            self.normal_move(self.animation_images['Right'], direction= direction, maze= maze, 
                             energy_grp= energy_grp, jerrgy_grp= jerry_grp, ui_grp= ui_grp)
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
                                grids= maze.grids,
                                footprint=self.foot
                                )  
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

class Jerry(Tom):
    def __init__(self,
                #  maze: Maze,
                 end_position: tuple[int],
                 grid_size: int,
                 img_scale: int = 1,
                 screen= None,
                 window_screen = None,
                 jerry_img_directory: str = r'./images/Jerry'
                 ):
        super().__init__(
            start_position= end_position,
            grid_size= grid_size,
            img_scale= img_scale,
            screen= screen,
            window_screen = window_screen,
            tom_img_directory= jerry_img_directory
        )
        
        # self.position = end_position
        # self._grid_size = grid_size
        # self.scale = img_scale
        # self.screen = screen
        # self.screen_vector = pygame.math.Vector2(self.screen.get_size())
        # self.window_screen = window_screen
        # self.scale_surface_offset = pygame.math.Vector2()

        self.current_sprite = 0

        self.animation_images = {
            'Up': [],
            'Right': [],
            'Down': [],
            'Left': [],
            'StandDown': []
        }

        # Load all the image
        for folder in os.listdir(jerry_img_directory):
            for file in os.listdir(os.path.join(jerry_img_directory, folder)):
                tmp_img = pygame.image.load(os.path.join(jerry_img_directory, folder, file))
                
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

        self.rect = self.image.get_rect(topleft= (self.position[0] * self._grid_size + coord_adjust * 2,
                                                  self.position[1] * self._grid_size - coord_adjust * 2))        
    @property
    def grid_size(self):
        return self._grid_size * self.scale

    def escape_move(self, maze, energy_grp= None, tom_grp= None, ui_grp= None):
        tom_position = tom_grp.sprite.position
        
        if tom_position == self.position:
            return

        directions = ['T', 'R', 'B', 'L']

        distances = dict()

        for direction in directions:
            if self.is_valid_move(direction= direction, grids= maze.grids): 
                next_position = get_position_after_move(position= self.position, direction= direction)
                
                # distances[direction] = mahathan_distance(next_position, tom_position)
                distances[direction] = len(
                    BDFS(
                        grids= maze.grids,
                        player_current_position= next_position,
                        player_winning_position= tom_position,
                        algorithm= 'BFS'
                    )
                )

        if distances:
            maximize_direction = sorted(list(distances.keys()), key= lambda x: distances[x], reverse= True)[0]

            if maximize_direction == 'T':
                sprites = self.animation_images['Up']
            elif maximize_direction == 'R':
                sprites = self.animation_images['Right']
            elif maximize_direction == 'B':
                sprites = self.animation_images['Down']
            elif maximize_direction == 'L':
                sprites = self.animation_images['Left']

            self.position = get_position_after_move(position= self.position, direction= maximize_direction)
            
            move_coord = get_diffirent_coord(direction= maximize_direction, maze_grid_size= self.grid_size)
            move_coord = move_coord / self.grid_size
            
            pygame.event.clear()
            
            current_sprite = 0
            
            # Loop 28 frame
            for _ in range(self._grid_size):
                self.image = sprites[int(current_sprite)]
                self.rect.topleft = self.rect.topleft + move_coord 
                
                maze.draw(self.screen)
                if energy_grp: energy_grp.draw(self.screen)
                tom_grp.update()
                tom_grp.draw(self.screen)
                
                self.screen.blit(self.image, self.rect)
                
                scale_surface = pygame.transform.scale(self.screen, self.screen_vector * self.scale)
                # scale_surface = pygame.transform.rotozoom(self.screen, 0, self.scale)
                scale_rect = scale_surface.get_rect(center= (self.window_screen.get_width() / 2, self.window_screen.get_height() / 2))

                self.window_screen.blit(scale_surface, scale_rect.topleft + self.scale_surface_offset) ###
                
                ui_grp.draw_ui()
                
                pygame.display.update()
                
                current_sprite += len(sprites) / self._grid_size

                # if current_sprite > len(sprites) - 1 :
                #     break
            maze.end_position = self.position
                
    def update(self, 
               maze= None,
               scale: int = None,
               offset: int = None,
               tom_grp = None,
               energy_grp = None,
               ui_grp = None,
                **kwargs) -> bool:
        if offset:
            self.scale_surface_offset = offset
        if scale:
            if scale != self.scale:
                # pass
                self.scale = scale
        if tom_grp:
            steps = tom_grp.sprite.step_moves
            if steps % 2 == 0:
                self.escape_move(
                    maze= maze,
                    energy_grp= energy_grp,
                    tom_grp= tom_grp,
                    ui_grp= ui_grp
                )

        self.current_sprite += 0.05
        if int(self.current_sprite) >= len(self.animation_images['StandDown']):
            self.current_sprite = 0
        self.image = self.animation_images['StandDown'][int(self.current_sprite)]