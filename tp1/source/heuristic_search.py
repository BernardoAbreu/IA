from priority_frontier import PriorityFrontier
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

    def _init_frontier(self, dimensions, node):
        self.frontier = PriorityFrontier(dimensions)
        self.frontier.insert((self._heuristic_value(node), node))
