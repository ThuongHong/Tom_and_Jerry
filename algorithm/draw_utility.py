import pygame
import os

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
              tom: bool = False,
              jerry: bool = False,
              COLOR: tuple[int] = COLOR.GREEN):
    if footprint:
        rect = footprint.get_rect(center=grids[current_grid].grid_coord_center)
        screen.blit(footprint, rect)
    elif tom:
        tmp_img = pygame.image.load(
            os.path.join("images", "Tom", "StandDown", "1.png")
        )

        tmp_img_height = tmp_img.get_height()
        tmp_img_width = tmp_img.get_width()

        bigger_size = (
            tmp_img_height
            if (tmp_img_height > tmp_img_width)
            else tmp_img_width
        )
        scale_index = bigger_size / grids[0, 0].grid_size

        image = pygame.transform.scale(
            tmp_img, (tmp_img_width / scale_index, tmp_img_height / scale_index)
        )

        rect = image.get_rect(center=grids[current_grid].grid_coord_center)

        screen.blit(image, rect)
    elif jerry:
        tmp_img = pygame.image.load(
            os.path.join("images", "Jerry", "StandDown", "1.png")
        )

        tmp_img_height = tmp_img.get_height()
        tmp_img_width = tmp_img.get_width()

        bigger_size = (
            tmp_img_height
            if (tmp_img_height > tmp_img_width)
            else tmp_img_width
        )
        scale_index = bigger_size / grids[0, 0].grid_size

        image = pygame.transform.scale(
            tmp_img, (tmp_img_width / scale_index, tmp_img_height / scale_index)
        )

        rect = image.get_rect(center=grids[current_grid].grid_coord_center)

        screen.blit(image, rect)
    else:
        left, top = grids[current_grid].grid_coord
        size = grids[current_grid].grid_size
        rect = pygame.Rect(left + 2, top + 2, size - 4, size - 4)

        pygame.draw.rect(screen, COLOR, rect)


    # pygame.display.update()
