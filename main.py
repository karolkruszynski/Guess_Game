# todo: Making random number 1 to 100 to guess
# todo: Make difficulty level choose easy = 10 attempts and hard = 5 attempts
# todo: Make funct that tell player that he/she bet to low or to high
# todo: If player don't guess his number of attempts decrease, after last try player lose
# todo: If player guess the number then win

import random
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
PLAYER_WON = False
# PLAYER_LIFE = 0
def randomizer():
    # number = random.randint(1,100)
    number = 10
    return number
def checker(number,player_number):
    global PLAYER_LIFE
    if player_number > number:
        print("Too high!")
        print("Guess again.")
        PLAYER_LIFE -= 1
        if PLAYER_LIFE == 0:
            print("You ran out of attempts! You LOST!")
            return True
        print(f"You have {PLAYER_LIFE} attempts remaining to guess the number")
    elif player_number < number:
        print("Too low!")
        print("Guess again.")
        PLAYER_LIFE -= 1
        if PLAYER_LIFE == 0:
            print("You ran out of attempts! You LOST!")
            return True
        print(f"You have {PLAYER_LIFE} attempts remaining to guess the number")
    elif player_number == number:
        print(f"You won ! The hidden number was {number}")
        return True
def check_player_won(number,player_number):
    global PLAYER_WON
    PLAYER_WON = checker(number,player_number)
def player_guess():
    player_number = int(input(" Make a guess: "))
    return player_number

difficulty_level = input("Choose a difficulty level! Type 'easy' or 'hard': ").lower()
if difficulty_level == "easy":
    PLAYER_LIFE = 10
elif difficulty_level == "hard":
    PLAYER_LIFE = 5
else:
    print("You write invalid syntax!")

while not PLAYER_WON:
    number = randomizer()
    player_number = player_guess()
    check_player_won(number,player_number)
