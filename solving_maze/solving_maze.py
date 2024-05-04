from algorithm.BDFS import BDFS
from game_structure.character import Character

def solve_maze(player: Character, algorithm: str = 'DFS') -> list[tuple[str, tuple[int]]]:
    """Given the character, this function return a list of move to get to the end point

    Args:
        player (Character): None_description_
        algorithm (str, optional): Algorithm you want to use. Defaults to 'DFS'.

    Returns:
        list[tuple[str, tuple[int]]]: A list of move, e.g [('L', (3, 3)), ('R', (4, 3))]
    """

    if algorithm == 'DFS' or algorithm == 'BFS':
        return BDFS(player=player,algorithm=algorithm)
    elif algorithm == 'GDFS':
        raise NotImplementedError
    elif algorithm == 'AStar':
        raise NotImplementedError
    elif algorithm == 'HAKill':
        raise NotImplementedError


                    


        

