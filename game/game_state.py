import numpy as np
import pickle
import pygame

class GameStateMemento:
    def __init__(self, state):
        self.state = np.copy(state)

class GameOfLife:
    def __init__(self, n_cells_x, n_cells_y):
        self.state = np.random.choice([0, 1], size=(n_cells_x, n_cells_y), p=[0.8, 0.2])

    def save_state(self):
        return GameStateMemento(self.state)

    def load_state(self, memento):
        self.state = np.copy(memento.state)

    def save_to_file(self, filename="game_state.pkl"):
        with open(filename, 'wb') as f:
            pickle.dump(self.state, f)
        print("Game state saved successfully.")

    def load_from_file(self, filename="game_state.pkl"):
        try:
            with open(filename, 'rb') as f:
                self.state = pickle.load(f)
        except FileNotFoundError:
            print("No saved game state found.")

    def next_generation(self):
        new_state = np.copy(self.state)
        n_cells_x, n_cells_y = self.state.shape
        for y in range(n_cells_y):
            for x in range(n_cells_x):
                n_neighbors = self.state[(x - 1) % n_cells_x, (y - 1) % n_cells_y] + \
                              self.state[(x)     % n_cells_x, (y - 1) % n_cells_y] + \
                              self.state[(x + 1) % n_cells_x, (y - 1) % n_cells_y] + \
                              self.state[(x - 1) % n_cells_x, (y)     % n_cells_y] + \
                              self.state[(x + 1) % n_cells_x, (y)     % n_cells_y] + \
                              self.state[(x - 1) % n_cells_x, (y + 1) % n_cells_y] + \
                              self.state[(x)     % n_cells_x, (y + 1) % n_cells_y] + \
                              self.state[(x + 1) % n_cells_x, (y + 1) % n_cells_y]

                if self.state[x, y] == 1 and (n_neighbors < 2 or n_neighbors > 3):
                    new_state[x, y] = 0
                elif self.state[x, y] == 0 and n_neighbors == 3:
                    new_state[x, y] = 1

        self.state = new_state

def draw_text(screen, text, x, y, font_size=36, color=(0, 0, 0)):
    font = pygame.font.Font(None, font_size)
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))