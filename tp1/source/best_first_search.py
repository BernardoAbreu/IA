# from node import Node
# from util import *
# from explored import ExploredSet
from heuristic_search import HeuristicSearch

# import heapq

# from visu import Visu


# class _Frontier(object):

#     def __init__(self, item):
#         self.frontier = []
#         self.insert(item)

#     def insert(self, item):
#         heapq.heappush(self.frontier, item)

#     def remove(self):
#         return heapq.heappop(self.frontier)

#     def is_empty(self):
#         return len(self.frontier) == 0

#     def __contains__(self, state):
#         for _, node in self.frontier:
#             if state == node.state:
#                 return True

#         return False

#     def __str__(self):
#         return str(self.frontier)


# def best_first_search(problem):
#     # with Visu() as v:
#     # v.init_screen(problem.map)

#     node = Node(problem.initial, 0)
#     goal = problem.goal

#     frontier = _Frontier((manhattan_distance(node.state, goal), node))
#     explored = ExploredSet(problem.dimensions)

#     # v.update_coord(node.state, 'o')

#     while True:
#         if frontier.is_empty():
#             return []  # Failure

#         _, node = frontier.remove()
#         # v.update_coord(node.state, '*')

#         if problem.goal_test(node.state):
#             return solution(node)

#         explored.add(node.state)

#         for action in problem.get_actions(node.state):
#             child = child_node(problem, node, action)

#             if child.state not in explored and child.state not in frontier:
#                 frontier.insert((manhattan_distance(child.state, goal), child))


class BestFirstSearch(HeuristicSearch):

    def _update_frontier(self, child):
        if not self._in_explored(child.state) and \
                not self._in_frontier(child.state):
            self._insert_frontier(child)

    def _heuristic_value(self, node):
        return self.heuristic(node.state, self.problem.goal)
