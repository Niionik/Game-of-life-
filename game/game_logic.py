class Game:
    def __init__(self, grid):
        self.grid = grid

    def next_generation(self):
        new_state = self.grid.get_state().copy()
        for x in range(self.grid.width):
            for y in range(self.grid.height):
                alive_neighbors = self.count_alive_neighbors(x, y)
                if self.grid.state[x, y]:
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        new_state[x, y] = False
                else:
                    if alive_neighbors == 3:
                        new_state[x, y] = True
        self.grid.set_state(new_state)

    def count_alive_neighbors(self, x, y):
        count = 0
        for i in range(max(0, x-1), min(self.grid.width, x+2)):
            for j in range(max(0, y-1), min(self.grid.height, y+2)):
                if (i, j) != (x, y) and self.grid.state[i, j]:
                    count += 1
        return count 