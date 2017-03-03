#cython: boundscheck=False, wraparound=False, nonecheck=False
import random
cimport cython
import numpy as np
cimport numpy as np
from libc.stdlib cimport rand

# cdef extern from "limits.h":
#    int RAND_MAX

DTYPE = np.int
ctypedef np.int_t DTYPE_t
# cdef int rand_norm = (int) (24.0 / float(INT_MAX))


cdef bint valid_point(int x, int y, np.ndarray[DTYPE_t, ndim=2] grid, int width, int height):
    return 0 <= x <= (width - 1) and 0 <= y <= (height - 1) and grid[y, x] == 0


cdef check_surrounding(int x, int y, np.ndarray[DTYPE_t, ndim=2] grid, int width, int height):
    # cdef int randnum = (int) (rand() * rand_norm)

    random_directions = [1, 2, 3, 4]
    random.shuffle(random_directions)

    cdef int new_x = 0
    cdef int new_y = 0

    cdef int each

    for each in random_directions:
        new_x = 0
        new_y = 0

        if each == 1:
            new_x = x + 1
            if valid_point(new_x, y, grid, width, height):
                return new_x, y, 1

        elif each == 2:
            new_x  = x - 1
            if valid_point(new_x, y, grid, width, height):
                return new_x, y, 2

        elif each == 3:
            new_y = y - 1
            if valid_point(x, new_y, grid, width, height):
                return x, new_y, 3

        elif each == 4:
            new_y = y + 1
            if valid_point(x, new_y, grid, width, height):
                return x, new_y, 4

    return False


def recursive_backtracker(int current_x, int current_y, np.ndarray[DTYPE_t, ndim=2] grid, int width, int height):

    stack = []
    cdef int last_direction = 0
    cdef bint backtracking = False

    while True:

        check_result = check_surrounding(current_x, current_y, grid, width, height)

        if check_result:
            if backtracking:
                last_direction = grid[current_y, current_x]
            backtracking = False

            stack.append((current_x, current_y))
            new_x, new_y, new_direction = check_result

            grid[current_y, current_x] = last_direction

            current_x, current_y = new_x, new_y
            last_direction = new_direction
        else:
            try:
                if not backtracking:
                    grid[current_y, current_x] = last_direction

                backtracking = True

                current_x, current_y = stack.pop()
            except IndexError:
                break
