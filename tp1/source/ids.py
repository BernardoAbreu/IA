# from node import Node
# from util import solution
# from util import child_node
# from explored import ExploredSet
from graph_search import GraphSearch

from collections import deque

from visu import Visu


# class _Frontier(object):
#     def __init__(self, item):
#         self.frontier = deque()
#         self.frontier.append(item)

#     def insert(self, item):
#         self.frontier.append(item)

#     def remove(self):
#         return self.frontier.pop()

#     def is_empty(self):
#         return len(self.frontier) == 0

#     def __contains__(self, state):
#         for node in self.frontier:
#             if state == node.state:
#                 return True

#         return False


# CUTOFF = -1


# def ids(problem):
#     depth = 0
#     while True:
#         result = dfs(problem, depth)
#         if result != CUTOFF:
#             print(depth)
#             return result
#         depth += 1


# def dfs(problem, limit=-1):

#     # with Visu() as v:
#     #     v.init_screen(problem.map)

#     limit_reached = False
#     node = Node(problem.initial, 0)
#     frontier = _Frontier(node)
#     explored = ExploredSet(problem.dimensions)

#     # v.update_coord(node.state, 'o')

#     while True:
#         if frontier.is_empty():
#             return CUTOFF if limit_reached else []

#         node = frontier.remove()
#         # v.update_coord(node.state, '*')

#         if problem.goal_test(node.state):
#             return solution(node)

#         explored.add(node.state)

#         for action in reversed(problem.get_actions(node.state)):
#             child = child_node(problem, node, action)

#             if child.path_cost > limit:
#                 limit_reached = True
#             elif child.state not in explored and child.state not in frontier:
#                 frontier.insert(child)
#                 # v.update_coord(child.state, 'o')


class IDS(GraphSearch):

    def _update_frontier(self, child):
        if child.path_cost > self.limit:
            self.limit_reached = True
        elif self.costs[child.state.x, child.state.y] > child.path_cost or \
                not (self._in_explored(child.state) or
                     self._in_frontier(child.state)):
            self._insert_frontier(child)

    def _init_frontier(self):
        self.frontier = deque()

    def run(self, problem):
        self.limit = 0
        while True:
            self.limit_reached = False
            print(self.limit)
            result = self._run(problem)
            if result or not self.limit_reached:
                return result
            self.limit += 1
