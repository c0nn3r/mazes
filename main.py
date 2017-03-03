import time
import random
import numpy as np
from collections import namedtuple

WIDTH = 30
HEIGHT = 30

grid = np.full((HEIGHT, WIDTH), ' ', dtype=str)

Point = namedtuple('Point', ['y', 'x'])


def valid_point(point, grid):
    if 0 <= point.x <= (grid.shape[1] - 1) and 0 <= point.y <= (grid.shape[0] - 1):
        if grid[point] == ' ':
            return True
    return False


def print_maze(grid):
    print(((WIDTH * 2) + 1) * '_')

    for y in range(HEIGHT):
        print('|', end='')
        for x in range(WIDTH):
            if (y + 1 != HEIGHT and grid[y + 1, x] == 'v') or grid[y, x] == '^':
                print(' ', end='')
            else:
                print('_', end='')
            if (x + 1 != WIDTH and grid[y, x + 1] == '>') or grid[y, x] == '<':
                print(' ', end='')
            else:
                print('|', end='')
        print('')


def check_surrounding(point, grid):
    random_directions = ['right', 'left', 'up', 'down']

    random.shuffle(random_directions)

    for each in random_directions:

        if each is 'right':
            new_point = Point(x=point.x + 1, y=point.y)
            if valid_point(new_point, grid):
                return new_point, 'right'

        elif each is 'left':
            new_point = Point(x=point.x - 1, y=point.y)
            if valid_point(new_point, grid):
                return new_point, 'left'

        elif each is 'up':
            new_point = Point(x=point.x, y=point.y - 1)
            if valid_point(new_point, grid):
                return new_point, 'up'

        elif each is 'down':
            new_point = Point(x=point.x, y=point.y + 1)
            if valid_point(new_point, grid):
                return new_point, 'down'

    return False


def recursive_backtracker(starting_point, grid):

    stack = []
    current_point = starting_point
    last_direction_char = '>'
    direction_to_char = {'right': '>', 'left': '<', 'up': '^', 'down': 'v'}
    backtracking = False

    while True:

        check_result = check_surrounding(current_point, grid)

        if check_result:
            if backtracking:
                last_direction_char = grid[current_point]
            backtracking = False

            stack.append(current_point)
            new_point, new_direction_num = check_result
            new_direction_char = direction_to_char[new_direction_num]

            grid[current_point] = last_direction_char

            current_point = new_point
            last_direction_char = new_direction_char
        else:
            try:
                if not backtracking:
                    grid[current_point] = last_direction_char
                backtracking = True
                current_point = stack.pop()
            except IndexError:
                break


recursive_backtracker(Point(0, 0), grid)
print_maze(grid)
