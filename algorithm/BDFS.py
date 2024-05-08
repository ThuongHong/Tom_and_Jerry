from algorithm.utility import Node, StackFrontier, QueueFrontier
from algorithm.draw_utility import draw_two_grids
import pygame

def BDFS(grids: dict,
         player_current_position: tuple[int],
         player_winning_position: tuple[int],
         algorithm: str = 'DFS',
         is_process: bool = False
        #  screen= None
         ):
    # Keep track of number of grid explored and grid that already explored
    num_explored = 0
    all_player_moves = []
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
        all_player_moves.append(node.state)

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
            
            solution =  list(zip(actions, grids))
            all_player_moves.pop(0)

            if is_process: return all_player_moves
            else: return solution
    
        # If we not found the end position
            # Add current position to explored set
        explored_grid.add(node.state)

        # current_node = node
        # while set() < set(grids[current_node.state].get_neighbors()) <= explored_grid:
            # all_player_moves.append(current_node.state)
            # current_node = current_node.parent

            # print(all_player_moves)

            # Add neighbors to frontier
        for action, state in grids[node.state].get_neighbors(is_get_direction= True):
            if not frontier.contains_state(state) and state not in explored_grid:
                child_node = Node(state= state, parent= node, action= action)
                frontier.add(child_node)
                # if screen:
                #     draw_two_grids(grids= grids,
                #                 screen= screen,
                #                 current_grid= node.state,
                #                 next_grid= child_node.state)
                    
                #     pygame.time.wait(10)

