'''
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
'''

"""
x = {5 : 6, 1.213 : 2, 3.234 : 4, 1.1 : 2}
print(sorted(x.items()))"""

'''x = {}
x[1.1] = (0, 1)
print(x)'''

import pygame
import math

# Initialize Pygame
pygame.init()

# Set screen size and title
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Cone Raycasting")

# Set font
font = pygame.font.SysFont("Arial", 24)

# Set clock
clock = pygame.time.Clock()

# Set colors
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
GREEN = (0, 255, 0)

# Set number of rays and maximum ray length
num_rays = 64
max_ray_length = 300

# Set the cone angle
cone_angle = 45 * (math.pi / 180)
# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Clear the screen
    screen.fill(GRAY)

    # Calculate the angle between the center of the window and the mouse position
    center_angle = math.atan2(mouse_pos[1] - screen_height / 2, mouse_pos[0] - screen_width / 2)

    # Draw the rays
    for i in range(num_rays):
        # Calculate the angle of the ray relative to the center angle
        angle = center_angle + (i - num_rays / 2) * cone_angle / num_rays

        # Calculate the direction of the ray
        direction = [math.cos(angle), math.sin(angle)]

        # Calculate the end point of the ray
        end_point = [screen_width / 2 + direction[0] * max_ray_length, screen_height / 2 + direction[1] * max_ray_length]

        # Calculate the distance between the ray and the center of the window
        distance = math.sqrt((end_point[0] - screen_width / 2) ** 2 + (end_point[1] - screen_height / 2) ** 2)

        # Check if the ray is within the cone angle
        #if math.acos(direction[0]) <= cone_angle / 2 and math.asin(direction[1]) <= cone_angle / 2:
            # Draw the ray
        pygame.draw.line(screen, GREEN, (screen_width / 2, screen_height / 2), end_point)

    # Draw the mouse position
    pygame.draw.circle(screen, BLACK, mouse_pos, 5)

    # Update the screen
    pygame.display.update()

    # Limit frame rate
    clock.tick(60)
