import pygame
import sqlite3
from game_structure.grid import GridCell
from game_structure.maze import Maze
from game_structure.character import Tom
from algorithm.draw_utility import mark_grid
from solving_maze.solving_maze import solve_maze
import json

def str_to_tuple(encode_str: str) -> tuple[int]:
    x, y = encode_str.lstrip('(').rstrip(')').split(',')
    return (int(x), int(y))


class GamePlay():
    Game_States = ['start', 'in_game', 'save_game', 'win_game']
    
    def __init__(self,
                 maze_size: int = 20,
                 grid_size: int = 30,
                 start_coord_screen: tuple[int] = (0, 0),
                 end_coord_screen: tuple[int] = (700, 700),
                 screen = None,
                 player_skin: str = 'Normal',
                 energy: int = 0,
                 scale: int = 1,
                 **kwargs):
        # self.id = 0

        self.grid_size = grid_size

        self._maze_size = maze_size
        
        if self.maze_size == 20:
            self.game_mode = 'Easy'
        elif self.maze_size == 40:
            self.game_mode = 'Medium'
        elif self.maze_size == 100:
            self.game_mode = 'Hard'
        else:
            self.game_mode = 'NULL'

        self.energy = energy

        self.player_skin = player_skin
        
        self.screen = screen
        
        self.scale = scale
        
        self.is_draw_solution = False
                
        self.game_state = 'start'

        self.solve_maze_algorithm = 'BFS'

        self.solving_grid_process = None
        self.solve_position = None
        self.solve_index = 0
        
        self.is_move = False

        self.is_stop_process = True
    
    @property
    def maze_size(self):
        return self._maze_size
    
    @maze_size.setter
    def maze_size(self, new_size):
        self._maze_size = new_size
        
        if self.maze_size == 20:
            self.game_mode = 'Easy'
        elif self.maze_size == 40:
            self.game_mode = 'Medium'
        elif self.maze_size == 100:
            self.game_mode = 'Hard'
        else:
            self.game_mode = 'NULL'


    @property
    def step_moves(self):
        return self.player.sprite.step_moves
    
    @property
    def info(self):
        return f"Game end in {self.get_time} after {self.step_moves} moves"
    
    @property
    def get_time(self):
        mili_sec = pygame.time.get_ticks() - self.start_time

        return f"{mili_sec / 1000} s"
    
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
        self.Maze = Maze(
            maze_size= self.maze_size,
            maze_grid_size= self.grid_size,
            screen= self.screen,
            scale= self.scale
        )
        self.Maze.generate_new_maze(algorithm= algorithm,
                                    draw= ondraw,
                                    draw_speed= draw_speed)
        # Insert to database
        db_connect = sqlite3.connect(r'database/TomJerry.db')
        db_cursor = db_connect.cursor()

        # Insert to games
        db_cursor.execute('''INSERT INTO "games"("maze_size", "game_mode", "energy_mode", "grid_size", "player_skin", "generate_algorithm")
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            self.Maze.maze_size,
            self.game_mode,
            self.energy,
            self.grid_size,
            self.player_skin,
            algorithm
        )            
        )
        
        self.id = list(db_cursor.execute('SELECT "id" FROM "games" ORDER BY "id" DESC LIMIT 1'))[0][0]

        self.game_state == 'in_game'

        db_connect.commit()

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

        if self.check_win():
            self.save_leaderboard()

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
            return True
        return False

    def save_game(self):
        db_connect = sqlite3.connect(r'database/TomJerry.db')

        db_cursor = db_connect.cursor()

        maze_data = []
        for i in range(self.Maze.maze_size):
            for j in range(self.Maze.maze_size):
                maze_data.append(
                    self.Maze.grids[i, j].walls
                )

        maze_data.append(
            self.Maze.grids[self.Maze.start_position[0], -1].walls
        )
        
        maze_data.append(
            self.Maze.grids[self.Maze.end_position[0], self.maze_size].walls
        )

        maze_data_str = json.dumps(maze_data, indent= 4) 

        db_cursor.execute(
            '''
            INSERT INTO "game_saves"("game_id", "maze", "current_position", "start_position", "end_position", "scale", "times", "moves")
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''',
            (
                self.id,
                maze_data_str,
                self.player.sprite.position.__str__(),
                self.Maze.start_position.__str__(),
                self.Maze.end_position.__str__(),
                self.scale,
                self.get_time,
                self.step_moves
            )
        )

        db_connect.commit()

    def save_leaderboard(self):
        # Connect to database
        db_connect = sqlite3.connect(r'database/TomJerry.db')
        
        db_cursor = db_connect.cursor()
        
        insert_query = 'INSERT INTO "leaderboard"("game_id", "times", "moves") VALUES(?, ?, ?)'

        db_cursor.execute(insert_query, (self.id, self.get_time, self.step_moves))

        db_connect.commit()
        # Done
    
    # @classmethod
    # def load(cls, game_id, screen):
    #     return load_game_from_json_file(game_id= game_id,
    #                                     screen= screen)

def load_GamePlay(game_id: int, screen) -> GamePlay:
    # Read all the database

    db_connect = sqlite3.connect(r'database/TomJerry.db')

    db_cursor = db_connect.cursor()
    
    
    game_data_1 = list(db_cursor.execute(f'SELECT * FROM "game_saves" WHERE "game_id" = {game_id}'))[0] # Get that row

    game_data_2 = list(db_cursor.execute(f'SELECT * FROM "games" WHERE "id" = {game_id}'))[0]

    # Get the data that useful
    maze_size = int(game_data_2[2])

    grid_size = int(game_data_2[5])

    player_skin = game_data_2[6]

    is_energy = int(game_data_2[4])

    scale = int(game_data_1[5])

    times = float(game_data_1[-2].rstrip(' s')) * 1000

    moves = int(game_data_1[-1])

    # Intialize a gameplay
    Game = GamePlay(
        maze_size= maze_size,
        grid_size= grid_size,
        screen= screen,
        player_skin= player_skin,
        energy= is_energy,
        scale= scale
    )

    current_position = str_to_tuple(game_data_1[2])
    start_position = str_to_tuple(game_data_1[3])
    end_position = str_to_tuple(game_data_1[4])
    
    # Set the game.id to according to the data
    Game.id = game_id

    # Read the maze
    tmp_maze = Maze(
        maze_size= Game.maze_size,
        maze_grid_size= grid_size,
        screen= screen,
        scale= scale
    )

    maze_info = json.loads(game_data_1[1])

    for i in range(maze_size):
        for j in range(maze_size):
            tmp_maze.grids[i, j].walls = maze_info[i * maze_size + j].copy()
        
    tmp_maze.grids[start_position[0], -1] = GridCell(
        grid_position= (start_position[0], -1),
        grid_size= grid_size,
        scale= scale
    )
    tmp_maze.grids[end_position[0], maze_size] = GridCell(
        grid_position= (end_position[0], maze_size),
        grid_size= grid_size,
        scale= scale
    )
    tmp_maze.grids[start_position[0], start_position[1] - 1].walls = maze_info[-2].copy()
    tmp_maze.grids[end_position[0], maze_size].walls = maze_info[-1].copy()

    print(tmp_maze.grids[end_position].walls)
    print(end_position)

    for grid in tmp_maze.grids:
        tmp_maze.grids[grid].is_visited = True

    Game.Maze = tmp_maze
    
    Game.Maze.start_position = start_position
    Game.Maze.end_position = end_position

    Game.player = pygame.sprite.GroupSingle()
    Game.player.add(
        Tom(current_position, Game.grid_size, Game.screen, Game.scale)
    )

    Game.player.sprite.step_moves = moves

    Game.set_new_game_state('in_game')
    Game.start_time = pygame.time.get_ticks() - times

    Game.game_state = 'in_game'

    return Game




    

