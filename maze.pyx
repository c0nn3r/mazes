'''#cython: boundscheck=False, wraparound=False, nonecheck=False'''

import random
cimport cython

import numpy as np
cimport numpy as np

DTYPE = np.int
ctypedef np.int_t DTYPE_t

import numpy as np
from collections import namedtuple

Point = namedtuple('Point', ['y', 'x'])


def valid_point(point, np.ndarray[DTYPE_t, ndim=2] grid):
    if 0 <= point.x <= (grid.shape[1] - 1) and 0 <= point.y <= (grid.shape[0] - 1):
        if grid[point] == 0:
            return True
    return False


def check_surrounding(point, np.ndarray[DTYPE_t, ndim=2] grid):
    random_directions = [1, 2, 3, 4]

    random.shuffle(random_directions)

    for each in random_directions:

        if each == 1:
            new_point = Point(x=point.x + 1, y=point.y)
            if valid_point(new_point, grid):
                return new_point, 1

        elif each == 2:
            new_point = Point(x=point.x - 1, y=point.y)
            if valid_point(new_point, grid):
                return new_point, 2

        elif each == 3:
            new_point = Point(x=point.x, y=point.y - 1)
            if valid_point(new_point, grid):
                return new_point, 3

        elif each == 4:
            new_point = Point(x=point.x, y=point.y + 1)
            if valid_point(new_point, grid):
                return new_point, 4

    return False


def recursive_backtracker(starting_point, np.ndarray[DTYPE_t, ndim=2] grid):

    stack = []
    current_point = starting_point
    cdef int last_direction_char = 0
    backtracking = False

    while True:

        check_result = check_surrounding(current_point, grid)

        if check_result:
            if backtracking:
                last_direction_char = grid[current_point]
            backtracking = False

            stack.append(current_point)
            new_point, new_direction_num = check_result
            new_direction_char = new_direction_num

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
