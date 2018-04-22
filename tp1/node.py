class Node():

    def __init__(self, state, path_cost, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __str__(self):
        return '<' + str(self.state.x) + ',' + str(self.state.y) + ',' + \
               str(self.path_cost) + '>'

    def __repr__(self):
        return self.__str__()


def solution(node):
    sol_list = []
    aux = node

    while aux is not None:
        sol_list.append(aux)
        aux = aux.parent

    return sol_list[::-1]
