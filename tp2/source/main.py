#!/usr/bin/env python3

import argparse
from qlearning import QLearning
import numpy as np


def read_map(filename, skip=0):
    with open(filename, 'r') as f:
        for _ in range(skip):
            next(f)                            # Skip line

        return [list(line.rstrip()) for line in f]


d = ('direita', 'esquerda', 'acima', 'abaixo')
a = ('>', '<', '^', 'v')


def print_q(maze, q):
    for i, line in enumerate(maze):
        for j, element in enumerate(line):
            if element != '#':
                for action, q_value in zip(d, q[i][j]):
                    print('%d,%d,%s,%f' % (i, j, action, q_value))


def main(map_file, alpha, discount, n_iterations):

    maze = read_map(map_file, 1)

    for line in maze:
        print(''.join(line))

    qlearn = QLearning(maze, alpha, discount, n_iterations, seed=1)
    q = qlearn.run()

    print_q(maze, q)
    # for line in q:
    #     for element in line:
    #         print(','.join(map(str, element)) + ' ', end='')
    #     print()

    print()

    for i, line in enumerate(maze):
        for j, element in enumerate(line):
            if element == '-':
                print(a[np.argmax(q[i][j])], end='')
            else:
                print(element, end='')
        print()
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file', required=True, help='Input file.')
    parser.add_argument('-a', '--alpha', type=float, required=True,
                        help='Learning rate.')
    parser.add_argument('-d', '--discount', type=float, required=True,
                        help='Discount factor.')
    parser.add_argument('-n', '--iterations', type=int, required=True,
                        help='iterations to be run.')

    args = parser.parse_args()

    map_file = args.file
    alpha = args.alpha
    discount = args.discount
    n_iterations = args.iterations

    main(map_file, alpha, discount, n_iterations)
