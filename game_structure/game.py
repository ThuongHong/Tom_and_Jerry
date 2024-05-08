import pygame
import sqlite3
from game_structure.maze import Maze
from game_structure.character import Tom
from algorithm.draw_utility import mark_grid
from solving_maze.solving_maze import solve_maze


class GamePlay():
    Game_States = ['start', 'in_game', 'save_game', 'win_game']
    
    def __init__(self,
                 maze_size: int,
                 grid_size: int,
                 start_coord_screen: tuple[int],
                 end_coord_screen: tuple[int],
                 screen,
                 scale: int = 1,
                 **kwargs):
        self.grid_size = grid_size

        self.Maze = Maze(maze_size= maze_size,
                         maze_grid_size= self.grid_size,
                         screen= screen,
                         scale= scale)
        
        self.screen = screen
        
        self.scale = scale
        
        self.is_draw_solution = False
        
        # self.draw_solving_process = False
        
        self.game_state = 'start'

        self.solve_maze_algorithm = 'BFS'

        self.solving_grid_process = None
        self.solve_position = None
        self.solve_index = 0
        
        self.is_move = False

        self.is_stop_process = True
    
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
    
    def visualize_solution(self, algorithm: str = 'GBFS'):
        self.is_draw_solution = True
        self.solve_maze_algorithm = algorithm
    def de_visualize_solution(self):
        self.is_draw_solution = False
    
    def visualize_process(self, algorithm: str = 'BFS'):
        self.is_move = True

        self.draw_solving_process = True
        
        self.solve_maze_algorithm = algorithm
        
        self.solving_grid_process = solve_maze(
            self.player.sprite,
            self.Maze,
            algorithm= self.solve_maze_algorithm,
            is_process= True,
            adjust_start_position= self.solve_position
        )

        self.solve_index = 0

        self.is_stop_process = False
    def de_visualize_process(self):
        self.is_stop_process = True

    # def stop_process(self):
    #     self.is_stop_process = True

    def generate(self, 
                 algorithm= 'DFS', 
                 ondraw: bool = True,
                 draw_speed: str = 'FAST'):
        self.Maze.generate_new_maze(algorithm= algorithm,
                                    draw= ondraw,
                                    draw_speed= draw_speed)

    def spawn_random(self):
        self.Maze.spawn_start_end_position('TOP_BOTTOM')
        self.create_player()

    def select_position_spawn(self, 
                              start: tuple[int],
                              end: tuple[int]):
        is_posible =  self.Maze.spawn_start_end_position('SELECT', 
                                           start_position= start,
                                           end_position= end)    
        if not is_posible: return False
        self.create_player()

    def create_player(self):
        self.player = pygame.sprite.GroupSingle()
        self.player.add(
            Tom(self.Maze.start_position, self.grid_size, self.screen, self.scale)
        )

        self.set_new_game_state('in_game')
        self.start_time = pygame.time.get_ticks()

    def set_new_game_state(self, new_state: str):
        """Change the value of game_state

        Args:
            new_state (str): ENUM {'start', 'play', 'save', 'win'}
        """
        if new_state in self.Game_States:
            self.game_state = new_state

    def mmm(self):
        pass

    def update_screen(self):
        self.screen.fill((0, 0, 0))

    def run(self):  
        self.update_screen()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.player.update(direction= 'L', maze= self.Maze)
                    self.de_visualize_process()
                    self.de_visualize_solution()
                    self.is_move = True
                elif event.key == pygame.K_RIGHT:
                    self.player.update(direction= 'R', maze= self.Maze)
                    self.de_visualize_process()
                    self.de_visualize_solution()
                    self.is_move = True
                elif event.key == pygame.K_UP:
                    self.player.update(direction= 'T', maze= self.Maze)
                    self.de_visualize_process()                     
                    self.de_visualize_solution()                   
                    self.is_move = True
                elif event.key == pygame.K_DOWN:
                    self.player.update(direction= 'B', maze= self.Maze)
                    self.de_visualize_process()                      
                    self.de_visualize_solution()                  
                    self.is_move = True

        self.Maze.update(scale= self.scale)

        self.Maze.draw()
        
        self.player.draw(self.screen)

        self.draw_process()

        self.draw_solution()

        self.check_win()

        pygame.display.update()


    def draw_solution(self):
        if self.is_draw_solution:
            self.player.update(maze= self.Maze,
                                scale= self.scale,
                                show_solution= True,
                                algorithm= self.solve_maze_algorithm)

    def draw_process(self):
        if not self.is_stop_process and self.solving_grid_process:
            for i in range(self.solve_index + 1):
                mark_grid(self.Maze.grids,
                          self.screen,
                          self.solving_grid_process[i])
                
                # draw_two_grids(grids= self.Maze.grids,
                #             screen= self.screen, 
                #             current_grid= self.solving_grid_process[i],
                #             next_grid= self.solving_grid_process[i + 1])
                
            pygame.time.wait(10)

            self.solve_index += 1
            if self.solve_index == len(self.solving_grid_process):
                # self.solving_grid_process = []
                self.solve_index -= 1

                self.solve_position = None

                self.visualize_solution(algorithm= self.solve_maze_algorithm)

        
        elif self.is_stop_process and self.solving_grid_process:
            self.solve_position = self.solving_grid_process[self.solve_index]
            if not self.is_move:
                for i in range(self.solve_index):
                    mark_grid(self.Maze.grids,
                                self.screen,
                                self.solving_grid_process[i])

        elif self.is_move:
            self.solve_position = None
            self.solving_grid_process = []
            self.solve_index = 0
            # self.solving_grid_process = []

    def check_win(self):
        if self.player.sprite.position == self.Maze.end_position:
            self.game_state = 'win'

    
    def save(self):
        # Connect to Database
        self.db = sqlite3.connect(r'sqlite/Tom_and_Jerry.db').cursor()

        # self.db.execute("INSERT INTO 'game_save'('times', 'moves') VALUES(?, ?)", self.get_time, self.player.sprite.step_moves)
        data = self.db.execute('SELECT * FROM "game_save"')

        for row in data:
            print(row)

def load_game_from_json_file(file_name: str) -> GamePlay:
    ...

