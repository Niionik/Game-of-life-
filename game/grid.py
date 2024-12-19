import numpy as np

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.state = np.zeros((width, height), dtype=bool)

    def toggle_cell(self, x, y):
        if 0 <= x < self.width and 0 <= y < self.height:
            self.state[x, y] = not self.state[x, y]

    def reset(self):
        self.state.fill(False)

    def get_state(self):
        return self.state

    def set_state(self, new_state):
        if new_state.shape == self.state.shape:
            self.state = new_state 