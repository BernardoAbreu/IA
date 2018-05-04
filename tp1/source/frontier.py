import numpy as np
from collections import deque


class Frontier(object):
    def __init__(self, dimensions, stack=False):
        self.frontier = stack if deque() else []
        self.frontier_hash = np.zeros(dimensions, dtype=bool)

    def insert(self, item):
        self.frontier.append(item)
        self._insert_frontier_hash(item.state)

    def remove(self):
        node = self.frontier.pop()
        self._remove_frontier_hash(node.state)
        return node

    def replace(self, item):
        i = self.frontier.index(item)
        if self.frontier[i].path_cost > item.path_cost:
            self.frontier[i] = item

    def _insert_frontier_hash(self, state):
        self.frontier_hash[state.x, state.y] = True

    def _remove_frontier_hash(self, state):
        self.frontier_hash[state.x, state.y] = False

    def empty(self):
        return len(self.frontier) == 0

    def __contains__(self, key):
        return self.frontier_hash[key.x, key.y]
