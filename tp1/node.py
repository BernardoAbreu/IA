class Node():

    def __init__(self, state, path_cost, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost

    def __str__(self):
        return '<' + str(self.state) + ', ' + str(self.path_cost) + '>'

    def __repr__(self):
        return self.__str__()

    def __lt__(self, other):
        return self.path_cost < other.path_cost

    def __gt__(self, other):
        return self.path_cost > other.path_cost
