class Menace:
    def __init__(self):
        #This is a dictionary of game states (i.e. Matchboxes in Menace machine)
        self.game_states = {}

        #This is an array to store the moves played by Menace. Will be used for training.
        self.moves_played = []