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
        self.next = None

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
    def __init__(self):
        self.head = None
        self.tail = None

    def pop(self):
        if self.head is None:
            return None
        else:
            if self.head.next is None: self.tail = None
            pop_node = self.head
            self.head = pop_node.next
            return pop_node

    def is_empty(self):
        if self.head is None:
            return True
        return False
    
    def append(self, data: HyperNode):
        newNode = data

        if self.head is None:
            self.head = newNode
            self.tail = newNode
            return
        else:
            curNode = self.head

            if newNode.f <= curNode.f:
                # Add Head
                newNode.next = self.head
                self.head = newNode
            else:
                while curNode is not self.tail:
                    if curNode.f <= newNode.f <= curNode.next.f:
                        # Add at this pos
                        newNode.next = curNode.next
                        curNode.next = newNode
                        return
                    curNode = curNode.next
                # Add Tail
                self.tail.next = newNode
                self.tail = newNode

