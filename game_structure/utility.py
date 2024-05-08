def get_position_after_move(position: tuple[int],
                            direction: str):
    """Function take position and direction as inputs, return position after move follow that direction. This function does not check if it is a valid move or not. Be careful

    Args:
        position (tuple[int]): Tuple of int, e.g (x, y)
        direction (str): One of ['T', 'R', 'B', 'R'], if input is diffirent, function raise ValueError
    """
    # Standardize inputs
    direction = direction.upper()
    
    if direction == 'T': return (position[0], position[1] - 1)
    elif direction == 'R': return (position[0] + 1, position[1])
    elif direction == 'B': return (position[0], position[1] + 1)
    elif direction == 'L': return (position[0] - 1, position[1])
    else: raise ValueError

def get_diffirent_coord(direction: str, maze_grid_size: int):
    if direction == 'T': return (0, -maze_grid_size)
    elif direction == 'R': return (maze_grid_size, 0)
    elif direction == 'B': return (0, maze_grid_size)
    elif direction == 'L': return (-maze_grid_size, 0)

def get_direction(current_grid: tuple[int], 
                       next_grid: tuple[int],
                       maze_grid_size: int):
    print(current_grid, next_grid)

    delta_x = next_grid[0] - current_grid[1]
    if delta_x == 1: return 'R'
    elif delta_x == -1: return 'L'

    delta_y = next_grid[1] - current_grid[1]
    if delta_y == 1: return 'B'
    elif delta_y == -1: return 'T'