import random
import svgwrite

# define the size of the grid and the size of the tiles
grid_size = 10
tile_size = 50

# define color options
color_options = ['black', 'red', 'blue', 'green', 'orange']

# create a new SVG drawing
dwg = svgwrite.Drawing(filename='labyrinth_colors.svg', size=(grid_size*tile_size, grid_size*tile_size))

# loop through each tile in the grid
for i in range(grid_size):
    for j in range(grid_size):
        # generate a random number to determine the orientation of the tile
        rand_num = random.random()
        if rand_num < 0.5:
            # draw a white square with a diagonal line in the top-left to bottom-right direction
            dwg.add(dwg.rect((i*tile_size, j*tile_size), (tile_size, tile_size), fill='white'))
            dwg.add(dwg.line((i*tile_size, j*tile_size), ((i+1)*tile_size, (j+1)*tile_size), stroke=random.choice(color_options)))
        else:
            # draw a white square with a diagonal line in the top-right to bottom-left direction
            dwg.add(dwg.rect((i*tile_size, j*tile_size), (tile_size, tile_size), fill='white'))
            dwg.add(dwg.line(((i+1)*tile_size, j*tile_size), (i*tile_size, (j+1)*tile_size), stroke=random.choice(color_options)))

# save the drawing
dwg.save()
