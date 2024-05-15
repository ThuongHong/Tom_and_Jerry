import pygame


class MusicController:
    def __init__(self):
        pygame.mixer.init()
        self.tracks = {
            'main menu': 'sounds/menu_music.mp3',
            'new game': 'sounds/menu_music.mp3',
            'load game': 'sounds/menu_music.mp3',
            'login signin': 'sounds/menu_music.mp3',
            'leaderboard': 'sounds/victory_music.mp3',
            'easy mode': 'sounds/easy_mode_music.mp3',
            'medium mode': 'sounds/medium_mode_music.mp3',
            'hard mode': 'sounds/hard_mode_music.mp3',
            'character_move_sound': 'sounds/character_moving_sound.ogg',
            'win_music': 'sounds/victory_music.mp3'
            # Add more menu options and their corresponding music files here
        }
        self.current_track = None
        pygame.mixer.music.set_volume(0.2)

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_track = None

    def play_music(self, game_state):
        track = self.tracks.get(game_state)
        if track:
            pygame.mixer.music.load(track)
            pygame.mixer.music.play(-1)
            self.current_track = track

    def pause_music(self):
        pygame.mixer.music.pause()

    def unpause_music(self):
        pygame.mixer.music.unpause()

    # def increase_volume(self):
    #     self.volume = min(1, self.volume + 0.1)
    #     pygame.mixer.music.set_volume(self.volume)

    # def decrease_volume(self):
    #     self.volume = max(0, self.volume - 0.1)
    #     pygame.mixer.music.set_volume(self.volume)


