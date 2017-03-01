import random
import numpy as np
from collections import namedtuple

WIDTH, HEIGHT = 10, 10

grid = np.full((WIDTH, HEIGHT), 'N', dtype=str)

point = namedtuple('Point', ['x', 'y'])


def directions_iterator():
    directions = ['R', 'L', 'D', 'U']

    random.shuffle(directions)

    for each in directions:
        yield each


new_direction_x = {'R': 1, 'L': -1, 'D': 0, 'U': 0}
new_direction_y = {'R': 0, 'L': 0, 'D': -1, 'U': 1}

opposite_direction = {'R': 'L', 'L': 'R', 'U': 'D', 'D': 'U'}


def carve_passages_from(current_point, grid):
    for each in directions_iterator():

        new_point = point(current_point.x + new_direction_x[each],
                          current_point.y + new_direction_y[each])

        if 0 <= new_point.x <= (WIDTH - 1) and 0 <= new_point.y <= (HEIGHT - 1) and grid[new_point.x][new_point.y] == 'N':
            grid[current_point.x][current_point.y] = each
            grid[new_point.x][new_point.y] = opposite_direction[each]

            carve_passages_from(new_point, grid)


carve_passages_from(point(0, 0), grid)


print(grid)

for y in range(HEIGHT):
    print('|')
    for x in range(WIDTH):
        if grid[y][x] == 'R':
            print('___', end='')
        elif grid[y][x] == 'L':
            print('___', end='')
        elif grid[y][x] == 'U':
            print('| |', end='')
        elif grid[y][x] == 'D':
            print('| |', end='')
print('')
