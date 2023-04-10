import random
import math
import svgwrite

# Set up the SVG canvas
canvas_width = 500
canvas_height = 500
dwg = svgwrite.Drawing('truchet_smith.svg', size=(canvas_width, canvas_height))

# Define a function to draw a half circle
def draw_half_circle(x, y, r, color):
    path = dwg.path(d=f"M{x},{y} A{r},{r} 0 0 1 {x + r * 2},{y} L{x + r},{y} Z", fill=color)
    dwg.add(path)

# Define a function to draw a Smith Truchet tile
def draw_truchet_smith(x, y, size):
    # Generate a random orientation (0 or 1)
    orientation = random.randint(0, 1)

    # Draw the two half circles in the appropriate positions
    if orientation == 0:
        draw_half_circle(x, y + size/2, size/2, 'black')
        draw_half_circle(x + size/2, y, size/2, 'white')
    else:
        draw_half_circle(x, y, size/2, 'white')
        draw_half_circle(x + size/2, y + size/2, size/2, 'black')

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
