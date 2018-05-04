import numpy as np
from ucs import UCS
from ids import IDS
from best_first_search import BestFirstSearch
from a_star import AStar
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

    if map_matrix[initial_point.x, initial_point.y] != '@':
        solution = search.run(prob)
    else:
        solution = []

    if solution:
        print(solution[0])
        print(solution[-1])
        print()
        print(' '.join(str(s) for s in solution))
    else:
        print('<' + str(initial_point) + ', 0' + '>')
        print('<' + str(goal_point) + ', inf' + '>')
        print()

    print('Expanded states: ' + str(search.get_expanded_states()))

    for i, node in enumerate(solution):
        map_matrix[node.state.x, node.state.y] = 'X'
    np.savetxt('outputmap', map_matrix, delimiter='', fmt='%s')
    return


if __name__ == '__main__':
        parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True,
                        help='Input file.')
    parser.add_argument('-ix', '--initial_x', type=int, required=True,
                        help='X of the initial point.')
    parser.add_argument('-iy', '--initial_y', type=int, required=True,
                        help='Y of the initial point.')
    parser.add_argument('-fx', '--final_x', type=int, required=True,
                        help='X of the final point.')
    parser.add_argument('-fy', '--final_y', type=int, required=True,
                        help='Y of the final point.')
    parser.add_argument('-a', '--algorithm', type=str, default='ucs',
                        help='Search algorithm to be used.')
    parser.add_argument('-h', '--heuristic', type=float, default='manhattan',
                        help='Heuristic function for the search algorithm.')

    args = parser.parse_args()
    print(args)

    map_file = args.file
    initial_point = Point(args.initial_x, args.initial_y)
    goal_point = Point(args.final_x, args.final_y)
    main(map_file, initial_point, goal_point, args.algorithm, args.heuristic)
