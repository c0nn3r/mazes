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


def recursive_backtracker(starting_point, grid): # TODO: Fix

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
        '''
        os.system('clear')
        print(grid)
        time.sleep(.5)
        '''

def scan(grid_line_partial, dir_num):
    scan_val = 0
    for each in grid_line_partial:
        scan_val <<= 1
        scan_val |= each != dir_num
    return scan_val

def grid_line_walls(grid_line, dir_num1, dir_num2):
    a = scan(grid_line[:len(grid_line)-1], dir_num1)
    b = scan(grid_line[1:], dir_num2)
    return a & b

def grid_walls(grid):
    vertical_walls = [grid_line_walls(list(row), '>', '<') for row in grid]
    swapped_grid = np.swapaxes(grid, 0, 1)
    horizontal_walls = [grid_line_walls(list(column), 'v', '^') for column in swapped_grid]
    return vertical_walls, horizontal_walls

recursive_backtracker(Point(0, 0), grid)

test_grid = np.array([['>','v','v','<'],
                      ['v','<','x','^'],
                      ['v','>','v','^'],
                      ['>','^','>','^']])
