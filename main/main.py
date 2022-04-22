from concurrent.futures import ThreadPoolExecutor
from game_board import Game_Board
from menace import Menace
from human import Human

#This method uses human optimal strategy for opponent
def training():
    game_board_training = Game_Board()
    #game_board_training.display_board()

    while True:
        #Determine move of menace based on training
        menace_move = menace.move_to_make(game_board_training)
        game_board_training.make_move_on_board(menace_move, "X")
        
        #print("Move Made By Menace:")
        #game_board_training.display_board()

        if game_board_training.win_condition():
            menace.win_result()
            human.lose_result()
            break
            
        if game_board_training.draw_condition():
            menace.draw_result()
            break


        #Take move input from human
        human_move = human.human_move(game_board_training)
        #Validate if move is valid, i.e. between 0 and 8 and cell is empty
        if game_board_training.is_move_valid(human_move, game_board_training):
            game_board_training.make_move_on_board(human_move, "O")
            #game_board_training.display_board()

            if game_board_training.win_condition():
                human.win_result()
                menace.lose_result()
                break

            if game_board_training.draw_condition():
                menace.draw_result()
                break
        else:
            print("Invalid move.")
            menace.win_result()
            human.lose_result
            break

#This method takes human input for gameplay. To be used after training
def gameplay():
    game_board_gameplay = Game_Board()
    game_board_gameplay.display_board()
    
    while True:
        #Determine move of menace based on training
        menace_move = menace.move_to_make(game_board_gameplay)
        game_board_gameplay.make_move_on_board(menace_move, "X")

        print("Move Made By Menace:")
        game_board_gameplay.display_board()

        if game_board_gameplay.win_condition():
            menace.win_result()
            human.lose_result()
            break
            
        if game_board_gameplay.draw_condition():
            menace.draw_result()
            break


        #Take move input from human
        human_move = input("Make a move on the board:")
        human_move = int(human_move)
        #Validate if move is valid, i.e. between 0 and 8 and cell is empty
        if game_board_gameplay.is_move_valid(human_move, game_board_gameplay):
            game_board_gameplay.make_move_on_board(human_move, "O")
            game_board_gameplay.display_board()

            if game_board_gameplay.win_condition():
                human.win_result()
                menace.lose_result()
                break

            if game_board_gameplay.draw_condition():
                menace.draw_result()
                break
        else:
            print("Invalid move.")
            menace.win_result()
            human.lose_result
            break

if __name__ == '__main__':
    #Intialize objects of game board, menace and human
    menace = Menace()
    human = Human()

    print("Training now:")
    
    #Multithreading implementation
    processes = []
    with ThreadPoolExecutor(max_workers=10) as executor:
        for i in range(300):
            processes.append(executor.submit(training()))
    print("Training complete")    

    print("-------------------------------------------------") 

    print("Gameplay now:")
    gameplay()
    print("Gameplay complete")
    while True:
        decision = input("Play again? Press y to play again and any other key to cancel:")
        if decision == 'y':
            gameplay()
            print("Gameplay complete")
        else:
            break