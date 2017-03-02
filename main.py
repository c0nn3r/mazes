import os
import time
import random
import numpy as np
from collections import namedtuple

WIDTH = 10
HEIGHT = 10

grid = np.full((HEIGHT, WIDTH), ' ', dtype=str)

Point = namedtuple('Point', ['y', 'x'])


def valid_point(point, grid):
    if 0 <= point.x <= (WIDTH - 1) and 0 <= point.y <= (HEIGHT - 1):
        if grid[point] == ' ':
            return True
    return False


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


def recursive_backtracker(current_point, grid):

    stack = []
    current_direction = 1
    last_direction = 1
    direction_to_number = {'right': '>', 'left': '<', 'up': '^', 'down': 'v'}

    while True:
        '''
        os.system('clear')
        print(grid)
        time.sleep(.1)
        '''

        check_result = check_surrounding(current_point, grid)

        if check_result:
            stack.append(current_point)
            new_point, direction = check_result
            current_direction = direction_to_number[direction]

            grid[current_point] = last_direction
            grid[new_point] = current_direction

            current_point = new_point
            last_direction = current_direction
        else:
            try:
                current_point = stack.pop()
            except IndexError:
                break

def scan(grid_line_partial, dir_num):
    scan_val = 0
    for each in grid_line_partial:
        scan_val <<= 1
        scan_val |= each != dir_num
    return scan_val

def wall_profile(grid_line, dir_num1, dir_num2):
    a = scan(grid_line[:len(grid_line)-1], dir_num1)
    b = scan(grid_line[1:], dir_num2)
    return a & b

recursive_backtracker(Point(0, 0), grid)
