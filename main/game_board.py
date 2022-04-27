class Game_Board:
    def __init__(self):
        #To declare empty game board
        self.game_board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ',]
    
    #Set the game board
    def set_game_board(self, game_board):
        self.game_board = game_board
    
    #Get the game board
    def get_game_board(self):
        return self.game_board

    def display_board(self):
        #To display board on the terminal
        print("------||------")
        print("|"  + self.game_board[0] + "|"  + self.game_board[1] + "|" + self.game_board[2] + "||" + "0" + "|" + "1" + "|" + "2" + "|")
        print("------||------")
        print("|"  + self.game_board[3] + "|"  + self.game_board[4] + "|" + self.game_board[5] + "||" + "3" + "|" + "4" + "|" + "5" + "|")
        print("------||------")
        print("|"  + self.game_board[6] + "|"  + self.game_board[7] + "|" + self.game_board[8] + "||" + "6" + "|" + "7" + "|" + "8" + "|")
        print("------||------")

    #Check for win condition on the board, i.e., three in a row
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

    #Check for draw condition on the board
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
        pass

    #Make the move on the board
    def make_move_on_board(self, position, symbol):
        self.game_board[position] = symbol

    #Check if the move is valid, i.e., check if the input is between 0 and 9 and if the cell is currently empty
    def is_move_valid(self, move, board):
        move = int(move)
        board = board.convert_board_to_string()
        if move>=0 and move<9 and board[move] == ' ':
            return True
        return False

    #To convert the board to string format
    def convert_board_to_string(self):
        return ''.join(self.game_board)
