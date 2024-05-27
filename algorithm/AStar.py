from algorithm.data_structure import HyperNode
from algorithm.data_structure import OrderedList
from algorithm.data_structure import MinBinaryHeap


# A* use a 'f' function to evaluate a node to choose right direction
# f(node) = g(node) + h(node)
# with:
#   - f(node): evaluating function
#   - g(node): cost that we consume to 'come' to 'node'. In this code, I suppose the cost is number of moves needing to come to that node
#   - h(node): distance from current node to goal node. Approximately , I use Manhattan distance to calcute this distance


def h(fisrt_position: tuple, second_position: tuple):
    return abs(fisrt_position[0] - second_position[0]) + abs(
        fisrt_position[1] - second_position[1]
    )


def f(node: HyperNode, player_winning_position):
    return h(node.state, player_winning_position) + node.g


def AStar(
    grids: dict,
    player_current_position: tuple[int],
    player_winning_position: tuple[int],
    is_process: bool = False,
    data_structure="OrderedList",
):
    # Intialize all_moves list to keep track on process
    all_player_moves = []

    # Intialize openlist and closelist

    # This list contains the nodes that we need to explore
    # Class OrderedList() helps us when append new node, the list automatically sort increasingly
    if data_structure == "OrderedList":
        open_list = OrderedList()
    else:
        open_list = MinBinaryHeap()
    # This list contains the nodes that we have explored and evaluated.
    # When a node is in this list, it means the lowest-cost path to that node has been found
    close_list = set()

    # Initialize start node
    start = HyperNode(
        state=player_current_position,
        action=None,
        parent=None,
        g=0,
        h=h(player_current_position, player_winning_position),
    )
    open_list.add(start)

    # Loop until find the goal or open_list is empty
    while not open_list.is_empty():
        # Take the first node (means the lowest-cost node)
        node = open_list.pop()
        all_player_moves.append(node.state)

        # If the node is goal -> return solution
        if node.state == player_winning_position:
            actions = []
            states = []
            # Bakctrack from the goal to find the path
            while node.parent is not None:
                actions.append(node.action)
                states.append(node.state)
                node = node.parent

            actions.reverse()
            states.reverse()

            all_player_moves.pop(0)

            if is_process:
                return all_player_moves
            else:
                return list(zip(actions, states))

        # If not the goal, evaluate the neighbor of current node
        for action, state in grids[node.state].get_neighbors(is_get_direction=True):
            # As you know the meaning of close_list, we pass the node that has been in close_list
            if state not in close_list:
                child = HyperNode(
                    state=state,
                    action=action,
                    parent=node,
                    g=node.g + 1,
                    h=h(state, player_winning_position),
                )
                open_list.add(child)

        close_list.add(node.state)
    if is_process:
        return all_player_moves
    return []
