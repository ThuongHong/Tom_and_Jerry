import pygame
import sqlite3
from game_structure.maze import Maze
from game_structure.character import Tom



class GamePlay():
    def __init__(self,
                 maze_size: int,
                 grid_size: int,
                 start_coord_screen: tuple[int],
                 end_coord_screen: tuple[int],
                 game_setting: list,
                 screen,
                 scale: int = 1,
                 **kwargs):
        self.Maze = Maze(maze_size= maze_size,
                         maze_grid_size= grid_size,
                         screen= screen,
                         scale= scale)
        
        self.screen = screen
        self.scale = scale
        
        if game_setting[0]: # i.e generate new game
            self.Maze.generate_new_maze('HAK',
                                        draw= True,
                                        screen= self.screen)
            if game_setting[1]: # i.e user choose to select position
                
                # This step here, we will get the user input for start_end_position some how in Game UI
                # Fuhoa just create two position
                TMP_START_POSIION = (0, 0)
                TMP_END_POSITION = (1, 1)

                self.Maze.spawn_start_end_position(option= 'SELECT',
                                                   start_position= TMP_START_POSIION,
                                                   end_position= TMP_END_POSITION)
            else: # i.e no select spawn position
                self.Maze.spawn_start_end_position()

        self.player = pygame.sprite.GroupSingle()
        tom = Tom(self.Maze.start_position, 
                  grid_size= grid_size, 
                  screen= screen,
                  scale= scale)
        self.player.add(tom)
        
        # # Maze
        # self.maze = player.sprite.Maze
        # # Player
        # self.player = player
        
        # Time
        self.game_state = 'run'
        self.start_time = pygame.time.get_ticks()

        self.game_clock = pygame.time.Clock()

    @property
    def step_moves(self):
        return self.player.sprite.step_moves
    
    @property
    def info(self):
        return f"Game end in {self.get_time} after {self.step_moves} moves"
    
    @property
    def get_time(self):
        mili_sec = pygame.time.get_ticks() - self.start_time

        return f"{mili_sec / 1000} ms"

    def run(self, screen):
        test_draw_process = True
        while self.game_state == 'run':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.update(direction= 'L', maze= self.Maze)
                    elif event.key == pygame.K_RIGHT:
                        self.player.update(direction= 'R', maze= self.Maze)
                    elif event.key == pygame.K_UP:
                        self.player.update(direction= 'T', maze= self.Maze)
                    elif event.key == pygame.K_DOWN:
                        self.player.update(direction= 'B', maze= self.Maze)
            self.Maze.draw()
            self.player.draw(screen)

            self.Maze.update(scale= self.scale)
            self.player.update(scale= self.scale, 
                            maze= self.Maze, 
                            show_solving_process= test_draw_process,
                            draw_solution= True,
                            algorithm= 'GBFS')
            
            if test_draw_process: test_draw_process = False

            self.game_clock.tick(60)

            if self.player.sprite.position == self.Maze.end_position:
                self.game_state = 'win'

            pygame.display.update()

        self.save()
    
    def save(self):
        # Connect to Database
        self.db = sqlite3.connect(r'sqlite/Tom_and_Jerry.db').cursor()

        # self.db.execute("INSERT INTO 'game_save'('times', 'moves') VALUES(?, ?)", self.get_time, self.player.sprite.step_moves)
        data = self.db.execute('SELECT * FROM "game_save"')

        for row in data:
            print(row)

def load_game_from_json_file(file_name: str) -> GamePlay:
    ...

