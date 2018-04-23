from node import Node
from util import solution
from util import child_node
from explored import ExploredSet

from collections import deque

from visu import Visu


class _Frontier(object):
    def __init__(self, item):
        self.frontier = deque()
        self.frontier.append(item)

    def insert(self, item):
        self.frontier.append(item)

    def remove(self):
        return self.frontier.popleft()

    def is_empty(self):
        return len(self.frontier) == 0

    def __contains__(self, state):
        for node in self.frontier:
            if state == node.state:
                return True

        return False


def bfs(problem):
    v = Visu()
    v.init_screen(problem.map)

    node = Node(problem.initial, 0)
    if problem.goal_test(node.state):
        v.close()
        return solution(node)

    # a FIFO queue with node as the only element
    frontier = _Frontier(node)
    explored = ExploredSet(problem.dimensions)

    v.update_coord(node.state, 'o')

    while True:
        if frontier.is_empty():
            v.close()
            return []  # Failure

        # chooses the shallowest node in frontier
        node = frontier.remove()
        v.update_coord(node.state, '*')

        explored.add(node.state)
        for action in problem.get_actions(node.state):
            child = child_node(problem, node, action)

            if child.state not in explored and child.state not in frontier:
                if problem.goal_test(child.state):
                    v.close()
                    return solution(child)

                frontier.insert(child)
                v.update_coord(child.state, 'o')
