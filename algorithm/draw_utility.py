import pygame
from Game_Constant.Color import Color

def draw_two_grids(grids,
                   screen,
                   current_grid: tuple[int],
                   next_grid: tuple[int]):
    current_center_coord = grids[current_grid].get_center_coord()
    next_center_coord = grids[next_grid].get_center_coord()

    CIRCLE_RADIUS = grids[current_grid].grid_size / 6

    pygame.draw.circle(screen, Color.RED, current_center_coord, CIRCLE_RADIUS)
    pygame.draw.line(screen, Color.RED, current_center_coord, next_center_coord)
    pygame.draw.circle(screen, Color.RED, next_center_coord, CIRCLE_RADIUS)

    pygame.display.update()
