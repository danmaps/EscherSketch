import random
from PIL import Image

def tile(in_png):
    # Define the input and output file names
    input_filename = in_png
    output_filename = 'tileoutput.png'

    # Load the input image and determine its size
    img = Image.open(input_filename)
    width, height = img.size

    # Set up the output image
    output_img = Image.new('RGB', (width, height), color='white')

    # Define a function to draw a rotated tile
    def draw_tile(image, x, y, size):
        # Generate a random rotation angle (in degrees)
        rotation = random.randint(0, 3) * 90

        # Rotate the tile
        rotated_image = image.rotate(rotation, expand=True)

        # Get the size of the rotated tile
        rotated_width, rotated_height = rotated_image.size

        # Calculate the position to draw the rotated tile
        x_pos = x + int((size - rotated_width) / 2)
        y_pos = y + int((size - rotated_height) / 2)

        # Paste the rotated tile onto the output image
        output_img.paste(rotated_image, (x_pos, y_pos), rotated_image)

    # Set the tile size and grid size
    tile_size = 100
    grid_size = 3

    # Draw the tiles in a grid
    for i in range(grid_size):
        for j in range(grid_size):
            x = i * tile_size
            y = j * tile_size
            draw_tile(img, x, y, tile_size)

    # Save the output image
    output_img.save(output_filename)


tile('Truchet_tile.png')
