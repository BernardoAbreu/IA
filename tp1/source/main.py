import numpy as np
from ucs import UCS
from ids import IDS
from best_first_search import BestFirstSearch
from a import AStar
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


def main(map_file, initial_point, goal_point, algo, heuristic='manhattan'):
    map_name, map_matrix = read_map(map_file)

    prob = Problem(map_matrix, initial_point, goal_point)

    if algo == 'astar':
        search = AStar(heuristic)
    elif algo == 'best_first_search':
        search = BestFirstSearch('manhattan')
    elif algo == 'ids':
        search = IDS()
    else:
        search = UCS()

    solution = search.run(prob)
    if solution:
        print(solution[0])
        print(solution[-1])
        print()
        print(' '.join(str(s) for s in solution))
    else:
        print('<' + str(initial_point) + ', 0' + '>')
        print('<' + str(goal_point) + ', inf' + '>')
        print()

    for i, node in enumerate(solution):
        map_matrix[node.state.x, node.state.y] = 'X'
    print('Expanded states: ' + str(search.get_expanded_states()))

    # print(map_matrix)
    np.savetxt('outmap2', map_matrix, delimiter='', fmt='%s')
    return


if __name__ == '__main__':
    map_file = '../maps/map1.map'
    initial_point = Point(29, 21)
    goal_point = Point(60, 19)
    main(map_file, initial_point, goal_point, 'ids')
