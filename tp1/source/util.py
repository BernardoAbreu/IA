from node import Node


def solution(node):
    sol_list = []
    aux = node

    while aux is not None:
        sol_list.append(aux)
        aux = aux.parent

    return sol_list[::-1]


def child_node(problem, parent, action):
    return Node(problem.result(parent.state, action),
                parent.path_cost + problem.step_cost(parent.state, action),
                parent,
                action)


def manhattan_distance(node, goal):
    return abs(node.x - goal.x) + abs(node.y - goal.y)


def octile_distance(node, goal):
    dx = abs(node.x - goal.x)
    dy = abs(node.y - goal.y)
    return max(dx, dy) + 0.5 * min(dx, dy)
