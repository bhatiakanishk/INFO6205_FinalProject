import random
class Human:
    def __init__(self):
        pass
        
    def win_result(self):
        print("Human Player Wins.")
    
    def draw_result(self):
        print("Game Draw.")

    def lose_result(self):
        print("Human Player Loses.")
    
    #Win: If the player has two in a row, they can place a third to get three in a row.
    def two_in_a_row(self, game_board):
        if(game_board[0]!=' ' and game_board[0] == game_board[1]):
            return 2
        elif(game_board[0]!=' ' and game_board[0] == game_board[3]):
            return 6
        elif(game_board[0]!=' ' and game_board[0] == game_board[4]):
            return 8
        elif(game_board[1]!=' ' and game_board[1] == game_board[4]):
            return 7
        elif(game_board[1]!=' ' and game_board[1] == game_board[2]):
            return 0
        elif(game_board[2]!=' ' and game_board[2] == game_board[5]):
            return 8
        elif(game_board[2]!=' ' and game_board[2] == game_board[4]):
            return 6
        elif(game_board[3]!=' ' and game_board[3] == game_board[4]):
            return 5
        elif(game_board[4]!=' ' and game_board[4] == game_board[5]):
            return 3
        elif(game_board[4]!=' ' and game_board[4] == game_board[6]):
            return 2
        elif(game_board[4]!=' ' and game_board[4] == game_board[7]):
            return 1
        elif(game_board[4]!=' ' and game_board[4] == game_board[8]):
            return 0
        elif(game_board[5]!=' ' and game_board[5] == game_board[8]):
            return 2
        elif(game_board[6]!=' ' and game_board[6] == game_board[3]):
            return 0
        elif(game_board[6]!=' ' and game_board[6] == game_board[7]):
            return 8
        elif(game_board[7]!=' ' and game_board[7] == game_board[8]):
            return 6
        else:
            return -1

    #Center: A player marks the center.
    def center(self, game_board):
        if(game_board[4] == ' '):
            return 4
        else:
            return -1

    #Opposite corner: If the opponent is in the corner, the player plays the opposite corner.
    def opposite_corner(self, game_board):
        if(game_board[0] != ' '):
            return 8
        elif(game_board[2] != ' '):
            return 6
        elif(game_board[6] != ' '):
            return 2
        elif(game_board[8] != ' '):
            return 0
        else:
            return -1
    
    #Empty corner: The player plays in a corner square
    def empty_corner(self, game_board):
        corner_list = []
        if(game_board[0] == ' '):
            corner_list.append(0)            
        if(game_board[2] == ' ' ):
            corner_list.append(2)
        if(game_board[6] == ' ' ):
            corner_list.append(6)
        if(game_board[8] == ' ' ):
            corner_list.append(8)
        if(len(corner_list) == 0):
            return -1
        return random.choice(corner_list)
    
    #Empty side: The player plays in a middle square on any of the four sides.
    def empty_side(self, game_board):
        side_list = [1, 3, 5, 7]
        if(game_board[1] == ' '):
            side_list.append(1)            
        if(game_board[3] == ' ' ):
            side_list.append(3)
        if(game_board[5] == ' ' ):
            side_list.append(5)
        if(game_board[7] == ' ' ):
            side_list.append(7)
        if(len(side_list) == 0):
            return -1
        return random.choice(side_list)

    def human_move(self, game_board):
        game_board = game_board.board_string()
        move = -1
        move = self.two_in_a_row(game_board)
        if move == -1:
            move = self.center(game_board)
        if move == -1:
            move = self.opposite_corner(game_board)
        if move == -1:
            move = self.empty_corner(game_board)
        if move == -1:
            move = self.empty_side(game_board)

        return move