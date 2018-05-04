from heuristic_search import HeuristicSearch


class BestFirstSearch(HeuristicSearch):

    def _update_frontier(self, child):
        if not (child.state in self.explored or child.state in self.frontier):
            self.frontier.insert((self._heuristic_value(child), child))

    def _heuristic_value(self, node):
        return self.heuristic(node.state, self.problem.goal)
