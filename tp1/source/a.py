from heuristic_search import HeuristicSearch


class AStar(HeuristicSearch):

    def _update_frontier(self, child):
        if child.state in self.frontier:
            self.frontier.replace((self._heuristic_value(child), child))
        elif child.state not in self.explored:
            self.frontier.insert((self._heuristic_value(child), child))

    def _heuristic_value(self, node):
        return self.heuristic(node.state, self.problem.goal) + node.path_cost
