import heapq
from util import manhattan_distance
from util import octile_distance
from graph_search import GraphSearch


class HeuristicSearch(GraphSearch):

    _heuristics_dict = {'manhattan': manhattan_distance,
                        'octile': octile_distance}

    def __init__(self, heuristic):
        self._expanded_states = 0
        self.heuristic = self._heuristics_dict[heuristic]

    def _heuristic_value(self):
        pass

    def _insert_frontier(self, node):
        self.explored[node.state.x, node.state.y] = self._FRONTIER
        item = (self._heuristic_value(node), node)
        heapq.heappush(self.frontier, item)

    def _remove_frontier(self):
        _, node = heapq.heappop(self.frontier)
        self.explored[node.state.x, node.state.y] = self._EMPTY
        return node

    def _replace_insert_frontier(self, item):
        for i, _, node in enumerate(self.frontier):
            if node.state == item.state:
                if node.path_cost > item.path_cost:
                    self.frontier[i] = item
                    heapq.heapify(self.frontier)
                break
