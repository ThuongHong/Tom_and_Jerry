from algorithm.utility import HyperNode, SortedList
def h(fisrt_position: tuple, second_position: tuple):
    return abs(fisrt_position[0] - second_position[0]) + abs(fisrt_position[1] - second_position[1])
def f(node: HyperNode, player_winning_position):
    return h(node.state, player_winning_position) + node.g
def AStar(grids: dict,
          player_current_position: tuple[int],
         player_winning_position: tuple[int]):
    #Intialize openlist and closelist
    open_list = SortedList() # This 
    close_list = []
    start = HyperNode(state=player_current_position, 
                      action=None, parent=None, g=0, 
                      h=h(player_current_position,player_winning_position))
    open_list.append(start)
    while len(open_list) != 0:
        node = open_list.pop(0)
        if node.state == player_winning_position:
            actions = []
            states = []
            while node.parent is not None:
                actions.append(node.action)
                states.append(node.state)
                node = node.parent
            actions.reverse()
            states.reverse()
            return list(zip(actions, states))
        for action, state in grids[node.state].get_neighbors(is_get_direction= True):
            if state not in close_list:
                child = HyperNode(state=state, action=action, parent=node, g=node.g + 1, h=h(state,player_winning_position))
                open_list.append(child)
        close_list.append(node.state)