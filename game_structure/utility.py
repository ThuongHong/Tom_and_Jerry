from algorithm.BDFS import BDFS
import pygame
import random

def get_position_after_move(position: tuple[int],
                            direction: str):
    """Function take position and direction as inputs, return position after move follow that direction. This function does not check if it is a valid move or not. Be careful

    Args:
        position (tuple[int]): Tuple of int, e.g (x, y)
        direction (str): One of ['T', 'R', 'B', 'L'], if input is diffirent, function raise ValueError
    """
    # Standardize inputs
    direction = direction.upper()
    
    if direction == 'T': return (position[0], position[1] - 1)
    elif direction == 'R': return (position[0] + 1, position[1])
    elif direction == 'B': return (position[0], position[1] + 1)
    elif direction == 'L': return (position[0] - 1, position[1])
    else: raise ValueError

def get_diffirent_coord(direction: str, maze_grid_size: int):
    if direction == 'T': return pygame.math.Vector2(0, -maze_grid_size)
    elif direction == 'R': return pygame.math.Vector2(maze_grid_size, 0)
    elif direction == 'B': return pygame.math.Vector2(0, maze_grid_size)
    elif direction == 'L': return pygame.math.Vector2(-maze_grid_size, 0)

def get_direction(current_grid: tuple[int],
                  next_grid: tuple[int],
                  maze_grid_size: int):
    delta_x = next_grid[0] - current_grid[1]
    if delta_x == 1: return 'R'
    elif delta_x == -1: return 'L'

    delta_y = next_grid[1] - current_grid[1]
    if delta_y == 1: return 'B'
    elif delta_y == -1: return 'T'

def choose_k_point_in_path(grids, position_lst: list, number: int) -> list:
    preprocess_lst = []

    for action, grid in position_lst:
        name = grids[grid].get_feature
        if name == 'no-wall' or '-' not in name:# or len(name.split('-')) == 2:
            preprocess_lst.append(grid)
    
    if not preprocess_lst: return []

    processing_lst = []
    processing_lst.append(preprocess_lst[0])
    for i in range(1, len(preprocess_lst)):
        if mahathan_distance(
            fisrt_position= preprocess_lst[i],
            second_position= processing_lst[len(processing_lst) - 1]
        ) >= 3:
            processing_lst.append(preprocess_lst[i])
            
    return processing_lst
    # return preprocess_lst

def choose_point_in_path(grids, path_list: list, energy_list: list):
    path_len = len(path_list)
    def is_valid_path_list(path_list: list, energy_list: list):
        for place in path_list:
            if place[1] not in energy_list:
                return True
        return False

    if not is_valid_path_list(path_list= path_list, energy_list= energy_list):
        return []

    number = int(path_len / 3)

    if number == 0: return []
    
    random_index_lst = []
    # random_index_lst.append(0)

    while True:
        first_random_index = random.randrange(0, path_len)
        if first_random_index not in energy_list:
            random_index_lst.append(first_random_index)
            break
    
    while (path_len - 1) - random_index_lst[-1] > 5:
        random_index = random.randrange(random_index_lst[-1] + 1, path_len - 1)
        if path_list[random_index][1] not in energy_list:
            random_index_lst.append(random_index)

    while random_index_lst[0] > 4:
        random_index = random.randrange(0, random_index_lst[0])
        if path_list[random_index][1] not in energy_list:
            random_index_lst.insert(
                0,
                random_index
            )
    
    if len(random_index_lst) <= 1:
        if len(random_index_lst) == 0: print(path_list)
        return [path_list[i][1] for i in random_index_lst]
    else:
        i = 1
        while True:
            if i == len(random_index_lst):
                break

            if random_index_lst[i] - random_index_lst[i - 1] > 5:
                random_index = random.randrange(random_index_lst[i - 1] + 1, random_index_lst[i])
                if path_list[random_index][1] not in energy_list:
                    random_index_lst.insert(
                        i,
                        random_index
                    )
                # i += 1
                continue

            i += 1

        return [path_list[i][1] for i in random_index_lst]

def mahathan_distance(fisrt_position: tuple, second_position: tuple):
    return abs(fisrt_position[0] - second_position[0]) + abs(fisrt_position[1] - second_position[1])

def random_square_position(grids, current_grid):
    # rand_index = random
    return random.choice(grids[current_grid].get_neighbors())

def is_valid(position: tuple[int, int], max_size):
    if position[0] < 0 or position[0] >= max_size:
        return False
    if position[1] < 0 or position[1] >= max_size:
        return False
    return True

def get_surround(position: tuple[int, int], max_size, square_size):
    suround_lst = []
    for i in range(square_size):
        for j in range(square_size):
            if i == 1 and j == 1: continue
            suround_position = (position[0] + i - square_size // 2, position[1] + j - square_size // 2)
            if is_valid(
                suround_position,
                max_size= max_size
            ):
                suround_lst.append(suround_position)

    return suround_lst