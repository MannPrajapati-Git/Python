# project : rock paper scissors game 
# uses function + random 

import random

def comp_choice():
    return random.choice(["rock", "paper", "scissors"])

def winner(user, comp):
    if user == comp:
        return "It's a tie!"
    elif (user == "rock" and comp == "scissors") or \
         (user == "paper" and comp == "rock") or \
         (user == "scissors" and comp == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    while True:
        user = input("Enter rock, paper, or scissors (or 'exit' to quit): ").lower()
        if user == "exit":
            print("Thanks for playing! Goodbye.")
            break
        elif user not in ["rock", "paper", "scissors"]:
            print("Invalid input. Try again.")
            continue
        
        comp = comp_choice()
        print("Computer chose:", comp)
        result = winner(user, comp)
        print(result)

play_game()
