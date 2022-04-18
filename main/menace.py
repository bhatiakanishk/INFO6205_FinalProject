import random

class Menace:
    def __init__(self):
        #This is a dictionary of game states (i.e. Matchboxes in Menace machine)
        self.game_states = {}

        #This is an array to store the moves played by Menace. Will be used for training.
        self.moves_played = []

    #Function to decide which move Menace will make1
    def move_to_make(self, game_board):
        #Menace will learn game_states as and when it sees them
        if game_board not in self.game_states:
            beads_dataset = []
            cell_counter = 0
            for cell in game_board:
                if cell != ' ':
                    #Add cell number to beads_dataset
                    beads_dataset.append(cell_counter)
                    cell_counter += 1
            #Add 5 beads of the available moves
            self.game_states[game_board] = beads_dataset * 5

        #Get the beads for a particular game state
        available_beads = self.game_states[game_board]

        #Choose a random bead from the set of available beads
        chosen_bead = random.choice(available_beads)

        #Add the game state (i.e. game_board) and the chosen bead (i.e. move) to moves_played to keep track
        self.moves_played.append(game_board, chosen_bead)
        return chosen_bead
        
    def win_result(self):
        #Adding beads to elements in moves_played on winning the game
        pass

    def draw_result(self):
        #Adding beads to elements in moves_played on drawing the game
        pass

    def lose_result(self):
        #Confiscate beads from elements in moves_played on loosing the game
        pass