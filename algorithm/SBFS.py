from algorithm.data_structure import Node
from algorithm.data_structure import StackFroniterGreedySearch
from algorithm.data_structure import QueueFrontier

from utility.draw_utility import draw_two_grids


def get_manhattan_distance(fisrt_position: tuple, second_position: tuple):
    bias_x = abs(fisrt_position[0] - second_position[0]) // 2
    bias_y = abs(fisrt_position[1] - second_position[1]) // 2

    if fisrt_position[0] < second_position[0]:
        bias_distance_right = abs(
            fisrt_position[0] - second_position[0] - bias_x * 2
        ) + abs(fisrt_position[1] - second_position[1] + bias_y)
        bias_distance_left = abs(
            fisrt_position[0] - second_position[0] + bias_x * 2
        ) + abs(fisrt_position[1] - second_position[1] + bias_y)
        if bias_distance_left >= 5 or bias_distance_right >= 5:
            return abs(fisrt_position[0] - second_position[0]) + abs(
                fisrt_position[1] - second_position[1]
            )
            # return 1
        return (
            bias_distance_right
            if bias_distance_right >= bias_distance_left
            else bias_distance_left
        )
    elif fisrt_position[0] > second_position[0]:
        bias_distance_right = abs(
            fisrt_position[0] - second_position[0] - bias_x * 2
        ) + abs(fisrt_position[1] - second_position[1] + bias_y)
        bias_distance_left = abs(
            fisrt_position[0] - second_position[0] + bias_x * 2
        ) + abs(fisrt_position[1] - second_position[1] + bias_y)
        if bias_distance_left >= 5 or bias_distance_right >= 5:
            return abs(fisrt_position[0] - second_position[0]) + abs(
                fisrt_position[1] - second_position[1]
            )
            # return 1
        return (
            bias_distance_right
            if bias_distance_right >= bias_distance_left
            else bias_distance_left
        )
    elif fisrt_position[0] == second_position[0]:
        bias_distance_right = abs(
            fisrt_position[0] - second_position[0] - bias_x
        ) + abs(fisrt_position[1] - second_position[1] - bias_y)
        bias_distance_left = abs(fisrt_position[0] - second_position[0] + bias_x) + abs(
            fisrt_position[1] - second_position[1] + bias_y
        )
        if bias_distance_left >= 5 or bias_distance_right >= 5:
            return abs(fisrt_position[0] - second_position[0]) + abs(
                fisrt_position[1] - second_position[1]
            )
            # return 1
        return (
            bias_distance_right
            if bias_distance_right >= bias_distance_left
            else bias_distance_left
        )


def SBFS(
    grids: dict,
    player_current_position: tuple[int],
    player_winning_position: tuple[int],
    is_process: bool = False,
):

    # Keep track which node is explored
    node_explored = []
    all_player_moves = []

    # Initialize a frontier to contain nodes that need to explored
    frontier = StackFroniterGreedySearch()
    start = Node(state=player_current_position, action=None, parent=None)
    frontier.add([start])

    # Loop til find the solution
    while True:
        if frontier.empty():
            if is_process:
                return all_player_moves
            else:
                return []

        node = frontier.remove()
        all_player_moves.append(node.state)

        if node.state == player_winning_position:  # Found the goal
            actions = []
            states = []
            # Backtrack to get the path
            while node.parent is not None:
                actions.append(node.action)
                states.append(node.state)
                node = node.parent

            all_player_moves.pop(0)

            actions.reverse()
            states.reverse()

            if is_process:
                return all_player_moves

            else:
                return list(zip(actions, states))

        # When haven't found the goal yet, add the current node to frontier
        node_explored.append(node.state)

        # This list contains the child nodes of current node
        moves = []
        for action, state in grids[node.state].get_neighbors(is_get_direction=True):
            if not frontier.contains_state(state) and state not in node_explored:

                child = Node(state=state, action=action, parent=node)
                moves.append(child)

        # Add child nodes that are sorted decreasely by Manhattan distance
        frontier.add(
            sorted(
                moves,
                key=lambda x: get_manhattan_distance(x.state, player_winning_position),
                reverse=True,
            )
        )


def SBFS1(
    grids: dict,
    player_current_position: tuple[int],
    player_winning_position: tuple[int],
    is_process: bool = False,
    #  screen= None
):
    # Keep track of number of grid explored and grid that already explored
    num_explored = 0
    all_player_moves = []
    explored_grid = set()

    # Intialize the frontier
    start = Node(state=player_current_position, parent=None, action=None)
    frontier = QueueFrontier()

    frontier.add(start)
    is_first = True
    min_path_len = 0

    # Looping to find solution
    while True:
        is_remove_node_state = False

        if frontier.empty():
            if is_process:
                return all_player_moves
            else:
                return []

        # Choose a node from frontier
        node = frontier.remove()
        all_player_moves.append(node.state)

        num_explored += 1

        # If we found the end position
        # Backtracking from end to start then reverse to get solution
        if node.state == player_winning_position:
            actions = []
            grids_solution = []

            while node.parent is not None:
                actions.append(node.action)
                grids_solution.append(node.state)
                node = node.parent

            actions.reverse()
            grids_solution.reverse()

            solution = list(zip(actions, grids_solution))
            all_player_moves.pop(0)
            if not is_first:
                if min_path_len + 6 <= len(grids_solution):
                    if is_process:
                        return all_player_moves
                    else:
                        return solution
                else:
                    is_remove_node_state = True
            else:
                min_path_len = len(grids_solution)

                for state in grids_solution:
                    explored_grid.discard(state)
                is_first = False
        # If we not found the end position
        # Add current position to explored set
        if not is_remove_node_state:
            explored_grid.add(node.state)

            # if node.state == player_winning_position and is_first:
            #     is_first = False
            #     explored_grid.remove(node.state)
            #     continue
            for action, state in grids[node.state].get_neighbors(is_get_direction=True):
                if not frontier.contains_state(state):
                    child_node = Node(state=state, parent=node, action=action)
                    frontier.add(child_node)
