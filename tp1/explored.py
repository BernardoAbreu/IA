import numpy as np


class ExploredSet(object):

    def __init__(self, dimensions):
        self.visited = np.zeros(dimensions, dtype=bool)

    def __contains__(self, key):
        return self.visited[key.x, key.y]

    def add(self, key):
        self.visited[key.x, key.y] = True

    def remove(self, key):
        self.visited[key.x, key.y] = False
