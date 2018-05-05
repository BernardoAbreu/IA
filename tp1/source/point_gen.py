#!/usr/bin/env python3

import numpy as np
from random import seed
from random import randrange
import sys


def read_map(filename, skip=0):
    with open(filename, 'r') as f:
        for _ in range(skip):
            next(f)                            # Skip line

        matrix = np.array([list(line.rstrip()) for line in f])

    return matrix


def main(num_points, folder):
    map_files = ['map1.map', 'map2.map', 'map3.map']

    maps = [read_map(folder + m, 4) for m in map_files]

    map_points = [[] for _ in map_files]

    seed()

    while sum(map(len, map_points)) < len(map_points) * num_points:
        points = [randrange(256) for _ in range(4)]

        for i, m in enumerate(maps):
            if m[tuple(points[:2])] == '.' and m[tuple(points[2:])] == '.' \
                    and len(map_points[i]) < num_points \
                    and points not in map_points[i]:
                map_points[i].append(points)

    for filename, m in zip(map_files, map_points):
        with open(filename + '_points', 'w') as f:
            for p in m:
                f.write(' '.join(map(str, p)) + '\n')


if __name__ == '__main__':
    num_points = int(sys.argv[1])
    folder = sys.argv[2]
    main(num_points, folder)
