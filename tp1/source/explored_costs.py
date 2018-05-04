import numpy as np
from explored import ExploredSet


class ExploredCosts(ExploredSet):

    def __init__(self, dimensions):
        self.visited = np.zeros(dimensions, dtype=float) - 1

    def __contains__(self, key):
        return self.visited[key.x, key.y] != -1

    def add(self, node):
        if self.visited[node.state.x, node.state.y] == -1:
            self.visited[node.state.x, node.state.y] = node.path_cost
        else:
            self.visited[node.state.x, node.state.y] = \
                min(node.path_cost, self.visited[node.state.x, node.state.y])

    def remove(self, key):
        self.visited[key.x, key.y] = -1

    def get_cost(self, state):
        return self.visited[state.x, state.y]
