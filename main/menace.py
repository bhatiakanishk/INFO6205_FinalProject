import random

class Menace:
    def __init__(self):
        #This is a dictionary of game states (i.e. Matchboxes in Menace machine)
        self.game_states = {}

        #This is an array to store the moves played by Menace. Will be used for training.
        self.moves_played = []

        #Number of beads to add at start of the game
        self.alpha = 3
        #Number of beads to add in case of a win
        self.beta = 3
        #Number of beads to remove in case of a lose
        self.gamma = 1
        #Number of beads to add in case of a draw
        self.delta = 1
    
    def get_moves_played(self):
        return self.moves_played

    def get_game_states(self):
        return self.game_states
    
    def set_game_states(self, game_states):
        self.game_states = game_states

    def reset_moves_played(self):
        self.moves_played = []

    #Function to decide which move Menace will make
    def move_to_make(self, game_board):
        game_board = game_board.convert_board_to_string()
        #Menace will learn game_states as and when it sees them
        if game_board not in self.game_states:
            beads_dataset = []
            print(game_board)
            for iterator, cell in enumerate(game_board):
                if cell == ' ':
                    # Add cell number to beads_dataset
                    beads_dataset.append(iterator)
            # Add 5 beads of the available moves
            self.game_states[game_board] = beads_dataset * self.alpha

        #Get the beads for a particular game state
        available_beads = self.game_states[game_board]

        #Choose a random bead from the set of available beads
        if len(available_beads) > 0:
            chosen_bead = random.choice(available_beads)
            # print("Chosen bead:")
            # print(chosen_bead)

            # Add the game state (i.e. game_board) and the chosen bead (i.e. move) to moves_played to keep track
            self.moves_played.append((game_board, chosen_bead))
        else:
            chosen_bead = -1
        return chosen_bead
        
    def win_result(self):
        #Adding beads to elements in moves_played on winning the game
        print("Menace Wins.")
        for(game_board, chosen_bead) in self.moves_played:
            for iterations in range(self.beta):
                self.game_states[game_board].append(chosen_bead)

    def draw_result(self):
        #Adding beads to elements in moves_played on drawing the game
        print("Menace Draws")
        for(game_board, chosen_bead) in self.moves_played:
            for iterations in range(self.delta):
                self.game_states[game_board].append(chosen_bead)

    def lose_result(self):
        #Confiscate beads from elements in moves_played on loosing the game
        print("Menace Loses.")
        for(game_board, chosen_bead) in self.moves_played:
            curr_state = self.game_states[game_board]
            del curr_state[curr_state.index(chosen_bead)]