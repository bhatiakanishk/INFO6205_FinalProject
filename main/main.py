from asyncore import write
from concurrent.futures import ThreadPoolExecutor
from game_board import Game_Board
from menace import Menace
from human import Human
import datetime
import json

number_of_plays = 0
number_of_wins = 0
number_of_draws = 0
number_of_loses = 0
training_log_file = open('logs/training_log.txt', 'a')
gameplay_log_file = open('logs/gameplay_log.txt', 'w')

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
        
        # print("Move Made By Menace:")
        # print(str(menace_move))
        #game_board_training.display_board()

        if game_board_training.win_condition():
            menace.win_result()
            number_of_wins += 1
            human.lose_result()

            result = "Menace Win"
            current_time = datetime.datetime.now()
            write_training_logs(current_time, result)
            menace.reset_moves_played()
            write_game_states(menace)

            break
            
        if game_board_training.draw_condition():
            menace.draw_result()
            number_of_draws += 1

            result = "Menace Draw"
            current_time = datetime.datetime.now()
            write_training_logs(current_time, result)
            menace.reset_moves_played()
            write_game_states(menace)
            break


        #Determine move according to human optimal strategy
        human_move = human.human_move(game_board_training)

        #Validate if move is valid, i.e. between 0 and 8 and cell is empty
        if game_board_training.is_move_valid(human_move, game_board_training):
            game_board_training.make_move_on_board(human_move, "O")
            #game_board_training.display_board()

            if game_board_training.win_condition():
                human.win_result()
                print("Calling lose")
                menace.lose_result()
                number_of_loses += 1

                result = "Menace Lose"
                current_time = datetime.datetime.now()
                write_training_logs(current_time, result)
                menace.reset_moves_played()
                write_game_states(menace)
                break

            if game_board_training.draw_condition():
                menace.draw_result()
                number_of_draws += 1

                result = "Menace Draw"
                current_time = datetime.datetime.now()
                write_training_logs(current_time, result)
                menace.reset_moves_played()
                write_game_states(menace)
                break
        else:
            print("Invalid move.")
            menace.win_result()
            human.lose_result
            number_of_wins += 1

            result = "Menace Win"
            current_time = datetime.datetime.now()
            write_training_logs(current_time, result)
            menace.reset_moves_played()
            write_game_states(menace)
            break

#This method trains two menaces against each other
def two_menace_training():
    game_states = load_game_states()
    menace_one.set_game_states(game_states)
    menace_two.set_game_states(game_states)

    game_board_training = Game_Board()
    global number_of_plays
    global number_of_wins
    global number_of_draws
    global number_of_loses
    number_of_plays += 1
    #game_board_training.display_board()

    while True:
        #Determine move of menace based on training
        menace_move = menace_one.move_to_make(game_board_training)
        game_board_training.make_move_on_board(menace_move, "X")
        
        # print("Move Made By Menace:")
        # print(str(menace_move))
        #game_board_training.display_board()

        if game_board_training.win_condition():
            menace_one.win_result()
            number_of_wins += 1
            menace_two.lose_result()

            result = "Menace Win"
            current_time = datetime.datetime.now()
            write_training_logs(current_time, result)
            menace_one.reset_moves_played()
            menace_two.reset_moves_played()
            write_game_states(menace_one)
            write_game_states(menace_two)
            break
            
        if game_board_training.draw_condition():
            menace_one.draw_result()
            menace_two.draw_result()
            number_of_draws += 1

            result = "Menace Draw"
            current_time = datetime.datetime.now()
            write_training_logs(current_time, result)
            menace_one.reset_moves_played()
            menace_two.reset_moves_played()
            write_game_states(menace_one)
            write_game_states(menace_two)
            break


        #Take move from menace
        menace_two_move = menace_two.move_to_make(game_board_training)

        #Validate if move is valid, i.e. between 0 and 8 and cell is empty
        if game_board_training.is_move_valid(menace_two_move, game_board_training):
            game_board_training.make_move_on_board(menace_two_move, "O")
            #game_board_training.display_board()

            if game_board_training.win_condition():
                menace_two.win_result()
                print("Calling lose")
                menace_one.lose_result()
                number_of_loses += 1

                result = "Menace Lose"
                current_time = datetime.datetime.now()
                write_training_logs(current_time, result)
                menace_one.reset_moves_played()
                menace_two.reset_moves_played()
                write_game_states(menace_one)
                write_game_states(menace_two)
                break

            if game_board_training.draw_condition():
                menace_one.draw_result()
                menace_two.draw_result()
                number_of_draws += 1

                result = "Menace Draw"
                current_time = datetime.datetime.now()
                write_training_logs(current_time, result)
                menace_one.reset_moves_played()
                menace_two.reset_moves_played()
                write_game_states(menace_one)
                write_game_states(menace_two)
                break
        else:
            print("Invalid move.")
            menace_one.win_result()
            menace_two.lose_result
            number_of_wins += 1

            result = "Menace Win"
            current_time = datetime.datetime.now()
            write_training_logs(current_time, result)
            menace_one.reset_moves_played()
            menace_two.reset_moves_played()
            write_game_states(menace_one)
            write_game_states(menace_two)
            break

