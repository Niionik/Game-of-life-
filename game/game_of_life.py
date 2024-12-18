# Feel free to add more files to the program and include them in the main file
# Different programming languages are accepted.

# Requirements
# 1. Make simulation real time
# 2. Add pause / resume logic
# 3. Add save / load logic
# 4. Implement design patterns wherever you think they're suitable
# 5. Provide a brief explanation why you used the chosen design patterns

# High-level logic
# 1. Create and init the simulation grid
# 2. Start the simulation with a tick interval of <n> seconds
# 3. At each tick:
#   3.1. Update the grid - loop over each element of the board
#   3.2. Render new generation

# General approach
# 1. Plan & write down the general workflow
#  1.1. Define Input&Output 
#  1.2. Consider adding validation
# 2. Separate the main algorithms / actors in the code. Try to abstract as much common code as possible
# 3. Define communication between the objects
# 4. List the patterns you could apply
# 5. Build PoCs (Proof of concepts). Try to separate implementation of specific steps. Prepare smaller modules
#    and combine them into a complete application
# 6. Refine if needed

# Deadline - 20th of December 2024
# Way of handing the projects over will be defined 24.11.2024

import pygame
import numpy as np
from game_state import GameOfLife
from ui import draw_button, draw_grid, draw_cells

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Grid dimensions
n_cells_x, n_cells_y = 40, 30
cell_width = width // n_cells_x
cell_height = height // n_cells_y

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
green = (0, 255, 0)

# Button dimensions
button_width, button_height = 200, 50
button_x, button_y = (width - button_width * 3) // 2, height - button_height - 10

# Initialize games
games = [GameOfLife(n_cells_x, n_cells_y)]
current_game_index = 0

def switch_game(index):
    global current_game_index
    if 0 <= index < len(games):
        current_game_index = index

def draw_buttons():
    # Draw "Next Generation" button
    draw_button(screen, button_x, button_y, button_width, button_height, "Next Generation", green, black)
    # Draw "Save" button
    draw_button(screen, button_x + button_width + 10, button_y, button_width, button_height, "Save", green, black)
    # Draw "Load" button
    draw_button(screen, button_x + 2 * (button_width + 10), button_y, button_width, button_height, "Load", green, black)

running = True
while running:
    screen.fill(white)
    draw_grid(screen, width, height, cell_width, cell_height, gray)
    draw_cells(screen, games[current_game_index].state, cell_width, cell_height, black)
    draw_buttons()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_x <= event.pos[0] <= button_x + button_width and button_y <= event.pos[1] <= button_y + button_height:
                games[current_game_index].next_generation()
            elif button_x + button_width + 10 <= event.pos[0] <= button_x + 2 * button_width + 10 and button_y <= event.pos[1] <= button_y + button_height:
                games[current_game_index].save_to_file()
            elif button_x + 2 * (button_width + 10) <= event.pos[0] <= button_x + 3 * button_width + 20 and button_y <= event.pos[1] <= button_y + button_height:
                games[current_game_index].load_from_file()
            else:
                x, y = event.pos[0] // cell_width, event.pos[1] // cell_height
                games[current_game_index].state[x, y] = not games[current_game_index].state[x, y]

pygame.quit()

