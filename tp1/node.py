class Node():

    def __init__(self, state, path_cost, parent=None, action=None):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = path_cost
