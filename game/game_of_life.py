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
from ui import draw_button
from session_time import SessionTimer
from state_manager import GameStateCaretaker
from speed_controller import SpeedController
from game_commands import ResetCommand

# Initialize Pygame
pygame.init()

# Screen dimensions
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Grid dimensions
n_cells_x, n_cells_y = 40, 30
cell_width = width // n_cells_x
cell_height = height // n_cells_y

# Game state
game_state = np.random.choice([0, 1], size=(n_cells_x, n_cells_y), p=[0.8, 0.2])

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
gray = (128, 128, 128)
green = (0, 255, 0)

# Button dimensions
button_width, button_height = 200, 50
button_x, button_y = (width - button_width) // 2, height - button_height - 10

def draw_grid():
    for y in range(0, height, cell_height):
        for x in range(0, width, cell_width):
            cell = pygame.Rect(x, y, cell_width, cell_height)
            pygame.draw.rect(screen, gray, cell, 1)

def next_generation():
    global game_state
    new_state = np.copy(game_state)

    for y in range(n_cells_y):
        for x in range(n_cells_x):
            n_neighbors = game_state[(x - 1) % n_cells_x, (y - 1) % n_cells_y] + \
                          game_state[(x)     % n_cells_x, (y - 1) % n_cells_y] + \
                          game_state[(x + 1) % n_cells_x, (y - 1) % n_cells_y] + \
                          game_state[(x - 1) % n_cells_x, (y)     % n_cells_y] + \
                          game_state[(x + 1) % n_cells_x, (y)     % n_cells_y] + \
                          game_state[(x - 1) % n_cells_x, (y + 1) % n_cells_y] + \
                          game_state[(x)     % n_cells_x, (y + 1) % n_cells_y] + \
                          game_state[(x + 1) % n_cells_x, (y + 1) % n_cells_y]

            if game_state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                new_state[x, y] = 0
            elif game_state[x, y] == 0 and n_neighbors == 3:
                new_state[x, y] = 1

    game_state = new_state

def draw_cells():
    for y in range(n_cells_y):
        for x in range(n_cells_x):
            cell = pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)
            if game_state[x, y] == 1:
                pygame.draw.rect(screen, black, cell)

clock = pygame.time.Clock()

# Ustawienia czasu
tick_interval = 500  # czas w milisekundach między generacjami
last_update_time = pygame.time.get_ticks()

session_timer = SessionTimer()

paused = False

running = True

# Inicjalizacja
caretaker = GameStateCaretaker()
speed_controller = SpeedController(tick_interval)
reset_command = ResetCommand(game_state)

def draw_timer(screen, x, y):
    font = pygame.font.Font(None, 36)
    elapsed_time = session_timer.get_elapsed_time()
    time_text = f"Time: {elapsed_time // 60}:{elapsed_time % 60:02}"
    text_surface = font.render(time_text, True, black)
    screen.blit(text_surface, (x, y))

while running:
    screen.fill(white)
    draw_grid()
    draw_cells()
    draw_button(screen, button_x, button_y, button_width, button_height, "Next", green, black)
    draw_button(screen, button_x, button_y - 60, button_width, button_height, "Pause" if not paused else "Resume", green, black)
    draw_timer(screen, 10, 10)
    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if not paused and current_time - last_update_time > tick_interval:
        next_generation()
        last_update_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_x <= event.pos[0] <= button_x + button_width and button_y <= event.pos[1] <= button_y + button_height:
                next_generation()
            elif button_x <= event.pos[0] <= button_x + button_width and button_y - 60 <= event.pos[1] <= button_y - 60 + button_height:
                paused = not paused
                if paused:
                    session_timer.pause()
                else:
                    session_timer.resume()
            elif some_reset_button_condition:  # Replace with actual condition
                reset_command.execute()
                session_timer.reset()
            elif some_save_button_condition:  # Replace with actual condition
                try:
                    caretaker.save_state(game_state)
                except ValueError as e:
                    print(f"Error saving state: {e}")
            elif some_load_button_condition:  # Replace with actual condition
                try:
                    loaded_state = caretaker.restore_state()
                    if loaded_state is not None:
                        game_state = loaded_state
                except FileNotFoundError as e:
                    print(f"Error loading state: {e}")
            else:
                x, y = event.pos[0] // cell_width, event.pos[1] // cell_height
                if 0 <= x < grid_width and 0 <= y < grid_height:
                    game_state[x, y] = not game_state[x, y]

    clock.tick(60)

pygame.quit()

