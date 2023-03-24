
import pygame as pg
import math

# Initialize Pygame
pg.init()

# Set the window size and create a window surface
WINDOW_SIZE = (640, 480)
window = pg.display.set_mode(WINDOW_SIZE)

# Define the colors we will use
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the initial position of the line
line_start = (WINDOW_SIZE[0] // 2, WINDOW_SIZE[1] // 2)

# Set the fixed length of the line
LINE_LENGTH = 100

# Start the main game loop
running = True
while running:

    # Handle events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Get the current position of the mouse
    mouse_pos = pg.mouse.get_pos()

    # Calculate the direction and distance to the mouse position
    direction = [mouse_pos[0] - line_start[0], mouse_pos[1] - line_start[1]]
    distance = math.sqrt(direction[0] ** 2 + direction[1] ** 2)

    # Normalize the direction vector
    direction[0] /= distance
    direction[1] /= distance

    # Calculate the end position of the line
    line_end = (line_start[0] + direction[0] * LINE_LENGTH, line_start[1] + direction[1] * LINE_LENGTH)

    # Clear the screen
    window.fill(WHITE)

    # Draw the line
    pg.draw.line(window, RED, line_start, line_end, width=4)

    # Update the screen
    pg.display.flip()

# Quit Pygame properly
pg.quit()
