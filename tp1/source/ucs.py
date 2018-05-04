from graph_search import GraphSearch

from priority_frontier import PriorityFrontier


class UCS(GraphSearch):

    def _init_frontier(self, dimensions, node):
        self.frontier = PriorityFrontier(dimensions)
        self.frontier.insert((node.path_cost, node))

    def _update_frontier(self, child):
        if child.state in self.frontier:
            self.frontier.replace((child.path_cost, child))
        elif child.state not in self.explored:
            self.frontier.insert((child.path_cost, child))
