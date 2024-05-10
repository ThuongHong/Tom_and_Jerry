class Node:
    def __init__(self, state, action, parent):
        self.state = state
        self.action = action
        self.parent = parent
        
class HyperNode:
    def __init__(self, state, action, parent, g, h = 0):
        self.state = state
        self.action = action
        self.parent = parent
        self.f = g + h
        self.g = g #cost
        self.h = h #heuristic, if h = 0 -> Dijkstra

class StackFrontier:
    def __init__(self):
        self.frontier = []
    def add(self,node):
        self.frontier.append(node)
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)
    def empty(self):
        return len(self.frontier) == 0
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty Frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node
class StackFroniterGreedySearch(StackFrontier):
    def add(self, list_node):
        self.frontier.extend(list_node)
class SortedList(list):
    def append(self, node: HyperNode):
        super().append(node)
        self.sort(key= lambda x: x.f)