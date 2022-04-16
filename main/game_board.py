class Game_Board:
    def __init__(self):
        #To declare empty game board
        self.game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
    
    def display_board(self):
        #To display board on the terminal
        print("-------")
        print("|"  + self.game_board[0] + "|"  + self.game_board[1] + "|" + self.game_board[2] + "|")
        print("-------")
        print("|"  + self.game_board[3] + "|"  + self.game_board[4] + "|" + self.game_board[5] + "|")
        print("-------")
        print("|"  + self.game_board[6] + "|"  + self.game_board[7] + "|" + self.game_board[8] + "|")
        print("-------")

    def win_condition(self):
        win_condition = False
        if(self.game_board[0]!=' ' and self.game_board[0] == self.game_board[1] == self.game_board[2]):
            win_condition = True
        elif(self.game_board[0]!=' ' and self.game_board[0] == self.game_board[3] == self.game_board[6]):
            win_condition = True
        elif(self.game_board[0]!=' ' and self.game_board[0] == self.game_board[4] == self.game_board[8]):
            win_condition = True
        elif(self.game_board[4]!=' ' and self.game_board[1] == self.game_board[4] == self.game_board[7]):
            win_condition = True
        elif(self.game_board[4]!=' ' and self.game_board[3] == self.game_board[4] == self.game_board[5]):
            win_condition = True
        elif(self.game_board[4]!=' ' and self.game_board[2] == self.game_board[4] == self.game_board[6]):
            win_condition = True
        elif(self.game_board[8]!=' ' and self.game_board[2] == self.game_board[5] == self.game_board[8]):
            win_condition = True
        elif(self.game_board[8]!=' ' and self.game_board[6] == self.game_board[7] == self.game_board[8]):
            win_condition = True
        return win_condition

    def draw_condition(self):
        #To check for empty cells on the board
        empty_cell = 0
        for cell in self.game_board:
            if cell == ' ':
                #Increment counter if there are empty cells
                empty_cell = empty_cell + 1
        #If there are no empty cells, game is drawn
        if empty_cell == 0:
            return True 
        return False


    def lose_condition(self):
        #Needed? If not win and not draw, then lose?!
        pass
