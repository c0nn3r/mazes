import time
import random
import numpy as np
import subprocess as sp
from collections import namedtuple

WIDTH, HEIGHT = 40, 40

grid = np.full((WIDTH, HEIGHT), 'N', dtype=str)

point = namedtuple('Point', ['x', 'y'])


def directions_iterator():
    directions = ['→', '←', '↓', '↑']

    random.shuffle(directions)

    for each in directions:
        yield each


new_direction_x = {'→': 1, '←': -1, '↓': 0, '↑': 0}
new_direction_y = {'→': 0, '←': 0, '↓': -1, '↑': 1}

opposite_direction = {'→': '←', '←': '→', '↑': '↓', '↓': '↑'}


def carve_passages_from(current_point, grid):
    # print(grid)
    # time.sleep(.01)
    # _ = sp.call('clear', shell=True)

    for each in directions_iterator():

        new_point = point(current_point.x + new_direction_x[each],
                          current_point.y + new_direction_y[each])

        if 0 <= new_point.x <= (WIDTH - 1) and 0 <= new_point.y <= (HEIGHT - 1) and grid[new_point.x][new_point.y] == 'N':
            if new_direction_x[each] == 1:
                arrow = '→'
            elif new_direction_x[each] == -1:
                arrow = '←'
            elif new_direction_y[each] == 1:
                arrow = '↑'
            elif new_direction_y[each] == -1:
                arrow = '↓'
            print(arrow)

            grid[current_point.x][current_point.y] = arrow
            grid[new_point.x][new_point.y] = opposite_direction[arrow]

            carve_passages_from(new_point, grid)


carve_passages_from(point(0, 0), grid)


print(grid)

for y in range(HEIGHT):
    print('|', end='')
    for x in range(WIDTH):
        if grid[y][x] == '→':
            print('```', end='')
        elif grid[y][x] == '←':
            print('___', end='')
        elif grid[y][x] == '↑':
            print('| |', end='')
        elif grid[y][x] == '↓':
            print('| |', end='')
    print('|')
