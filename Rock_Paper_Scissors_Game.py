# importing random, so that the computer can make random choices 
import random

# assigning variables so that the computer can choose randomly
choices = ["rock", "paper", "scissors"]

loop_end = ""

while loop_end != "quit":

    # asking the user for either rock, paper, or scissors
    while True:
        user_choice = input("Choose either rock, paper, or scissors: ").lower()
        if user_choice in choices:
            break
        print("Invalid choice, please try again.")

    # random.choices using the random function to choose one of the answers randomly
    computer_choice = random.choice(choices)    

    # simulate processing with delay
    for i in range(3):
        print("processing......")

    # wait for user to press any key to continue
    input("Press any key to continue: ")

    # comparing the choices and printing the result
    if user_choice == computer_choice:
        print("It is a draw")
    
    elif user_choice == "rock":
        if computer_choice == "paper":
            print("you lost")
        elif computer_choice == "scissors":
            print("you win")
    
    elif user_choice == "paper":
        if computer_choice == "scissors":
            print("you lost")
        elif computer_choice == "rock":
            print("you win")

    elif user_choice == "scissors":
        if computer_choice == "rock":
            print("you lost")
        elif computer_choice == "paper":
            print("you win")
            
    # this checks if the user wants to continue the loop
    loop_end = input("If you want to quit the program, type 'quit': ")