#This method takes human input for gameplay. To be used after training
def gameplay():
    game_states = load_game_states()
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
            menace.reset_moves_played()
            break
            
        if game_board_gameplay.draw_condition():
            menace.draw_result()
            menace.reset_moves_played()
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
                menace.reset_moves_played()
                break

            if game_board_gameplay.draw_condition():
                menace.draw_result()
                break
        else:
            print("Invalid move.")
            menace.win_result()
            human.lose_result
            menace.reset_moves_played()
            break

    
    gameplay_log_file.write("Time: " + str(current_time) + " | Game Ends \n")
    gameplay_log_file.write("-------------------------------------------------------" + "\n")

#Load the game states for gameplay
def load_game_states():
    with open("logs/game_states_log.json", "r") as game_states_file:
        game_states = json.load(game_states_file)
    game_states_file.close()
    return game_states

#Write the game states to the JSON file
def write_game_states(menace_object):
    with open("logs/game_states_log.json", "w") as game_states_file:
        json.dump(menace_object.get_game_states(), game_states_file)

#Write training logs to training_log.txt
def write_training_logs(current_time, result):
    training_log_file = open('logs/training_log.txt', 'a')
    training_log_file.write("Time: " + str(current_time) + " | Result: " + str(result) + "\n")

#Write training results to results_logs.txt
def write_result_logs():
    win_percentage = (100*number_of_wins)/number_of_plays
    lose_percentage = (100*number_of_loses)/number_of_plays
    draw_percentage = (100*number_of_draws)/number_of_plays

    log_file = open('logs/results_log.txt', 'a')
    log_file.write("Number of games: " + str(number_of_plays) + "\n")
    log_file.write("Number of wins: " + str(number_of_wins) + "\n")
    log_file.write("Number of draws: " + str(number_of_draws) + "\n")
    log_file.write("Number of loses: " + str(number_of_loses) + "\n")
    log_file.write("Win Percentage: " + str(win_percentage) + "\n")
    log_file.write("Lost Percentage: " + str(lose_percentage) + "\n")
    log_file.write("Draw Percentage: " + str(draw_percentage) + "\n")
    log_file.write("-------------------------------------------------------" + "\n")

#Call the training() method
def call_menace_human_training(menace, human, menace_human_training_iterations):
    print("Training between Menace and Human Optimal Strategy Begins:")
    #Multithreading implementation
    processes = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        for i in range(menace_human_training_iterations):
            processes.append(executor.submit(training()))
            game_states = load_game_states()
            menace.set_game_states(game_states)

    print("Training between Menace and Human Optimal Strategy Complete.")
    write_result_logs()

#Call the two_menace_training() method
def call_menace_menace_training(menace_menace_training_iterations):
    print("Training between Menace and Menace Begins:")
    #Multithreading implementation
    processes = []
    with ThreadPoolExecutor(max_workers=50) as executor:
        for i in range(menace_menace_training_iterations):
            processes.append(executor.submit(two_menace_training()))
            
    print("Training between Menace and Menace Complete.")
    write_result_logs()

#Call the gameplay() method
def call_user_gameplay():
    print("Gameplay now:")
    gameplay()
    write_game_states(menace)

#Main method
if __name__ == '__main__':
    #Initialize objects Menace and Human
    menace = Menace()
    human = Human()

    menace_one = Menace()
    menace_two = Menace()

    menace_human_training_iterations = 2000
    menace_menace_training_iterations = 10000
    
    while True:
        print("Press 1 to traning menace against human optimal strategy.")
        print("Press 2 to train menace against menace.")
        print("Press 3 to play against the menace")
        decision = input("Input Decision:")
        if decision == "1":
            call_menace_human_training(menace, human, menace_human_training_iterations)
        elif decision == "2":
            call_menace_menace_training(menace_menace_training_iterations)
        elif decision == "3":
            call_user_gameplay()
        else:
            break