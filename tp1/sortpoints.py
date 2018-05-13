#!/usr/bin/env python3

import sys
import numpy as np


map_folder = sys.argv[1]

points = []


astar_manhat_filename = 'astar_manhattan_stats'
astar_oct_filename = 'astar_octile_stats'
bg_filename = 'bg_stats'
ucs_filename = 'ucs_stats'
ids_filename = 'ids_stats'

files = [astar_manhat_filename,
         astar_oct_filename,
         bg_filename,
         ucs_filename]

costs = np.loadtxt(map_folder + astar_oct_filename,
                   dtype=float,
                   delimiter=';',
                   skiprows=1,
                   usecols=2)

indices = np.argsort(costs)


with open(map_folder + astar_oct_filename) as f:
    titles = f.readline().rstrip()

for filename in files:
    lines = np.loadtxt(map_folder + filename, skiprows=1, dtype=str)[indices]
    np.savetxt(map_folder + filename + '_sorted', lines,
               fmt='%s', header=titles, comments='')


points = np.loadtxt(map_folder + astar_oct_filename,
                    dtype=str,
                    delimiter=';',
                    skiprows=1,
                    usecols=0)[indices]

d = {}
with open(map_folder + ids_filename, 'r') as f:
    next(f)
    for line in f:
        d[line.split(';')[0]] = line.rstrip()


with open(map_folder + ids_filename + '_sorted', 'w') as f:
    f.write(titles + '\n')
    for p in points:
        if p in d.keys():
            f.write(d[p] + '\n')
