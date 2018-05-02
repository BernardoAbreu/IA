# from node import Node
# from util import solution
# from util import child_node
# from explored import ExploredSet
from graph_search import GraphSearch

import heapq

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
#         for node in self.frontier:
#             if state == node.state:
#                 return True

#         return False

#     def replace_insert(self, item):
#         for i, node in enumerate(self.frontier):
#             if node.state == item.state:
#                 if node.path_cost > item.path_cost:
#                     self.frontier[i] = item
#                     heapq.heapify(self.frontier)
#                 else:
#                     break

#     def __str__(self):
#         return str(self.frontier)


# def ucs(problem):
#     # with Visu() as v:
#     # v.init_screen(problem.map)

#     node = Node(problem.initial, 0)

#     frontier = _Frontier(node)
#     explored = ExploredSet(problem.dimensions)

#     # v.update_coord(node.state, 'o')

#     while True:
#         if frontier.is_empty():
#             return []  # Failure

#         node = frontier.remove()
#         # v.update_coord(node.state, '*')

#         if problem.goal_test(node.state):
#             return solution(node)

#         explored.add(node.state)

#         for action in problem.get_actions(node.state):
#             child = child_node(problem, node, action)

#             if child.state in frontier:
#                 # if child.STATE is in frontier with higher PATH-COST
#                 # then replace frontier node with child
#                 frontier.replace_insert(child)
#             elif child.state not in explored:
#                 frontier.insert(child)
#                 # v.update_coord(child.state, 'o')

class UCS(GraphSearch):

    def _insert_frontier(self, item):
        self.explored[item.state.x, item.state.y] = self._FRONTIER
        heapq.heappush(self.frontier, item)

    def _remove_frontier(self):
        node = heapq.heappop(self.frontier)
        self.explored[node.state.x, node.state.y] = self._EMPTY
        return node

    def _replace_insert_frontier(self, item):
        for i, node in enumerate(self.frontier):
            if node.state == item.state:
                if node.path_cost > item.path_cost:
                    self.frontier[i] = item
                    heapq.heapify(self.frontier)
                break

    def _update_frontier(self, child):
        if self._in_frontier(child.state):
            # if child.STATE is in frontier with higher PATH-COST
            # then replace frontier node with child
            self._replace_insert_frontier(child)
        elif not self._in_explored(child.state):
            self._insert_frontier(child)
