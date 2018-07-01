#!/usr/bin/env python3

import argparse
from qlearning import QLearning
import numpy as np


d = ('direita', 'esquerda', 'acima', 'abaixo')
a = ('>', '<', '^', 'v')


def read_map(filename, skip=0):
    with open(filename, 'r') as f:
        for _ in range(skip):
            next(f)                            # Skip line

        return [list(line.rstrip()) for line in f]


def save_q(maze, q):
    with open('q.txt', 'w') as f:
        for i, line in enumerate(maze):
            for j, element in enumerate(line):
                if element == '-':
                    for action, q_value in zip(d, q[i][j]):
                        f.write('%d,%d,%s,%f\n' % (i, j, action, q_value))


def main(map_file, alpha, discount, n_iterations):

    maze = read_map(map_file, 1)

    for line in maze:
        print(''.join(line))

    qlearn = QLearning(maze, alpha, discount, n_iterations, seed=1)
    q = qlearn.run()

    save_q(maze, q)

    with open('pi.txt', 'w') as f:
        for i, line in enumerate(maze):
            for j, element in enumerate(line):
                if element == '-':
                    f.write(a[np.argmax(q[i][j])])
                else:
                    f.write(element)
            f.write('\n')
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
