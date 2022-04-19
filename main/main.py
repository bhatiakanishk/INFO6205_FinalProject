from game_board import Game_Board
from menace import Menace
from human import Human

#This method uses human optimal strategy for opponent
def training():
    game_board.display_board()
    
    while True:
        #Determine move of menace based on training
        menace_move = menace.move_to_make(game_board)
        #Validate if move is valid, i.e. between 0 and 8 and cell is empty
        if(menace_move>=0 and menace_move<9):
            game_board.make_move_on_board(menace_move, "X")
            game_board.display_board()

            if game_board.win_condition():
                menace.win_result()
                human.lose_result()
                break
                
            if game_board.draw_condition():
                menace.draw_result()
                break


        #Take move input from human
        human_move = human.human_move()
        #Validate if move is valid, i.e. between 0 and 8 and cell is empty
        if(human_move>=0 and human_move<9):
            game_board.make_move_on_board(human_move, "O")
            game_board.display_board()

            if game_board.win_condition():
                human.win_result()
                menace.lose_result()
                break

            if game_board.draw_condition():
                menace.draw_result()
                break

#This method takes human input for gameplay. To be used after training
def gameplay():
    
    
    while True:
        #Determine move of menace based on training
        menace_move = menace.move_to_make(game_board)
        print(menace_move)
        #Validate if move is valid, i.e. between 0 and 8 and cell is empty
        if(menace_move>=0 and menace_move<9):
            game_board.make_move_on_board(menace_move, "X")
            game_board.display_board()

            if game_board.win_condition():
                menace.win_result()
                human.lose_result()
                break
                
            if game_board.draw_condition():
                menace.draw_result()
                break
        else:
            print("Menace move invalid")


        #Take move input from human
        #human_move = human.human_move()
        human_move = input("Make a move on the board:")
        human_move = int(human_move)
        #Validate if move is valid, i.e. between 0 and 8 and cell is empty
        if(human_move>=0 and human_move<9):
            game_board.make_move_on_board(human_move, "O")
            game_board.display_board()

            if game_board.win_condition():
                human.win_result()
                menace.lose_result()
                break

            if game_board.draw_condition():
                menace.draw_result()
                break

if __name__ == '__main__':
    #Intialize objects of game board, menace and human
    menace = Menace()
    human = Human()
    game_board = Game_Board()
    game_board.display_board()

    print("Training now:")
    for i in range(10):
        training()

    print("Training complete")    
    
    print("Gameplay now:")
    gameplay()
    print("Gameplay complete")