class Human:
    def __init__(self):
        pass

    def human_move(self):
        input_move = input("Make a move on the board:")
        return input_move
    def win_result(self):
        print("Human Player Wins.")
    
    def draw_result(self):
        print("Game Draw.")

    def lose_result(self):
        print("Human Player Loses.")