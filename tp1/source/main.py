import numpy as np
import argparse
import time

from ucs import UCS
from ids import IDS
from best_first_search import BestFirstSearch
from a_star import AStar
from point import Point
from problem import Problem


def read_map(filename, skip=0):
    with open(filename, 'r') as f:
        for _ in range(skip):
            next(f)                            # Skip line

        matrix = np.array([list(line.rstrip()) for line in f])

    return matrix


def main(map_file, initial_point, goal_point, algo, heuristic='manhattan',
         stats_file=''):
    map_matrix = read_map(map_file, 4)

    prob = Problem(map_matrix, initial_point, goal_point)

    if algo == 'astar':
        search = AStar(heuristic)
    elif algo == 'bg':
        search = BestFirstSearch('manhattan')
    elif algo == 'ids':
        search = IDS()
    else:
        search = UCS()

    start_time = time.time()
    if map_matrix[initial_point.x, initial_point.y] != '@':
        solution = search.run(prob)
    else:
        solution = []
    total_time = time.time() - start_time

    if solution:
        print(solution[0])
        print(solution[-1])
        print()
        print(' '.join(str(s) for s in solution))
    else:
        print('<' + str(initial_point) + ', 0.0' + '>')
        print('<' + str(goal_point) + ', inf' + '>')
        print()

    if stats_file:
        with open(stats_file, 'w') as f:
            f.write('Initial Point;')
            f.write('Final Point;')
            f.write('Total Cost;')
            f.write('Expanded States;')
            f.write('Execution time')
            f.write('\n')

            f.write(str(initial_point).replace(' ', '') + ';')
            f.write(str(goal_point).replace(' ', '') + ';')
            f.write((str(solution[-1].path_cost) if solution else 'inf') + ';')
            f.write(str(search.get_expanded_states()) + ';')
            f.write(str(total_time))

    # for i, node in enumerate(solution):
    #     map_matrix[node.state.x, node.state.y] = 'X'
    # np.savetxt('outputmap', map_matrix, delimiter='', fmt='%s')
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='Input file.')
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
    parser.add_argument('-he', '--heuristic', type=str, default='manhattan',
                        help='Heuristic function for the search algorithm.')
    parser.add_argument('-s', '--stats', type=str,
                        help='File to store statistics.')

    args = parser.parse_args()

    map_file = args.file
    initial_point = Point(args.initial_x, args.initial_y)
    goal_point = Point(args.final_x, args.final_y)
    stats_file = args.stats
    main(map_file, initial_point, goal_point, args.algorithm, args.heuristic,
         stats_file)
