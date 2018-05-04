#!/usr/bin/env python3

from random import seed
from random import randrange
import sys

seed()

num_points = int(sys.argv[1])

for i in range(num_points):
    for j in range(4):
        print(randrange(256), end=' ')
    print()
