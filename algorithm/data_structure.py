class Node:
    def __init__(self, state, action, parent):
        self.state = state
        self.action = action
        self.parent = parent


class HyperNode:
    def __init__(self, state, action, parent, g, h=0):
        self.state = state
        self.action = action
        self.parent = parent
        self.f = g + h
        self.g = g  # cost
        self.h = h  # heuristic, if h = 0 -> Dijkstra
        self.next = None


class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
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


class OrderedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def pop(self):
        if self.head is None:
            return None
        else:
            if self.head.next is None:
                self.tail = None
            pop_node = self.head
            self.head = pop_node.next
            return pop_node

    def is_empty(self):
        if self.head is None:
            return True
        return False

    def add(self, data: HyperNode):
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
                    if curNode.f < newNode.f < curNode.next.f:
                        # Add at this pos
                        newNode.next = curNode.next
                        curNode.next = newNode
                        return
                    curNode = curNode.next
                # Add Tail
                self.tail.next = newNode
                self.tail = newNode


class MinBinaryHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def is_empty(self):
        if len(self.heap) == 0:
            return True
        return False

    def add(self, data: HyperNode):
        self.heap.append(data)
        i = len(self.heap) - 1
        while i > 0 and self.heap[i].f < self.heap[self.parent(i)].f:
            self.heap[i], self.heap[self.parent(i)] = (
                self.heap[self.parent(i)],
                self.heap[i],
            )
            i = self.parent(i)

    def pop(self):
        if not self.heap:
            return None
        root = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()  # used to pop the last element in list self.heap
        self.min_heapify(0)
        return root

    def min_heapify(self, i):
        left = self.left_child(i)
        right = self.right_child(i)
        smallest = i
        if left < len(self.heap) and self.heap[left].f < self.heap[smallest].f:
            smallest = left
        if right < len(self.heap) and self.heap[right].f < self.heap[smallest].f:
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.min_heapify(smallest)
