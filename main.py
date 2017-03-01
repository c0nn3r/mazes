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
    random_directions = ['right', 'left', 'up', 'down']

    random.shuffle(random_directions)

    for each in random_directions:

        if each is 'right':
            new_point = Point(x=point.x + 1, y=point.y)
            if valid_point(new_point, grid) is True:
                return new_point, 'right'

        elif each is 'left':
            new_point = Point(x=point.x - 1, y=point.y)
            if valid_point(new_point, grid) is True:
                return new_point, 'left'

        elif each is 'up':
            new_point = Point(x=point.x, y=point.y - 1)
            if valid_point(new_point, grid) is True:
                return new_point, 'up'

        elif each is 'down':
            new_point = Point(x=point.x, y=point.y + 1)
            if valid_point(new_point, grid) is True:
                return new_point, 'down'

    return False


def recursive_backtracker(current_point, grid):

    stack = []
    current_direction = 1
    direction_to_number = {'right': 1, 'left': 2, 'up': 3, 'down': 4}

    while True:

        check_result = check_surrounding(current_point, grid)

        if check_result:
            stack.append(current_point)
            new_point, direction = check_result
            current_direction = direction_to_number[direction]

            grid[current_point] = current_direction
            grid[new_point] = current_direction
            current_point = new_point
        else:
            try:
                current_point = stack.pop()
                continue
            except IndexError:
                break


recursive_backtracker(Point(0, 0), grid)

print(grid)
