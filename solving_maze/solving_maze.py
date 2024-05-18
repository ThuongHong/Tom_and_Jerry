from algorithm.BDFS import BDFS
from algorithm.GBFS import GBFS
from algorithm.AStar import AStar
# from algorithm.Dijkstra import Dijkstra
from algorithm.SBFS import SBFS
# from game_structure.character import Character

def solve_maze(player, #: Character,
               maze, 
               algorithm: str = 'DFS',
               is_process: bool = False,
               adjust_start_position: tuple[int] = None,
            #    screen= None
               ) -> list[list[tuple[str, tuple[int]]], list[tuple[int]]]:
    """Given the character, this function return a list of move to get to the end point OR a list of all moves that player go


    Args:
        player (Character): None_description_
        algorithm (str, optional): Algorithm you want to use. Defaults to 'DFS'.

    Returns:
        First list[tuple[str, tuple[int]]]: A list of move, e.g [('L', (3, 3)), ('R', (4, 3))], this is solution
        ----OR----
        Second list[tuple[int]]: A list of all grid that player go through
    """
    player_current_position = player.position
    if adjust_start_position:
        player_current_position = adjust_start_position
    
    player_winning_position = maze.end_position

    if algorithm == 'DFS' or algorithm == 'BFS':
        return BDFS(grids= maze.grids, 
                    player_current_position= player_current_position, 
                    player_winning_position= player_winning_position, 
                    algorithm=algorithm,
                    is_process= is_process)
    elif algorithm == 'SBFS':
        return SBFS(grids= maze.grids, 
                    player_current_position= player_current_position, 
                    player_winning_position= player_winning_position, 
                    is_process= is_process)

    elif algorithm == 'GBFS':
        return GBFS(grids= maze.grids,
                   player_current_position= player_current_position,
                   player_winning_position= player_winning_position,
                   is_process= is_process
                   )
    elif algorithm == 'AStar_OrderedList':
        return AStar(grids=maze.grids,
                     player_current_position=player_current_position,
                     player_winning_position=player_winning_position,
                     is_process= is_process,
                     data_structure = 'OrderedList')
    elif algorithm == 'AStar_MinBinaryHeap':
        return AStar(grids=maze.grids,
                     player_current_position=player_current_position,
                     player_winning_position=player_winning_position,
                     is_process= is_process,
                     data_structure = 'MinBinaryHeap')


                    


        

