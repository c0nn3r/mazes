import time
import random
import numpy as np
from collections import namedtuple

from maze import recursive_backtracker

WIDTH = 1000
HEIGHT = 1000

grid = np.full((HEIGHT, WIDTH), 0, dtype=int)


Point = namedtuple('Point', ['y', 'x'])


def print_maze(grid):
    print(((WIDTH * 2) + 1) * '_')

    for y in range(HEIGHT):
        print('|', end='')
        for x in range(WIDTH):
            if (y + 1 != HEIGHT and grid[y + 1, x] == 4) or grid[y, x] == 3:
                print(' ', end='')
            else:
                print('_', end='')
            if (x + 1 != WIDTH and grid[y, x + 1] == 1) or grid[y, x] == 2:
                print(' ', end='')
            else:
                print('|', end='')
        print('')


recursive_backtracker(0, 0, grid, width=WIDTH, height=HEIGHT)
# print_maze(grid)
