from game_board import Game_Board
from menace import Menace
from human import Human

if __name__ == '__main__':
    #Intialize objects of game board, menace and human
    game_board = Game_Board()
    menace = Menace()
    human = Human()

def gameplay(self):
    game_board.display_board()
    
    #Take move input from human
    move = human.human_move()

    #Validate if move is valid, i.e. between 0 and 8
    if(move>=0 and move<9):
        game_board.make_move_on_board(move, "X")
    