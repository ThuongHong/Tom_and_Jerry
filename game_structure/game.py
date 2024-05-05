import pygame
from game_structure.maze import Maze
from game_structure.character import Tom



class GamePlay():
    def __init__(self, player: pygame.sprite.GroupSingle):
        # Maze
        self.maze = player.sprite.Maze
        # Player
        self.player = player
        # Time
        self.game_state = 'run'
        self.start_time = pygame.time.get_ticks()

    @property
    def step_moves(self):
        return self.player.sprite.step_moves
        
    def run(self, screen):
        while self.game_state == 'run':
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.player.update(direction= 'L')
                    elif event.key == pygame.K_RIGHT:
                        self.player.update(direction= 'R')
                    elif event.key == pygame.K_UP:
                        self.player.update(direction= 'T')
                    elif event.key == pygame.K_DOWN:
                        self.player.update(direction= 'B')
        
            self.maze.draw(screen)
            self.player.update()
            self.player.draw(screen)

            if self.player.sprite.position == self.maze.end_position:
                self.game_state = 'win'

            pygame.display.update()

        print(self.get_time())
        print(self.step_moves)

    def get_time(self):
        mili_sec = pygame.time.get_ticks() - self.start_time

        return f"{mili_sec / 1000} ms"

def load_game_from_json_file(file_name: str) -> GamePlay:
    ...

