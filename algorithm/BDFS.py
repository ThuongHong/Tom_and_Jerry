from algorithm.utility import Node, StackFrontier, QueueFrontier

def BDFS(grids: dict,
         player_current_position: tuple[int],
         player_winning_position: tuple[int],
         algorithm: str = 'DFS'):
    # Keep track of number of grid explored and grid that already explored
    num_explored = 0
    explored_grid = set()

    # Intialize the frontier
    start = Node(state= player_current_position, parent= None, action= None)
    if algorithm == 'DFS': frontier = StackFrontier()
    else: frontier = QueueFrontier()

    frontier.add(start)

    # Looping to find solution
    while True:
        if frontier.empty(): return []

        # Choose a node from frontier
        node = frontier.remove()
        num_explored += 1
        
        # If we found the end position
        # Backtracking from end to start then reverse to get solution 
        if node.state == player_winning_position:
            actions = []
            grids = []

            while node.parent is not None:
                actions.append(node.action)
                grids.append(node.state)
                node = node.parent
            actions.reverse()
            grids.reverse()

            return zip(actions, grids)
    
        # If we not found the end position
            # Add current position to explored set
        explored_grid.add(node.state)

            # Add neighbors to frontier
        for action, state in grids[node.state].get_neighbors(is_get_direction= True):
            if not frontier.contains_state(state) and state not in explored_grid:
                child_node = Node(state= state, parent= node, action= action)
                frontier.add(child_node)
