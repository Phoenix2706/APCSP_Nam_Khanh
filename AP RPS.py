import random
# import the function "random" to use later when deciding computer's hand

user_score = 0
computer_score = 0
play_count = 0
# set the scoreboard and play count


def play_game():
    user_hand = input("please choose: (rock/paper/scissors) ").lower()
    # receives input as user's hand
    outcomes = ["rock", "paper", "scissors"]
    computer_hand = random.choice(outcomes)

    # set the computer to randomly choose rock, paper, or scissors
    return [user_hand, computer_hand]


def show_result(user_input, computer_input):
    winner = None
    print("---------------------------------------------------------")
    print("Rock... Paper... Scissors, you chose " + user_input + " and I chose " + computer_input + "!")

    if user_input == "rock" and computer_input == "scissors":
        print("You win! You get a point!")
        winner = 1

    elif user_input == "rock" and computer_input == "paper":
        print("You lose! I get a point!")
        winner = 0

    elif user_input == "paper" and computer_input == "rock":
        print("You win! You get a point!")
        winner = 1

    elif user_input == "paper" and computer_input == "scissors":
        print("You lose! I get a point!")
        winner = 0

    elif user_input == "scissors" and computer_input == "paper":
        print("You win! You get a point!")
        winner = 1

    elif user_input == "scissors" and computer_input == "rock":
        print("You lose! I get a point!")
        winner = 0

    elif user_input == computer_input:
        print("You and I both chose " + user_input)
        print("That's a tie! No points are given!")
        winner = 2

    return winner
# return the value "winner" to increment either the user's score or the computer's score.


print("Hello and welcome to Rock, Paper, Scissors!")
user_name = input("Please enter your username: (example: Khanh) ").upper()
play_count_request = int(input("How many times would you like to play? "))
# receive the user's requested play count
while play_count < play_count_request:
    user_hand_check, computer_hand_check = play_game()
    winner_check = show_result(user_hand_check, computer_hand_check)
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
        print("Your turns have ran out! ")
        print("--------------------FINAL SCOREBOARD---------------------")
        print(user_name + ":" + str(user_score))
        print("MOUNTAIN DEW-BOT: " + str(computer_score))
        print("Thank you for playing Rock, Paper, Scissors!")
        break
