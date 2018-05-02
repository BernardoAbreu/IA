from node import Node
from util import solution
from util import child_node
# from explored import ExploredSet
# from visu import Visu
import numpy as np


class GraphSearch(object):

    _EMPTY = 0
    _EXPLORED = 1
    _FRONTIER = 2

    def __init__(self):
        self._expanded_states = 0

    def get_expanded_states(self):
        return self._expanded_states

    def _update_frontier(self, child, explored):
        if child.state not in explored \
                and child.state not in map(lambda x: x.state, self.frontier):
            self._insert_frontier(child)

    def _init_frontier(self):
        self.frontier = []

    def _insert_frontier(self, item):
        self.frontier.append(item)
        self.explored[item.state.x, item.state.y] = self._FRONTIER

    def _remove_frontier(self):
        node = self.frontier.pop()
        self.explored[node.state.x, node.state.y] = self._EMPTY
        return node

    def _frontier_is_empty(self):
        return len(self.frontier) == 0

    def _in_frontier(self, key):
        return self.explored[key.x, key.y] == self._FRONTIER

    def _init_explored(self):
        self.explored = np.zeros(self.problem.dimensions, dtype=int)

    def _in_explored(self, key):
        return self.explored[key.x, key.y] == self._EXPLORED

    def _add_explored(self, key):
        self.explored[key.x, key.y] = self._EXPLORED

    def _remove_explored(self, key):
        self.explored[key.x, key.y] = self._EMPTY

    def _add_cost(self, node):
        if self.costs[node.state.x, node.state.y]:
            self.costs[node.state.x, node.state.y] = \
                min(node.path_cost, self.costs[node.state.x, node.state.y])
        elif node.state != self.problem.initial:
            self.costs[node.state.x, node.state.y] = node.path_cost

    def run(self, problem):
        # self.visu = False
        # if self.visu:
        #     with Visu() as self.v:
        #         self.v.init_screen(problem.map)
        #         return self._run(problem)
        return self._run(problem)

    def _run(self, problem):
        self.problem = problem
        node = Node(problem.initial, 0)

        self._init_explored()
        self._init_frontier()
        self._insert_frontier(node)
        # if self.visu:
        #     self.v.update_coord(node.state, 'o')

        # explored = ExploredSet(problem.dimensions)
        self.costs = np.zeros(problem.dimensions)

        while True:
            if self._frontier_is_empty():
                return []

            node = self._remove_frontier()
            self._expanded_states += 1

            # if self.visu:
            #     self.v.update_coord(node.state, '*')

            if problem.goal_test(node.state):
                return solution(node)

            # explored.add(node.state)
            self._add_explored(node.state)
            self._add_cost(node)

            for action in problem.get_actions(node.state):
                child = child_node(problem, node, action)
                self._update_frontier(child)
