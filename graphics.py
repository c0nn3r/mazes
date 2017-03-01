"""
import cairocffi as cairo


surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.scale(WIDTH, HEIGHT)  # Normalizing the canvas

ctx.rectangle(0, 0, 1, 1)  # Rectangle(x0, y0, x1, y1)
ctx.fill()


def draw_something():
    ctx.move_to(.1, .5)
    ctx.line_to(.1, .4)  # Line to (x,y)
    ctx.rel_line_to(0.1, -0.1)
    ctx.close_path()
    ctx.set_source_rgb(1, 1, 1)  # Solid color
    ctx.set_line_width(1)
    ctx.stroke()


for i in range(5):
    draw_something()


surface.write_to_png("example.png")  # Output to PNG
"""
