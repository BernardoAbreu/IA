from node import Node
from util import solution
from util import child_node
from explored import ExploredSet
from frontier import Frontier


class GraphSearch(object):

    def __init__(self):
        self._expanded_states = 0

    def get_expanded_states(self):
        return self._expanded_states

    def _init_frontier(self, dimensions):
        self.frontier = Frontier(dimensions)

    def _init_explored(self, dimensions):
        self.explored = ExploredSet(dimensions)

    def _update_frontier(self, child):
        if not (child.state in self.explored or child.state in self.frontier):
            self.frontier.insert(child)

    def _run(self, problem):
        self.problem = problem
        node = Node(problem.initial, 0)

        self._init_explored(problem.dimensions)
        self._init_frontier(problem.dimensions, node)

        while True:
            if self.frontier.empty():
                return []

            node = self.frontier.remove()
            self._expanded_states += 1

            if problem.goal_test(node.state):
                return solution(node)

            self.explored.add(node)

            for action in problem.get_actions(node.state):
                child = child_node(problem, node, action)
                self._update_frontier(child)

    def run(self, problem):
        return self._run(problem)
