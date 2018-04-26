import numpy as np
from bfs import bfs
from ucs import ucs
from ids import ids
from best_first_search import best_first_search
from a import a_star
from point import Point
from problem import Problem


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


def main():
    map_name, map_matrix = read_map('map4.map')
    print(map_matrix)

    initial_point = Point(2, 1)
    goal_point = Point(2, 5)
    prob = Problem(map_matrix, initial_point, goal_point)

    solution = a_star(prob)

    if solution:
        print(solution[0])
        print(solution[-1])
        print()
        print(solution)
    else:
        print('<' + str(initial_point) + ', 0' + '>')
        print('<' + str(goal_point) + ', inf' + '>')
        print()

    for i, node in enumerate(solution):
        map_matrix[node.state.x, node.state.y] = str(i)

    print(map_matrix)
    return


if __name__ == '__main__':
    main()
