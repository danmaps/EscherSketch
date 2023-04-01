import random
import math
import svgwrite

# Set up the SVG canvas
canvas_width = 500
canvas_height = 500
dwg = svgwrite.Drawing('truchet_smith.svg', size=(canvas_width, canvas_height))

# Define a function to draw a quarter circle
def draw_quarter_circle(x, y, r, start_angle, end_angle, color):
    path = dwg.path(d=f"M{x},{y} A{r},{r} 0 0 1 {x + r * math.cos(start_angle)},"
                     f"{y + r * math.sin(start_angle)} "
                     f"L{x + r * math.cos(end_angle)},{y + r * math.sin(end_angle)} "
                     f"A{r},{r} 0 0 0 {x + r * math.cos(start_angle)},{y + r * math.sin(start_angle)} Z",
                     fill=color)
    dwg.add(path)

# Define a function to draw a Smith Truchet tile
def draw_truchet_smith(x, y, size):
    # Generate a random orientation (0 or 1)
    orientation = random.randint(0, 1)

    # Draw the two quarter circles in the appropriate positions
    if orientation == 0:
        draw_quarter_circle(x, y + size/2, size/2, math.pi/2, math.pi, 'black')
        draw_quarter_circle(x + size/2, y, size/2, 0, math.pi/2, 'black')
    else:
        draw_quarter_circle(x, y, size/2, 3*math.pi/2, 0, 'black')
        draw_quarter_circle(x + size/2, y + size/2, size/2, math.pi, 3*math.pi/2, 'black')

# Set the tile size and grid size
tile_size = 100
grid_size = 2

# Draw the tiles in a grid
for i in range(grid_size):
    for j in range(grid_size):
        x = i * tile_size
        y = j * tile_size
        draw_truchet_smith(x, y, tile_size)

# Save the SVG file
dwg.save()
