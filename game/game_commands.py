class ResetCommand:
    def __init__(self, grid):
        self.grid = grid

    def execute(self):
        self.grid.reset() 