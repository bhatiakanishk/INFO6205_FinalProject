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
    
    #Win: If the player has two in a row, they can place a third to get three in a row.
    def two_in_a_row(self, game_board):
        if(self.game_board[0]!=' ' and self.game_board[0] == self.game_board[1]):
            return 2
        elif(self.game_board[0]!=' ' and self.game_board[0] == self.game_board[3]):
            return 6
        elif(self.game_board[0]!=' ' and self.game_board[0] == self.game_board[4]):
            return 8
        elif(self.game_board[1]!=' ' and self.game_board[1] == self.game_board[4]):
            return 7
        elif(self.game_board[1]!=' ' and self.game_board[1] == self.game_board[2]):
            return 0
        elif(self.game_board[2]!=' ' and self.game_board[2] == self.game_board[5]):
            return 8
        elif(self.game_board[2]!=' ' and self.game_board[2] == self.game_board[4]):
            return 6
        elif(self.game_board[3]!=' ' and self.game_board[3] == self.game_board[4]):
            return 5
        elif(self.game_board[4]!=' ' and self.game_board[4] == self.game_board[5]):
            return 3
        elif(self.game_board[4]!=' ' and self.game_board[4] == self.game_board[6]):
            return 2
        elif(self.game_board[4]!=' ' and self.game_board[4] == self.game_board[7]):
            return 1
        elif(self.game_board[4]!=' ' and self.game_board[4] == self.game_board[8]):
            return 0
        elif(self.game_board[5]!=' ' and self.game_board[5] == self.game_board[8]):
            return 2
        elif(self.game_board[6]!=' ' and self.game_board[6] == self.game_board[3]):
            return 0
        elif(self.game_board[6]!=' ' and self.game_board[6] == self.game_board[7]):
            return 8
        elif(self.game_board[7]!=' ' and self.game_board[7] == self.game_board[8]):
            return 6
        else:
            return -1
    
    #Center: A player marks the center.
    def center(self, game_board):
        if(self.game_board[4] == ' '):
            return 4
        else:
            return -1
