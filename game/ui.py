import pygame

def draw_button(screen, button_x, button_y, button_width, button_height, text, color, text_color):
    pygame.draw.rect(screen, color, (button_x, button_y, button_width, button_height))
    font = pygame.font.Font(None, 36)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=(button_x + button_width // 2, button_y + button_height // 2))
    screen.blit(text_surface, text_rect)

def draw_grid(screen, width, height, cell_width, cell_height, color):
    for y in range(0, height, cell_height):
        for x in range(0, width, cell_width):
            cell = pygame.Rect(x, y, cell_width, cell_height)
            pygame.draw.rect(screen, color, cell, 1)

def draw_cells(screen, game_state, cell_width, cell_height, color):
    n_cells_x, n_cells_y = game_state.shape
    for y in range(n_cells_y):
        for x in range(n_cells_x):
            cell = pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)
            if game_state[x, y] == 1:
                pygame.draw.rect(screen, color, cell) 