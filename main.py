import numpy as np
import svgwrite as sw

from maze import recursive_backtracker

WIDTH = 100
HEIGHT = 100

grid = np.full((HEIGHT, WIDTH), 0, dtype=int)

def print_maze(grid): print(((WIDTH * 2) + 1) * '_')

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


def save_maze_to_svg(path, grid):
    maze_height = 10
    maze_width = 10

    svg = sw.Drawing(filename=path, size=(str(WIDTH * maze_width + 100) + 'px', str(HEIGHT * maze_height + 100) + 'px'))
    svg.add(svg.line((0.5, 1), (WIDTH * maze_width + 1.5, 1), stroke=sw.rgb(1, 1, 1, '%')))
    svg.add(svg.line((1, 0.5), (1, HEIGHT * maze_height + 1.5), stroke=sw.rgb(1, 1, 1, '%')))

    for y in range(HEIGHT):

        for x in range(WIDTH):
            if (y + 1 != HEIGHT and grid[y + 1, x] == 'v') or grid[y, x] == '^':
                pass
            else:
                svg.add(svg.line((x * maze_width + 0.5, (y + 1) * maze_width + 1), ((x + 1) * maze_width + 1.5, (y + 1) * maze_height + 1), stroke=sw.rgb(1, 1, 1, '%')))
            if (x + 1 != WIDTH and grid[y, x + 1] == '>') or grid[y, x] == '<':
                pass
            else:
                svg.add(svg.line(((x + 1) * maze_width + 1, y * maze_height + 0.5), ((x + 1) * maze_width + 1, ((y + 1) * maze_height) + 1.5), stroke=sw.rgb(1, 1, 1, '%')))

    svg.save()


recursive_backtracker(0, 0, grid, width=WIDTH, height=HEIGHT)
save_maze_to_svg('test.svg', grid)
