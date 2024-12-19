import numpy as np
import os

class GameStateMemento:
    def __init__(self, state):
        if not isinstance(state, np.ndarray):
            raise ValueError("State must be a numpy array")
        self._state = state.copy()

    def get_state(self):
        return self._state

class GameStateCaretaker:
    def __init__(self):
        self._mementos = []

    def save_state(self, state):
        if not isinstance(state, np.ndarray):
            raise ValueError("State must be a numpy array")
        self._mementos.append(GameStateMemento(state))

    def restore_state(self):
        if self._mementos:
            return self._mementos.pop().get_state()
        return None

    def load_from_file(self, filename="game_state.npy"):
        if not os.path.exists(filename):
            raise FileNotFoundError(f"No such file: {filename}")
        return np.load(filename)

    def save_to_file(self, state, filename="game_state.npy"):
        if not isinstance(state, np.ndarray):
            raise ValueError("State must be a numpy array")
        np.save(filename, state)