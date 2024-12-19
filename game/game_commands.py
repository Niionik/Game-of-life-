class ResetCommand:
    def __init__(self, game_state):
        self.game_state = game_state

    def execute(self):
        self.game_state.fill(False) 