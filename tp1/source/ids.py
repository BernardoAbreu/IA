from node import Node
from util import solution
from util import child_node
from explored import ExploredSet

from collections import deque


class _Frontier(object):
    def __init__(self, item):
        self.frontier = deque()
        self.frontier.append(item)

    def insert(self, item):
        self.frontier.append(item)

    def remove(self):
        return self.frontier.pop()

    def is_empty(self):
        return len(self.frontier) == 0

    def __contains__(self, state):
        for node, _ in self.frontier:
            if state == node.state:
                return True

        return False


CUTOFF = -1


def ids(problem):
    depth = 0
    while True:
        result = dfs(problem, depth)
        if result != CUTOFF:
            print(depth)
            return result
        depth += 1


def dfs(problem, limit=-1):

    limit_reached = False
    node = Node(problem.initial, 0)
    frontier = _Frontier((node, 0))
    explored = ExploredSet(problem.dimensions)

    while True:
        if frontier.is_empty():
            return CUTOFF if limit_reached else []

        node, depth = frontier.remove()

        if problem.goal_test(node.state):
            return solution(node)

        explored.add(node.state)

        if depth != limit:
            for action in reversed(problem.get_actions(node.state)):
                child = child_node(problem, node, action)
                if child.state not in explored and child.state not in frontier:
                    frontier.insert((child, depth + 1))
        else:
            limit_reached = True
