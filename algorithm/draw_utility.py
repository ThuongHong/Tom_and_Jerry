import pygame

from CONSTANTS import COLOR

def draw_two_grids(grids,
                   screen,
                   current_grid: tuple[int],
                   next_grid: tuple[int]):
    current_center_coord = grids[current_grid].get_center_coord()
    next_center_coord = grids[next_grid].get_center_coord()

    CIRCLE_RADIUS = grids[current_grid].grid_size / 6

    pygame.draw.circle(screen, COLOR.RED, current_center_coord, CIRCLE_RADIUS)
    pygame.draw.line(screen, COLOR.RED, current_center_coord, next_center_coord)
    pygame.draw.circle(screen, COLOR.RED, next_center_coord, CIRCLE_RADIUS)

def mark_grid(grids,
              screen,
              current_grid: tuple[int],
              footprint = None,
              COLOR: tuple[int] = COLOR.GREEN):
    left, top = grids[current_grid].grid_coord
    size = grids[current_grid].grid_size
    rect = pygame.Rect(left + 2, top + 2, size - 4, size - 4)

    rect = footprint.get_rect(center=grids[current_grid].grid_coord_center)
    # pygame.draw.rect(screen, COLOR, rect)
    if footprint:
        screen.blit(footprint, rect)

    # pygame.display.update()
