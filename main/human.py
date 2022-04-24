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
    
    # Win: If the player has two in a row, they can place a third to get three in a row.
    def two_in_a_row(self, game_board):
        if(game_board[0] == 'X' and game_board[1] == 'X' and game_board[2] == ' '):
            return 2
        elif(game_board[0] == 'X' and game_board[3] == 'X' and game_board[6] == ' '):
            return 6
        elif(game_board[0] == 'X' and game_board[4] == 'X' and game_board[8] == ' '):
            return 8
        elif(game_board[1] == 'X' and game_board[4] == 'X' and game_board[7] == ' '):
            return 7
        elif(game_board[1] == 'X' and game_board[2] == 'X' and game_board[0] == ' '):
            return 0
        elif(game_board[2] == 'X' and game_board[5] == 'X' and game_board[8] == ' '):
            return 8
        elif(game_board[2] == 'X' and game_board[4] == 'X' and game_board[6] == ' '):
            return 6
        elif(game_board[3] == 'X' and game_board[4] == 'X' and game_board[5] == ' '):
            return 5
        elif(game_board[4] == 'X' and game_board[5] == 'X' and game_board[3] == ' '):
            return 3
        elif(game_board[4] == 'X' and game_board[6] == 'X' and game_board[2] == ' '):
            return 2
        elif(game_board[4] == 'X' and game_board[7] == 'X' and game_board[1] == ' '):
            return 1
        elif(game_board[4] == 'X' and game_board[8] == 'X' and game_board[0] == ' '):
            return 0
        elif(game_board[5] == 'X' and game_board[8] == 'X' and game_board[2] == ' '):
            return 2
        elif(game_board[6] == 'X' and game_board[3] == 'X' and game_board[0] == ' '):
            return 0
        elif(game_board[6] == 'X' and game_board[7] == 'X' and game_board[8] == ' '):
            return 8
        elif(game_board[7] == 'X' and game_board[8] == 'X' and game_board[6] == ' '):
            return 6
        else:
            return -1

    # Block: If the opponent has two in a row, the player must play the third themselves to block the opponent
    def block_two_in_a_row(self, game_board):
        if(game_board[0] == 'O' and game_board[1] == 'O' and game_board[2] == ' '):
            return 2
        elif(game_board[0] == 'O' and game_board[3] == 'O' and game_board[6] == ' '):
            return 6
        elif(game_board[0] == 'O' and game_board[4] == 'O' and game_board[8] == ' '):
            return 8
        elif(game_board[1] == 'O' and game_board[4] == 'O' and game_board[7] == ' '):
            return 7
        elif(game_board[1] == 'O' and game_board[2] == 'O' and game_board[0] == ' '):
            return 0
        elif(game_board[2] == 'O' and game_board[5] == 'O' and game_board[8] == ' '):
            return 8
        elif(game_board[2] == 'O' and game_board[4] == 'O' and game_board[6] == ' '):
            return 6
        elif(game_board[3] == 'O' and game_board[4] == 'O' and game_board[5] == ' '):
            return 5
        elif(game_board[4] == 'O' and game_board[5] == 'O' and game_board[3] == ' '):
            return 3
        elif(game_board[4] == 'O' and game_board[6] == 'O' and game_board[2] == ' '):
            return 2
        elif(game_board[4] == 'O' and game_board[7] == 'O' and game_board[1] == ' '):
            return 1
        elif(game_board[4] == 'O' and game_board[8] == 'O' and game_board[0] == ' '):
            return 0
        elif(game_board[5] == 'O' and game_board[8] == 'O' and game_board[2] == ' '):
            return 2
        elif(game_board[6] == 'O' and game_board[3] == 'O' and game_board[0] == ' '):
            return 0
        elif(game_board[6] == 'O' and game_board[7] == 'O' and game_board[8] == ' '):
            return 8
        elif(game_board[7] == 'O' and game_board[8] == 'O' and game_board[6] == ' '):
            return 6
        else:
            return -1

    # Center: A player marks the center.
    def center(self, game_board):
        if(game_board[4] == ' '):
            return 4
        else:
            return -1

    # Opposite corner: If the opponent is in the corner, the player plays the opposite corner.
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
    
    # Empty corner: The player plays in a corner square
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
    
    # Empty side: The player plays in a middle square on any of the four sides.
    def empty_side(self, game_board):
        side_list = []
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
    
    # Fork: Cause a scenario where the player has two ways to win
    # Fork A
    def fork_a(self, game_board):
        fork_1 = [] # 1, 4, 5
        fork_2 = [] # 4, 5, 7
        fork_3 = [] # 3, 4, 7
        fork_4 = [] # 1, 3, 4

        if(game_board[1] == ' '):
            fork_1.append(1)
            fork_4.append(1)
        if(game_board[3] == ' '):
            fork_3.append(3)
            fork_4.append(3)
        if(game_board[4] == ' '):
            fork_1.append(4)
            fork_2.append(4)
            fork_3.append(4)
            fork_4.append(4)
        if(game_board[5] == ' '):
            fork_1.append(5)
            fork_2.append(5)
        if(game_board[7] == ' '):
            fork_2.append(7)
            fork_3.append(7)
        if((game_board[1] == ' ' or game_board[4] == ' ' or game_board[5] == ' ') and (game_board[0] == 'X' and game_board[2] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_1)
        elif((game_board[4] == ' ' or game_board[5] == ' ' or game_board[7] == ' ') and (game_board[2] == 'X' and game_board[6] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_2)
        elif((game_board[3] == ' ' or game_board[4] == ' ' or game_board[7] == ' ') and (game_board[0] == 'X' and game_board[6] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_3)
        elif((game_board[1] == ' ' or game_board[3] == ' ' or game_board[4] == ' ') and (game_board[0] == 'X' and game_board[2] == 'X' and game_board[6] == 'X')):
            return random.choice(fork_4)
        else:
            return -1

    # Fork B
    def fork_b(self, game_board):
        fork_1 = [] # 2, 6
        fork_2 = [] # 0, 8

        if(game_board[0] == ' '):
            fork_2.append(0)
        if(game_board[2] == ' '):
            fork_1.append(2)
        if(game_board[6] == ' '):
            fork_1.append(6)
        if(game_board[8] == ' '):
            fork_2.append(8)
        if((game_board[2] == ' ' or game_board[6] == ' ') and (game_board[0] == 'X' and game_board[1] == 'X' and game_board[3] == 'X')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[8] == ' ') and (game_board[1] == 'X' and game_board[2] == 'X' and game_board[5] == 'X')):
            return random.choice(fork_2)
        elif((game_board[2] == ' ' or game_board[6] == ' ') and (game_board[5] == 'X' and game_board[7] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[8] == ' ') and (game_board[3] == 'X' and game_board[6] == 'X' and game_board[7] == 'X')):
            return random.choice(fork_2)
        else:
            return -1
    
    # Fork C
    def fork_c(self, game_board):
        fork_1 = [] # 5, 7
        fork_2 = [] # 3, 7
        fork_3 = [] # 1, 3
        fork_4 = [] # 1, 5

        if(game_board[1] == ' '):
            fork_3.append(1)
            fork_4.append(1)
        if(game_board[3] == ' '):
            fork_2.append(3)
            fork_3.append(3)
        if(game_board[5] == ' '):
            fork_1.append(5)
            fork_4.append(5)
        if(game_board[7] == ' '):
            fork_1.append(7)
            fork_2.append(7)
        if((game_board[5] == ' ' or game_board[7] == ' ') and (game_board[1] == 'X' and game_board[3] == 'X' and game_board[4] == 'X')):
            return random.choice(fork_1)
        elif((game_board[3] == ' ' or game_board[7] == ' ') and (game_board[1] == 'X' and game_board[4] == 'X' and game_board[5] == 'X')):
            return random.choice(fork_2)
        elif((game_board[1] == ' ' or game_board[3] == ' ') and (game_board[4] == 'X' and game_board[5] == 'X' and game_board[7] == 'X')):
            return random.choice(fork_3)
        elif((game_board[1] == ' ' or game_board[5] == ' ') and (game_board[3] == 'X' and game_board[4] == 'X' and game_board[7] == 'X')):
            return random.choice(fork_4)
        else:
            return -1

    # Fork D
    def fork_D(self, game_board):
        fork_1 = [] # 5, 6, 8
        fork_2 = [] # 0, 7, 8
        fork_3 = [] # 0, 2, 3
        fork_4 = [] # 1, 2, 8

        if(game_board[0] == ' '):
            fork_2.append(0)
            fork_3.append(0)
        if(game_board[1] == ' '):
            fork_4.append(1)
        if(game_board[2] == ' '):
            fork_3.append(2)
            fork_4.append(2)
        if(game_board[3] == ' '):
            fork_3.append(3)
        if(game_board[5] == ' '):
            fork_1.append(5)
        if(game_board[6] == ' '):
            fork_1.append(6)
        if(game_board[7] == ' '):
            fork_2.append(7)
        if(game_board[8] == ' '):
            fork_1.append(8)
            fork_2.append(8)
            fork_4.append(8)
        if((game_board[5] == ' ' or game_board[6] == ' ' or game_board[8] == ' ') and (game_board[0] == 'X' and game_board[3] == 'X' and game_board[4] == 'X')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[7] == ' ' or game_board[8] == ' ') and (game_board[1] == 'X' and game_board[2] == 'X' and game_board[4] == 'X')):
            return random.choice(fork_2)
        elif((game_board[0] == ' ' or game_board[2] == ' ' or game_board[3] == ' ') and (game_board[4] == 'X' and game_board[5] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_3)
        elif((game_board[1] == ' ' or game_board[2] == ' ' or game_board[8] == ' ') and (game_board[4] == 'X' and game_board[6] == 'X' and game_board[7] == 'X')):
            return random.choice(fork_4)
        else:
            return -1

    # Fork E
    def fork_e(self, game_board):
        fork_1 = [] # 1, 6
        fork_2 = [] # 0, 5
        fork_3 = [] # 2, 7
        fork_4 = [] # 3, 8

        if(game_board[0] == ' '):
            fork_2.append(0)
        if(game_board[1] == ' '):
            fork_1.append(1)
        if(game_board[2] == ' '):
            fork_3.append(2)
        if(game_board[3] == ' '):
            fork_4.append(3)
        if(game_board[5] == ' '):
            fork_2.append(5)
        if(game_board[6] == ' '):
            fork_1.append(6)
        if(game_board[7] == ' '):
            fork_3.append(7)
        if(game_board[8] == ' '):
            fork_4.append(8)
        if((game_board[1] == ' ' or game_board[6] == ' ') and (game_board[0] == 'X' and game_board[2] == 'X' and game_board[3] == 'X')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[5] == ' ') and (game_board[1] == 'X' and game_board[2] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_2)
        elif((game_board[2] == ' ' or game_board[7] == ' ') and (game_board[5] == 'X' and game_board[6] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_3)
        elif((game_board[3] == ' ' or game_board[8] == ' ') and (game_board[0] == 'X' and game_board[6] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_4)
        else:
            return -1
    
    # Fork F
    def fork_f(self, game_board):
        fork_1 = [] # 4, 6
        fork_2 = [] # 0, 4
        fork_3 = [] # 2, 4
        fork_4 = [] # 4, 8

        if(game_board[0] == ' '):
            fork_2.append(0)
        if(game_board[2] == ' '):
            fork_3.append(2)
        if(game_board[4] == ' '):
            fork_1.append(4)
            fork_2.append(4)
            fork_3.append(4)
            fork_4.append(4)
        if(game_board[6] == ' '):
            fork_1.append(6)
        if(game_board[8] == ' '):
            fork_4.append(8)
        if((game_board[4] == ' ' or game_board[6] == ' ') and (game_board[0] == 'X' and game_board[3] == 'X' and game_board[5] == 'X')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[4] == ' ') and (game_board[1] == 'X' and game_board[2] == 'X' and game_board[7] == 'X')):
            return random.choice(fork_2)
        elif((game_board[2] == ' ' or game_board[4] == ' ') and (game_board[3] == 'X' and game_board[5] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_3)
        elif((game_board[4] == ' ' or game_board[8] == ' ') and (game_board[1] == 'X' and game_board[6] == 'X' and game_board[7] == 'X')):
            return random.choice(fork_4)
        else:
            return -1

    # Fork G
    def fork_g(self, game_board):
        fork_1 = [] # 4, 6
        fork_2 = [] # 0, 4
        fork_3 = [] # 2, 4
        fork_4 = [] # 4, 8

        if(game_board[0] == ' '):
            fork_2.append(0)
        if(game_board[2] == ' '):
            fork_3.append(2)
        if(game_board[4] == ' '):
            fork_1.append(4)
            fork_2.append(4)
            fork_3.append(4)
            fork_4.append(4)
        if(game_board[6] == ' '):
            fork_1.append(6)
        if(game_board[8] == ' '):
            fork_4.append(8)
        if((game_board[4] == ' ' or game_board[6] == ' ') and (game_board[0] == 'X' and game_board[3] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[4] == ' ') and (game_board[1] == 'X' and game_board[2] == 'X' and game_board[6] == 'X')):
            return random.choice(fork_2)
        elif((game_board[2] == ' ' or game_board[4] == ' ') and (game_board[0] == 'X' and game_board[5] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_3)
        elif((game_board[4] == ' ' or game_board[8] == ' ') and (game_board[2] == 'X' and game_board[6] == 'X' and game_board[7] == 'X')):
            return random.choice(fork_4)
        else:
            return -1

    # Fork H
    def fork_h(self, game_board):
        fork_1 = [] # 1, 6
        fork_2 = [] # 0, 5
        fork_3 = [] # 2, 7
        fork_4 = [] # 3, 8

        if(game_board[0] == ' '):
            fork_2.append(0)
        if(game_board[1] == ' '):
            fork_1.append(1)
        if(game_board[2] == ' '):
            fork_3.append(2)
        if(game_board[3] == ' '):
            fork_4.append(3)
        if(game_board[5] == ' '):
            fork_2.append(5)
        if(game_board[6] == ' '):
            fork_1.append(6)
        if(game_board[7] == ' '):
            fork_3.append(7)
        if(game_board[8] == ' '):
            fork_4.append(8)
        if((game_board[1] == ' ' or game_board[6] == ' ') and (game_board[0] == 'X' and game_board[2] == 'X' and game_board[4] == 'X')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[5] == ' ') and (game_board[2] == 'X' and game_board[4] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_2)
        elif((game_board[2] == ' ' or game_board[7] == ' ') and (game_board[2] == 'X' and game_board[6] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_3)
        elif((game_board[3] == ' ' or game_board[8] == ' ') and (game_board[0] == 'X' and game_board[4] == 'X' and game_board[6] == 'X')):
            return random.choice(fork_4)
        else:
            return -1

    # Fork I
    def fork_i(self, game_board):
        fork_1 = [] # 0, 7
        fork_2 = [] # 2, 3
        fork_3 = [] # 1, 8
        fork_4 = [] # 5, 6

        if(game_board[0] == ' '):
            fork_1.append(0)
        if(game_board[1] == ' '):
            fork_3.append(1)
        if(game_board[2] == ' '):
            fork_2.append(2)
        if(game_board[3] == ' '):
            fork_2.append(3)
        if(game_board[5] == ' '):
            fork_4.append(5)
        if(game_board[6] == ' '):
            fork_4.append(6)
        if(game_board[7] == ' '):
            fork_1.append(7)
        if(game_board[8] == ' '):
            fork_3.append(8)
        if((game_board[0] == ' ' or game_board[7] == ' ') and (game_board[1] == 'X' and game_board[4] == 'X' and game_board[8] == 'X')):
            return random.choice(fork_1)
        elif((game_board[2] == ' ' or game_board[3] == ' ') and (game_board[4] == 'X' and game_board[5] == 'X' and game_board[6] == 'X')):
            return random.choice(fork_2)
        elif((game_board[1] == ' ' or game_board[8] == ' ') and (game_board[0] == 'X' and game_board[4] == 'X' and game_board[7] == 'X')):
            return random.choice(fork_3)
        elif((game_board[5] == ' ' or game_board[6] == ' ') and (game_board[2] == 'X' and game_board[3] == 'X' and game_board[4] == 'X')):
            return random.choice(fork_4)
        else:
            return -1
    





    # Block Fork: Cause a scenario where the player has two ways to win
    # Block Fork A
    def block_fork_a(self, game_board):
        fork_1 = [] # 1, 4, 5
        fork_2 = [] # 4, 5, 7
        fork_3 = [] # 3, 4, 7
        fork_4 = [] # 1, 3, 4

        if(game_board[1] == ' '):
            fork_1.append(1)
            fork_4.append(1)
        if(game_board[3] == ' '):
            fork_3.append(3)
            fork_4.append(3)
        if(game_board[4] == ' '):
            fork_1.append(4)
            fork_2.append(4)
            fork_3.append(4)
            fork_4.append(4)
        if(game_board[5] == ' '):
            fork_1.append(5)
            fork_2.append(5)
        if(game_board[7] == ' '):
            fork_2.append(7)
            fork_3.append(7)
        if((game_board[1] == ' ' or game_board[4] == ' ' or game_board[5] == ' ') and (game_board[0] == 'O' and game_board[2] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_1)
        elif((game_board[4] == ' ' or game_board[5] == ' ' or game_board[7] == ' ') and (game_board[2] == 'O' and game_board[6] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_2)
        elif((game_board[3] == ' ' or game_board[4] == ' ' or game_board[7] == ' ') and (game_board[0] == 'O' and game_board[6] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_3)
        elif((game_board[1] == ' ' or game_board[3] == ' ' or game_board[4] == ' ') and (game_board[0] == 'O' and game_board[2] == 'O' and game_board[6] == 'O')):
            return random.choice(fork_4)
        else:
            return -1

    # Block Fork B
    def block_fork_b(self, game_board):
        fork_1 = [] # 2, 6
        fork_2 = [] # 0, 8

        if(game_board[0] == ' '):
            fork_2.append(0)
        if(game_board[2] == ' '):
            fork_1.append(2)
        if(game_board[6] == ' '):
            fork_1.append(6)
        if(game_board[8] == ' '):
            fork_2.append(8)
        if((game_board[2] == ' ' or game_board[6] == ' ') and (game_board[0] == 'O' and game_board[1] == 'O' and game_board[3] == 'O')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[8] == ' ') and (game_board[1] == 'O' and game_board[2] == 'O' and game_board[5] == 'O')):
            return random.choice(fork_2)
        elif((game_board[2] == ' ' or game_board[6] == ' ') and (game_board[5] == 'O' and game_board[7] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[8] == ' ') and (game_board[3] == 'O' and game_board[6] == 'O' and game_board[7] == 'O')):
            return random.choice(fork_2)
        else:
            return -1
    
    # Block Fork C
    def block_fork_c(self, game_board):
        fork_1 = [] # 5, 7
        fork_2 = [] # 3, 7
        fork_3 = [] # 1, 3
        fork_4 = [] # 1, 5

        if(game_board[1] == ' '):
            fork_3.append(1)
            fork_4.append(1)
        if(game_board[3] == ' '):
            fork_2.append(3)
            fork_3.append(3)
        if(game_board[5] == ' '):
            fork_1.append(5)
            fork_4.append(5)
        if(game_board[7] == ' '):
            fork_1.append(7)
            fork_2.append(7)
        if((game_board[5] == ' ' or game_board[7] == ' ') and (game_board[1] == 'O' and game_board[3] == 'O' and game_board[4] == 'O')):
            return random.choice(fork_1)
        elif((game_board[3] == ' ' or game_board[7] == ' ') and (game_board[1] == 'O' and game_board[4] == 'O' and game_board[5] == 'O')):
            return random.choice(fork_2)
        elif((game_board[1] == ' ' or game_board[3] == ' ') and (game_board[4] == 'O' and game_board[5] == 'O' and game_board[7] == 'O')):
            return random.choice(fork_3)
        elif((game_board[1] == ' ' or game_board[5] == ' ') and (game_board[3] == 'O' and game_board[4] == 'O' and game_board[7] == 'O')):
            return random.choice(fork_4)
        else:
            return -1

    # Block Fork D
    def block_fork_D(self, game_board):
        fork_1 = [] # 5, 6, 8
        fork_2 = [] # 0, 7, 8
        fork_3 = [] # 0, 2, 3
        fork_4 = [] # 1, 2, 8

        if(game_board[0] == ' '):
            fork_2.append(0)
            fork_3.append(0)
        if(game_board[1] == ' '):
            fork_4.append(1)
        if(game_board[2] == ' '):
            fork_3.append(2)
            fork_4.append(2)
        if(game_board[3] == ' '):
            fork_3.append(3)
        if(game_board[5] == ' '):
            fork_1.append(5)
        if(game_board[6] == ' '):
            fork_1.append(6)
        if(game_board[7] == ' '):
            fork_2.append(7)
        if(game_board[8] == ' '):
            fork_1.append(8)
            fork_2.append(8)
            fork_4.append(8)
        if((game_board[5] == ' ' or game_board[6] == ' ' or game_board[8] == ' ') and (game_board[0] == 'O' and game_board[3] == '0' and game_board[4] == 'O')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[7] == ' ' or game_board[8] == ' ') and (game_board[1] == 'O' and game_board[2] == 'O' and game_board[4] == 'O')):
            return random.choice(fork_2)
        elif((game_board[0] == ' ' or game_board[2] == ' ' or game_board[3] == ' ') and (game_board[4] == 'O' and game_board[5] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_3)
        elif((game_board[1] == ' ' or game_board[2] == ' ' or game_board[8] == ' ') and (game_board[4] == 'O' and game_board[6] == 'O' and game_board[7] == 'O')):
            return random.choice(fork_4)
        else:
            return -1

    # Fork E
    def fork_e(self, game_board):
        fork_1 = [] # 1, 6
        fork_2 = [] # 0, 5
        fork_3 = [] # 2, 7
        fork_4 = [] # 3, 8

        if(game_board[0] == ' '):
            fork_2.append(0)
        if(game_board[1] == ' '):
            fork_1.append(1)
        if(game_board[2] == ' '):
            fork_3.append(2)
        if(game_board[3] == ' '):
            fork_4.append(3)
        if(game_board[5] == ' '):
            fork_2.append(5)
        if(game_board[6] == ' '):
            fork_1.append(6)
        if(game_board[7] == ' '):
            fork_3.append(7)
        if(game_board[8] == ' '):
            fork_4.append(8)
        if((game_board[1] == ' ' or game_board[6] == ' ') and (game_board[0] == 'O' and game_board[2] == 'O' and game_board[3] == 'O')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[5] == ' ') and (game_board[1] == 'O' and game_board[2] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_2)
        elif((game_board[2] == ' ' or game_board[7] == ' ') and (game_board[5] == 'O' and game_board[6] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_3)
        elif((game_board[3] == ' ' or game_board[8] == ' ') and (game_board[0] == 'O' and game_board[6] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_4)
        else:
            return -1
    
    # Fork F
    def fork_f(self, game_board):
        fork_1 = [] # 4, 6
        fork_2 = [] # 0, 4
        fork_3 = [] # 2, 4
        fork_4 = [] # 4, 8

        if(game_board[0] == ' '):
            fork_2.append(0)
        if(game_board[2] == ' '):
            fork_3.append(2)
        if(game_board[4] == ' '):
            fork_1.append(4)
            fork_2.append(4)
            fork_3.append(4)
            fork_4.append(4)
        if(game_board[6] == ' '):
            fork_1.append(6)
        if(game_board[8] == ' '):
            fork_4.append(8)
        if((game_board[4] == ' ' or game_board[6] == ' ') and (game_board[0] == 'O' and game_board[3] == 'O' and game_board[5] == 'O')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[4] == ' ') and (game_board[1] == 'O' and game_board[2] == 'O' and game_board[7] == 'O')):
            return random.choice(fork_2)
        elif((game_board[2] == ' ' or game_board[4] == ' ') and (game_board[3] == 'O' and game_board[5] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_3)
        elif((game_board[4] == ' ' or game_board[8] == ' ') and (game_board[1] == 'O' and game_board[6] == 'O' and game_board[7] == 'O')):
            return random.choice(fork_4)
        else:
            return -1

    # Fork G
    def fork_g(self, game_board):
        fork_1 = [] # 4, 6
        fork_2 = [] # 0, 4
        fork_3 = [] # 2, 4
        fork_4 = [] # 4, 8

        if(game_board[0] == ' '):
            fork_2.append(0)
        if(game_board[2] == ' '):
            fork_3.append(2)
        if(game_board[4] == ' '):
            fork_1.append(4)
            fork_2.append(4)
            fork_3.append(4)
            fork_4.append(4)
        if(game_board[6] == ' '):
            fork_1.append(6)
        if(game_board[8] == ' '):
            fork_4.append(8)
        if((game_board[4] == ' ' or game_board[6] == ' ') and (game_board[0] == 'O' and game_board[3] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[4] == ' ') and (game_board[1] == 'O' and game_board[2] == 'O' and game_board[6] == 'O')):
            return random.choice(fork_2)
        elif((game_board[2] == ' ' or game_board[4] == ' ') and (game_board[0] == 'O' and game_board[5] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_3)
        elif((game_board[4] == ' ' or game_board[8] == ' ') and (game_board[2] == 'O' and game_board[6] == 'O' and game_board[7] == 'O')):
            return random.choice(fork_4)
        else:
            return -1

    # Fork H
    def fork_h(self, game_board):
        fork_1 = [] # 1, 6
        fork_2 = [] # 0, 5
        fork_3 = [] # 2, 7
        fork_4 = [] # 3, 8

        if(game_board[0] == ' '):
            fork_2.append(0)
        if(game_board[1] == ' '):
            fork_1.append(1)
        if(game_board[2] == ' '):
            fork_3.append(2)
        if(game_board[3] == ' '):
            fork_4.append(3)
        if(game_board[5] == ' '):
            fork_2.append(5)
        if(game_board[6] == ' '):
            fork_1.append(6)
        if(game_board[7] == ' '):
            fork_3.append(7)
        if(game_board[8] == ' '):
            fork_4.append(8)
        if((game_board[1] == ' ' or game_board[6] == ' ') and (game_board[0] == 'O' and game_board[2] == 'X' and game_board[4] == 'X')):
            return random.choice(fork_1)
        elif((game_board[0] == ' ' or game_board[5] == ' ') and (game_board[2] == 'O' and game_board[4] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_2)
        elif((game_board[2] == ' ' or game_board[7] == ' ') and (game_board[2] == 'O' and game_board[6] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_3)
        elif((game_board[3] == ' ' or game_board[8] == ' ') and (game_board[0] == 'O' and game_board[4] == 'O' and game_board[6] == 'O')):
            return random.choice(fork_4)
        else:
            return -1

    # Fork I
    def fork_i(self, game_board):
        fork_1 = [] # 0, 7
        fork_2 = [] # 2, 3
        fork_3 = [] # 1, 8
        fork_4 = [] # 5, 6

        if(game_board[0] == ' '):
            fork_1.append(0)
        if(game_board[1] == ' '):
            fork_3.append(1)
        if(game_board[2] == ' '):
            fork_2.append(2)
        if(game_board[3] == ' '):
            fork_2.append(3)
        if(game_board[5] == ' '):
            fork_4.append(5)
        if(game_board[6] == ' '):
            fork_4.append(6)
        if(game_board[7] == ' '):
            fork_1.append(7)
        if(game_board[8] == ' '):
            fork_3.append(8)
        if((game_board[0] == ' ' or game_board[7] == ' ') and (game_board[1] == 'O' and game_board[4] == 'O' and game_board[8] == 'O')):
            return random.choice(fork_1)
        elif((game_board[2] == ' ' or game_board[3] == ' ') and (game_board[4] == 'O' and game_board[5] == 'O' and game_board[6] == 'O')):
            return random.choice(fork_2)
        elif((game_board[1] == ' ' or game_board[8] == ' ') and (game_board[0] == 'O' and game_board[4] == 'O' and game_board[7] == 'O')):
            return random.choice(fork_3)
        elif((game_board[5] == ' ' or game_board[6] == ' ') and (game_board[2] == 'O' and game_board[3] == 'O' and game_board[4] == 'O')):
            return random.choice(fork_4)
        else:
            return -1


    def human_move(self, game_board):
        game_board_object = game_board
        game_board = game_board.board_string()
        move = -1
        move = self.two_in_a_row(game_board)
        if move == -1 or game_board_object.is_move_valid(move, game_board_object) == False:
            move = self.center(game_board)
        if move == -1 or game_board_object.is_move_valid(move, game_board_object) == False:
            move = self.opposite_corner(game_board)
        if move == -1 or game_board_object.is_move_valid(move, game_board_object) == False:
            move = self.empty_corner(game_board)
        if move == -1 or game_board_object.is_move_valid(move, game_board_object) == False:
            move = self.empty_side(game_board)

        return move