class Game_Board:
    def initialize_board(self):
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
        pass

    def lose_condition(self):
        #Needed? If not win and not draw, then lose?!
        pass
