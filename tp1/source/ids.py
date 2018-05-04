from graph_search import GraphSearch
from explored_costs import ExploredCosts
from frontier import Frontier


class IDS(GraphSearch):

    def _init_explored(self, dimensions):
        self.explored = ExploredCosts(dimensions)

    def _update_frontier(self, child):
        if child.path_cost > self.limit:
            self.limit_reached = True
        elif self.explored.get_cost(child.state) > child.path_cost or \
                not (child.state in self.explored or
                     child.state in self.frontier):
            self.frontier.insert(child)

    def _init_frontier(self, dimensions, node):
        self.frontier = Frontier(dimensions, stack=True)
        self.frontier.insert(node)

    def run(self, problem):
        self.limit = 0
        while True:
            self.limit_reached = False
            result = self._run(problem)
            if result or not self.limit_reached:
                return result
            self.limit += 0.5
