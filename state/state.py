
import pygame

import time

# Define colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Define state class
class State:
    def __init__(self):
        self.state_num = 1

    def change_state(self):
        if self.state_num == 3:
            self.state_num = 1
        else:
            self.state_num += 1

    def get_color(self):
        if self.state_num == 1:
            return BLUE
        elif self.state_num == 2:
            return RED
        else:
            return GREEN

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 300
screen_height = 100
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("State Design Pattern Example")

# Set up the font
font = pygame.font.SysFont(None, 36)

# Set up the state and timer
state = State()
timer = time.time()

# Set up the circle
circle_radius = 30
circle_x = screen_width - circle_radius - 40
circle_y = screen_height // 2

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the circle
    pygame.draw.circle(screen, state.get_color(), (circle_x, circle_y), circle_radius)

    # Update the state every 2 seconds
    if time.time() - timer >= 2:
        state.change_state()
        timer = time.time()

    # Draw the state counter
    text = font.render("State: " + str(state.state_num), True, (0, 0, 0))
    text_rect = text.get_rect()
    text_rect.left = circle_x - text_rect.width - 50 # modified line
    text_rect.centery = circle_y
    screen.blit(text, text_rect)

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
