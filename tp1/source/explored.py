import numpy as np


class ExploredSet(object):

    def __init__(self, dimensions):
        self.visited = np.zeros(dimensions, dtype=bool)

    def __contains__(self, key):
        return self.visited[key.x, key.y]

    def add(self, node):
        self.visited[node.state.x, node.state.y] = True

    def remove(self, node):
        self.visited[node.state.x, node.state.y] = False
