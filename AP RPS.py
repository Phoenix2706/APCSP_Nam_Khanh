# lines 13 to 20 were inspired by lines 5 to 8 in sample H of the sample responses of 2022,
# located at https://apcentral.collegeboard.org/courses/ap-computer-science-principles/exam

import random
# import the function "random" to determine computer's hand at random.

user_score = 0
computer_score = 0
play_count = 0
# set the scoreboard and play count at 0.


def play_game():
    user_hand = input("Choose your weapon: rock, paper, or scissors? ").lower()
    # receives input as user's hand
    outcomes = ["rock", "paper", "scissors"]
    # give the computer potential options to choose from.
    computer_hand = random.choice(outcomes)
    # chooses the value computer_hand at random.
    return [user_hand, computer_hand]


def show_result(user_input, computer_input):
    winner = None
    # set the winner variable as empty, it will be assigned a value later.
    print("---------------------------------------------------------")
    print("Rock... Paper... Scissors, you chose " + user_input + " and I chose " + computer_input + "!")
    # report the user's and computer's hands
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
    # determines the result and set a value to variable winner based on the rules of rock, paper, scissors.
    # if winner = 1, the user wins
    # if winner = 0, the computer wins
    # if winner = 2, it's a draw
    return winner
# returns winner as a global variable to use outside the function, determine which side the score should be given to.


print("Hello and welcome to Rock, Paper, Scissors!")
user_name = input("Please enter your username: (example: Khanh) ").upper()
print("Alright " + user_name + "! You will be facing off against the great MOUNTAIN DEW-BOT!")
play_count_request = int(input("How many times would you like to play? "))
# receives the user's requested play count.
while play_count < play_count_request:
    user_hand_check, computer_hand_check = play_game()
    # executes function play_game, returning the inputs as global values.
    winner_check = show_result(user_hand_check, computer_hand_check)
    # executes function show_result, receiving play_game's output as parameters, returning value winner.
    if winner_check == 1:
        user_score += 1
    if winner_check == 0:
        computer_score += 1
    if winner_check == 2:
        user_score = user_score
        computer_score = computer_score
    # increment either the user's score or the computer's score depending on the value of winner_check.
    print("------------------CURRENT SCOREBOARD---------------------")
    print(user_name + ":" + str(user_score))
    print("MOUNTAIN DEW-BOT: " + str(computer_score))
    print("---------------------------------------------------------")
    # shows the current updated scoreboard.
    play_count += 1
    # increment the play count by 1
    if play_count == play_count_request:
        # check to see if the play count has reached the requested play count.
        # if it hasn't, continue looping.
        # if it has, display the final scoreboard and end the game.
        print("---------------------------------------------------------")
        print("Your turns have ran out! ")
        # report that the player's requested turns have run out
        print("--------------------FINAL SCOREBOARD---------------------")
        print(user_name + ":" + str(user_score))
        print("MOUNTAIN DEW-BOT: " + str(computer_score))
        # displays the final scoreboard.
        if user_score > computer_score:
            print("Nice job, you've won!")
        if user_score < computer_score:
            print("You've lost, maybe try again next time? ")
        if user_score == computer_score:
            print("That's a tie! Well played!")
        # display the winner based on the final scoreboard.
        print("Thank you for playing Rock, Paper, Scissors! ")
        break
