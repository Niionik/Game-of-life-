import pygame
import numpy as np
import pickle
from ui import draw_button
from session_time import SessionTimer
from state_manager import GameStateCaretaker
from speed_controller import SpeedController
from game_commands import ResetCommand
from grid import Grid
from game_logic import Game

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
red = (255, 0, 0)

# Initialize Pygame
pygame.init()
pygame.display.set_caption("Game of Life")

# Initialize clock
clock = pygame.time.Clock()

# Initialization
grid = Grid(n_cells_x, n_cells_y)
game = Game(grid)
tick_interval = 500  # time in milliseconds between generations
reset_command = ResetCommand(grid)
session_timer = SessionTimer()

# Button settings
button_width = 100
button_height = 40
button_x, button_y = (width - button_width) // 2, height - button_height - 10

# Additional button positions
resume_button_x, resume_button_y = button_x, button_y - 60
randomize_button_x, randomize_button_y = button_x, button_y - 120
save_button_x, save_button_y = button_x - 110, button_y - 60
load_button_x, load_button_y = button_x + 110, button_y - 60

# Pause state variable
paused = False

# Variable to store messages and their display time
message = ""
message_time = 0

def draw_grid():
    for x in range(0, n_cells_x * cell_width, cell_width):
        for y in range(0, n_cells_y * cell_height, cell_height):
            rect = pygame.Rect(x, y, cell_width, cell_height)
            pygame.draw.rect(screen, gray, rect, 1)

def draw_cells():
    for x in range(n_cells_x):
        for y in range(n_cells_y):
            if grid.state[x, y]:
                rect = pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)
                pygame.draw.rect(screen, black, rect)

def draw_timer(screen, x, y):
    font = pygame.font.Font(None, 36)
    elapsed_time = session_timer.get_elapsed_time()
    time_text = f"Time: {elapsed_time // 60}:{elapsed_time % 60:02}"
    text_surface = font.render(time_text, True, red)
    screen.blit(text_surface, (x, y))

def draw_message(screen, message, x, y):
    if message:
        font = pygame.font.Font(None, 36)
        text_surface = font.render(message, True, red)
        screen.blit(text_surface, (x, y))

def save_game_state(filename):
    global message, message_time
    try:
        with open(filename, 'wb') as f:
            pickle.dump(grid.get_state(), f)
        message = "Game saved successfully."
    except Exception as e:
        message = f"Error saving game: {e}"
    message_time = pygame.time.get_ticks()

def load_game_state(filename):
    global message, message_time
    try:
        with open(filename, 'rb') as f:
            state = pickle.load(f)
            grid.set_state(state)
        message = "Game loaded successfully."
    except FileNotFoundError:
        message = f"File {filename} not found."
    except Exception as e:
        message = f"Error loading game: {e}"
    message_time = pygame.time.get_ticks()

running = True
last_update_time = pygame.time.get_ticks()

while running:
    screen.fill(white)
    draw_grid()
    draw_cells()
    draw_button(screen, button_x, button_y, button_width, button_height, "Next", green, black)
    draw_button(screen, resume_button_x, resume_button_y, button_width, button_height, "Pause" if not paused else "Resume", green, black)
    draw_button(screen, randomize_button_x, randomize_button_y, button_width, button_height, "Random", green, black)
    draw_button(screen, save_button_x, save_button_y, button_width, button_height, "Save", green, black)
    draw_button(screen, load_button_x, load_button_y, button_width, button_height, "Load", green, black)
    draw_timer(screen, 10, 10)  # Display timer in the top-left corner

    # Display message if less than 6 seconds have passed
    if pygame.time.get_ticks() - message_time < 6000:
        draw_message(screen, message, 10, height - 50)

    pygame.display.flip()

    current_time = pygame.time.get_ticks()
    if not paused and current_time - last_update_time > tick_interval:
        game.next_generation()
        last_update_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_x <= event.pos[0] <= button_x + button_width and button_y <= event.pos[1] <= button_y + button_height:
                game.next_generation()
            elif resume_button_x <= event.pos[0] <= resume_button_x + button_width and resume_button_y <= event.pos[1] <= resume_button_y + button_height:
                paused = not paused
                if paused:
                    session_timer.pause()
                else:
                    session_timer.resume()
            elif randomize_button_x <= event.pos[0] <= randomize_button_x + button_width and randomize_button_y <= event.pos[1] <= randomize_button_y + button_height:
                new_random_state = np.random.choice([0, 1], size=(n_cells_x, n_cells_y), p=[0.8, 0.2])
                grid.set_state(new_random_state)
                message = "Grid randomized."
                message_time = pygame.time.get_ticks()
            elif save_button_x <= event.pos[0] <= save_button_x + button_width and save_button_y <= event.pos[1] <= save_button_y + button_height:
                save_game_state('game_state.pkl')
            elif load_button_x <= event.pos[0] <= load_button_x + button_width and load_button_y <= event.pos[1] <= load_button_y + button_height:
                load_game_state('game_state.pkl')
            else:
                x, y = event.pos[0] // cell_width, event.pos[1] // cell_height
                grid.toggle_cell(x, y)

    clock.tick(60)

pygame.quit()