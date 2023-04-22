import random
# import the function "random" to use later for the computer's outcomes

user_score = 0
computer_score = 0
play_count = 0
# set the scoreboard and play count


def play_game():
    computer_outcomes = ["rock", "paper", "scissors"]
    computer_hand = random.choice(computer_outcomes)
    # set the computer to randomly choose rock, paper, or scissors
    return [computer_hand]


def show_result(user_input, computer_input):
    winner = None
    print("---------------------------------------------------------")
    print("Rock... Paper... Scissors, you chose " + str(user_input) + " and I chose " + str(computer_input) + "!")

    if user_input == "rock" and computer_input == "scissors":
        print("You win! You get a point!")
        winner = 1

    elif user_input == "rock" and computer_input == "paper":
        print("You lose! That's a point for me!")
        winner = 0

    elif user_input == "paper" and computer_input == "rock":
        print("You win! You get a point!")
        winner = 1

    elif user_input == "paper" and computer_input == "scissors":
        print("You lose! That's a point for me!")
        winner = 0

    elif user_input == "scissors" and computer_input == "paper":
        print("You win! You get a point!")
        winner = 1

    elif user_input == "scissors" and computer_input == "rock":
        print("You lose! That's a point for me!")
        winner = 0

    elif user_input == computer_input:
        print("You and I both chose " + user_input)
        print("That's a tie! No points are given!")
        winner = 2

    return winner
# the user score and computer score will change accordingly to the value returned.


print("Hello and welcome to Rock, Paper, Scissors!")
user_name = input("Please enter your username: (example: Khanh) ").upper()
play_count_request = int(input("How many times would you like to play? "))
# receive the user's requested play count
while play_count < play_count_request:
    user_hand = input("please choose: (rock/paper/scissors) ").lower()
    if user_hand == "rock" or user_hand == "paper" or user_hand == "scissors":
        computer_hand_check = play_game()
        winner_check = show_result(user_hand, computer_hand_check)
        if winner_check == 1:
            user_score += 1
        if winner_check == 0:
            computer_score += 1
        if winner_check == 2:
            user_score = user_score
            computer_score = computer_score
        # increment either the user's score or the computer's score, updating the scoreboard
        print("------------------CURRENT SCOREBOARD---------------------")
        print(user_name + ":" + str(user_score))
        print("MOUNTAIN DEW-BOT: " + str(computer_score))
        print("---------------------------------------------------------")
        play_count += 1
        # increment the play count by 1

        if play_count == play_count_request:
            # check to see if the play count has reached the requested play count.
            # Display the final scoreboard and end the game if it does.
            print("---------------------------------------------------------")
            print("You have reached the requested turns! ")
            print("--------------------FINAL SCOREBOARD---------------------")
            print(user_name + ":" + str(user_score))
            print("MOUNTAIN DEW-BOT: " + str(computer_score))
            print("Thank you for playing Rock, Paper, Scissors!")
            break
    else:
        print("please choose only rock, paper, or scissors")
