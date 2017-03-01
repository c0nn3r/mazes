import random
import numpy as np
from collections import namedtuple

WIDTH = 10
HEIGHT = 10

grid = np.full((WIDTH, HEIGHT), 0)

Point = namedtuple('Point', ['x', 'y'])


def valid_point(point, grid):
    if 0 <= point.x <= (WIDTH - 1) and 0 <= point.y <= (HEIGHT - 1):
        if grid[point] == 0:
            return True
    return False


def check_surrounding(point, grid):
    random_directions = ['right', 'left', 'top', 'bottom']

    random.shuffle(random_directions)

    for each in random_directions:
        if each is 'right':
            new_point = Point(x=point.x + 1, y=point.y)
            if valid_point(new_point, grid) is True:
                return new_point, 1

        elif each is 'left':
            new_point = Point(x=point.x + -1, y=point.y)
            if valid_point(new_point, grid) is True:
                return new_point, 2

        elif each is 'top':
            new_point = Point(x=point.x, y=point.y + -1)
            if valid_point(new_point, grid) is True:
                return new_point, 3

        elif each is 'bottom':
            new_point = Point(x=point.x, y=point.y + 1)
            if valid_point(new_point, grid) is True:
                return new_point, 4

    return False


def recursive_backtracker(current_point, grid):
    stack = []
    direction = 1

    while True:

        grid[current_point] = direction
        check_result = check_surrounding(current_point, grid)

        if check_result:
            stack.append(current_point)
            current_point, direction = check_result
        else:
            try:
                current_point = stack.pop()
                continue
            except IndexError:
                break


recursive_backtracker(Point(0, 0), grid)

print(grid)


def print_maze(grid):
    for row in grid:
        print('|', end='')
        for direction in row:
            # right
            if direction == 1:
                print(' |', end='')
            # left
            elif direction == 2:
                print('| ', end='')
            # top
            elif direction == 3:
                print('``', end='')
            # bottom
            elif direction == 4:
                print('__', end='')
        print('|')


print_maze(grid)
