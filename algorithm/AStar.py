from Algorithm.utility import HyperNode
def h(fisrt_position: tuple, second_position: tuple):
    return abs(fisrt_position[0] - second_position[0]) + abs(fisrt_position[1] - second_position[1])
def f(node: HyperNode, player_winning_position):
    return h(node.state, player_winning_position) + node.g
def AStar(grids: dict,
          player_current_position: tuple[int],
         player_winning_position: tuple[int]):
    pass