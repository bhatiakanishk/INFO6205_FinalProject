from concurrent.futures import ThreadPoolExecutor
from time import gmtime
from game_board import Game_Board
from menace import Menace
from human import Human
import datetime
import json

number_of_plays = 0
number_of_wins = 0
number_of_draws = 0
number_of_loses = 0
training_log_file = open('training_log.txt', 'a')
gameplay_log_file = open('gameplay_log.txt', 'w')

def logging(current_time, result):
    training_log_file = open('training_log.txt', 'a')
    training_log_file.write("Time: " + str(current_time) + " | Result: " + str(result) + "\n")

#This method uses human optimal strategy for opponent
def training():
    game_board_training = Game_Board()
    global number_of_plays
    global number_of_wins
    global number_of_draws
    global number_of_loses
    number_of_plays += 1
    #game_board_training.display_board()

    while True:
        #Determine move of menace based on training
        menace_move = menace.move_to_make(game_board_training)
        game_board_training.make_move_on_board(menace_move, "X")
        
        #print("Move Made By Menace:")
        #game_board_training.display_board()

        if game_board_training.win_condition():
            menace.win_result()
            number_of_wins += 1
            human.lose_result()

            current_time = datetime.datetime.now()
            result = "Menace Win"
            logging(current_time, result)

            break
            
        if game_board_training.draw_condition():
            menace.draw_result()
            number_of_draws += 1

            current_time = datetime.datetime.now()
            result = "Menace Draw"
            logging(current_time, result)
            
            break


        #Take move input from human
        human_move = human.human_move(game_board_training)
        #print("Human strategy tries to make:")
        #print(human_move)

        #Validate if move is valid, i.e. between 0 and 8 and cell is empty
        if game_board_training.is_move_valid(human_move, game_board_training):
            game_board_training.make_move_on_board(human_move, "O")
            #game_board_training.display_board()

            if game_board_training.win_condition():
                human.win_result()
                menace.lose_result()
                number_of_loses += 1

                current_time = datetime.datetime.now()
                result = "Menace Lose"
                logging(current_time, result)

                break

            if game_board_training.draw_condition():
                menace.draw_result()
                number_of_draws += 1

                current_time = datetime.datetime.now()
                result = "Menace Draw"
                logging(current_time, result)

                break
        else:
            print("Invalid move.")
            menace.win_result()
            human.lose_result
            number_of_wins += 1

            current_time = datetime.datetime.now()
            result = "Menace Win"
            logging(current_time, result)

            break

#This method takes human input for gameplay. To be used after training
def gameplay():

    with open("game_states_log.json", "r") as game_states_file:
        game_states = json.load(game_states_file)
    game_states_file.close()
    menace.set_game_states(game_states)

    game_board_gameplay = Game_Board()
    game_board_gameplay.display_board()

    current_time = datetime.datetime.now()
    gameplay_log_file.write("Time: " + str(current_time) + " | Game Starts \n")

    while True:
        #Determine move of menace based on training
        menace_move = menace.move_to_make(game_board_gameplay)
        game_board_gameplay.make_move_on_board(menace_move, "X")

        current_time = datetime.datetime.now()
        gameplay_log_file.write("Time: " + str(current_time) + " | Move made by menace: " + str(menace_move) + "\n")

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

            current_time = datetime.datetime.now()
            gameplay_log_file.write("Time: " + str(current_time) + " | Move made by human: " + str(menace_move) + "\n")

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

    
    gameplay_log_file.write("Time: " + str(current_time) + " | Game Ends \n")
    gameplay_log_file.write("-------------------------------------------------------" + "\n")

if __name__ == '__main__':
    #Intialize objects of game board, menace and human
    menace = Menace()
    human = Human()

    print("Training now:")
    
    #Multithreading implementation
    processes = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(1000):
            processes.append(executor.submit(training()))
    print("Training complete")

    print("Number of games: " + str(number_of_plays))
    print("Number of wins: " + str(number_of_wins))
    print("Number of draws: " + str(number_of_draws))
    print("Number of loses: " + str(number_of_loses))

    win_percentage = (100*number_of_wins)/number_of_plays
    lose_percentage = (100*number_of_loses)/number_of_plays
    draw_percentage = (100*number_of_draws)/number_of_plays
    print("Win Percentage: " + str(win_percentage))
    print("Lose Percentage: " + str(lose_percentage))
    print("Draw Percentage: " + str(draw_percentage))
    print("-------------------------------------------------") 

    log_file = open('training_log.txt', 'a')
    log_file.write("Number of games: " + str(number_of_plays) + "\n")
    log_file.write("Number of wins: " + str(number_of_wins) + "\n")
    log_file.write("Number of draws: " + str(number_of_draws) + "\n")
    log_file.write("Number of loses: " + str(number_of_loses) + "\n")
    log_file.write("Win Percentage: " + str(win_percentage) + "\n")
    log_file.write("Lost Percentage: " + str(lose_percentage) + "\n")
    log_file.write("Draw Percentage: " + str(draw_percentage) + "\n")
    log_file.write("-------------------------------------------------------" + "\n")

    with open("game_states_log.json", "w") as game_states_file:
        json.dump(menace.get_game_states(), game_states_file)

    
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