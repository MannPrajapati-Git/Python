# Project : number guessing game

import random
n = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 10.")
print("Try to guess it!")

while True:
    number = int(input("Enter a number between 1 and 10: "))
    if number < n:
        print("Your guess is too low. Try again!")
    elif number > n:
        print("Your guess is too high. Try again!")
    else:
        print("Congratulations! You guessed the number correctly!")
        break