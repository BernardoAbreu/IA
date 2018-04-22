from node import Node
from numpy import np

def solution(node):
    return []


def child_node(problem, parent, action):
    return Node(problem.result(parent.STATE, action),
                parent.path_cost + problem.step_cost(parent.state, action),
                parent,
                action)


class bfs(object):

    def __empty(self, frontier):
        pass

    def __insert(self, frontier):
        pass

    def __remove(self, frontier):
        pass

    def __init_frontier(self, frontier):
        pass

    def run(self, problem):
        """ returns a solution, or failure

        [description]
        """
        node = Node(problem.initial_state, 0)
        if problem.goal_test(node.state):
            return solution(node)

        # a FIFO queue with node as the only element
        frontier = self.__init_frontier(node)
        explored = set()

        while True:
            if self.__empty(frontier):
                return -1  # Failure

            # chooses the shallowest node in frontier
            node = self.__remove(frontier)
            explored.add(node.state)
            for action in problem.get_actions(node.state):
                child = child_node(problem, node, action)
                if child.state not in explored or child.state not in frontier:
                    if problem.goal_test(child.state):
                        return solution(child)

                    frontier = self.__insert(child, frontier)


def main():
    return
