from collections import deque
from explored import ExploredSet


class Frontier(object):
    def __init__(self, dimensions, stack=False):
        self.frontier = stack if deque() else []
        self._frontier_hash = ExploredSet(dimensions)

    def insert(self, item):
        self.frontier.append(item)
        self._frontier_hash.add(item)

    def remove(self):
        node = self.frontier.pop()
        self._frontier_hash.remove(node)
        return node

    def replace(self, item):
        i = self.frontier.index(item)
        if self.frontier[i].path_cost > item.path_cost:
            self.frontier[i] = item

    def empty(self):
        return len(self.frontier) == 0

    def __contains__(self, key):
        return key in self._frontier_hash
