class Menace:
    def __init__(self):
        #This is a dictionary of game states (i.e. Matchboxes in Menace machine)
        self.game_states = {}

        #This is an array to store the moves played by Menace. Will be used for training.
        self.moves_played = []

    def win_result(self):
        #Adding beads to elements in moves_played on winning the game
        pass

    def draw_result(self):
        #Adding beads to elements in moves_played on drawing the game
        pass

    def lose_result(self):
        #Confiscate beads from elements in moves_played on loosing the game
        pass