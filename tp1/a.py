from node import Node
from util import *
from explored import ExploredSet

import heapq

# from visu import Visu


class _Frontier(object):

    def __init__(self, item):
        self.frontier = []
        self.insert(item)

    def insert(self, item):
        heapq.heappush(self.frontier, item)

    def remove(self):
        return heapq.heappop(self.frontier)

    def is_empty(self):
        return len(self.frontier) == 0

    def __contains__(self, state):
        for _, node in self.frontier:
            if state == node.state:
                return True

        return False

    def replace_insert(self, item):
        for i, node in enumerate(self.frontier):
            if node.state == item.state:
                if node.path_cost > item.path_cost:
                    self.frontier[i] = item
                    heapq.heapify(self.frontier)
                else:
                    break

    def __str__(self):
        return str(self.frontier)


def a_star(problem, heuristic='manhattan'):
    fheur = manhattan_distance if heuristic == 'manhattan' else octile_distance
    # with Visu() as v:
    # v.init_screen(problem.map)

    node = Node(problem.initial, 0)
    goal = problem.goal

    frontier = _Frontier((fheur(node.state, goal) + node.path_cost, node))
    explored = ExploredSet(problem.dimensions)

    # v.update_coord(node.state, 'o')

    while True:
        if frontier.is_empty():
            return []  # Failure

        _, node = frontier.remove()
        # v.update_coord(node.state, '*')

        if problem.goal_test(node.state):
            return solution(node)

        explored.add(node.state)

        for action in problem.get_actions(node.state):
            child = child_node(problem, node, action)

            if child.state not in explored and child.state not in frontier:
                heur_value = fheur(child.state, goal) + child.path_cost
                frontier.insert((heur_value, child))
