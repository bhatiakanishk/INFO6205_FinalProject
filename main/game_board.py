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