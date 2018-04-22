from node import Node
from node import solution
from point import Point
from problem import Problem
import numpy as np
from collections import deque


def read_map(filename):
    with open(filename, 'r') as f:
        f.readline()                            # Skip first line
        _, height = f.readline().split()
        _, width = f.readline().split()
        map_name = f.readline().rstrip()
        matrix = np.array([list(line.rstrip()) for line in f])

    height = int(height)
    width = int(width)
    return map_name, matrix


def child_node(problem, parent, action):
    return Node(problem.result(parent.state, action),
                parent.path_cost + problem.step_cost(parent.state, action),
                parent,
                action)


class ExploredSet(object):

    def __init__(self, dimensions):
        self.visited = np.zeros(dimensions, dtype=bool)

    def __contains__(self, key):
        return self.visited[key.x, key.y]

    def add(self, key):
        self.visited[key.x, key.y] = True


class Frontier(object):
    def __init__(self, item):
        self.frontier = deque()
        self.frontier.append(item)

    def insert(self, item):
        self.frontier.append(item)

    def remove(self):
        return self.frontier.popleft()

    def is_empty(self):
        return len(self.frontier) == 0

    def __contains__(self, state):
        for node in self.frontier:
            if state == node.state:
                return True

        return False


class BFS(object):

    def run(self, problem):
        node = Node(problem.initial, 0)
        if problem.goal_test(node.state):
            return solution(node)

        # a FIFO queue with node as the only element
        frontier = Frontier(node)
        explored = ExploredSet(problem.dimensions)

        while True:
            if frontier.is_empty():
                return []  # Failure

            # chooses the shallowest node in frontier
            node = frontier.remove()
            explored.add(node.state)
            for action in problem.get_actions(node.state):
                child = child_node(problem, node, action)
                if child.state not in explored or child.state not in frontier:
                    if problem.goal_test(child.state):
                        return solution(child)

                    frontier.insert(child)


def main():
    map_name, map_matrix = read_map('map4.map')
    print(map_matrix)

    p1 = Point(2, 3)
    p2 = Point(2, 7)
    prob = Problem(map_matrix, p1, p2)

    search = BFS()
    solution = search.run(prob)
    print(solution)
    for i, node in enumerate(solution):
        map_matrix[node.state.x, node.state.y] = str(i)

    print(map_matrix)
    return

main()
