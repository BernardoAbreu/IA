from node import Node


class UCS(object):

    def __init__(self):
        pass

    '''
    function UNIFORM-COST-SEARCH(problem) returns a solution, or failure
    node ← a node with STATE = problem.INITIAL-STATE, PATH-COST = 0
    frontier ← a priority queue ordered by PATH-COST,
                with node as the only element
    explored ←an empty set

        loop do
            if EMPTY?( frontier) then return failure
            node←POP( frontier ) /* chooses the lowest-cost node in frontier */
            if problem.GOAL-TEST(node.STATE) then return SOLUTION(node)
            add node.STATE to explored
            for each action in problem.ACTIONS(node.STATE) do
                child ←CHILD-NODE(problem, node, action)
                if child .STATE is not in explored or frontier then
                    frontier ←INSERT(child , frontier )
                else if
                    replace that frontier node with child
    '''

    def __empty(self, container):
        return True

    def __pop(self, container):
        return 1

    def run(self, problem):
        node = Node()
        frontier = self.__init_frontier(node)
        explored = set()
        while True:
            if self.__empty(frontier):
                return -1  # Failure

            node = self.__pop(frontier)
            if problem.goal_test(node.get_state()):
                return self.__solution(node)
            explored.add(node.get_state())

            for action in problem.get_actions(node.get_state()):
                child = self.__child_node(problem, node, action)
                if child.get_state() not in explored or \
                   child.get_state() not in frontier:
                    frontier = self.__insert(child, frontier)
                else:
                    if child.get_state() in frontier:
                        # child.STATE is in frontier with higher PATH-COST
                        if self.__check_path_cost(child.get_path_cost(),
                                                  child.get_state()):
                            # replace that frontier node with child
                            self.__replace(frontier, child)

        return
