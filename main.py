# todo: Making random number 1 to 100 to guess
# todo: Make difficulty level choose easy = 10 attempts and hard = 5 attempts
# todo: Make funct that tell player that he/she bet to low or to high
# todo: If player don't guess his number of attempts decrease, after last try player lose
# todo: If player guess the number then win

import random

'''Welcome print's'''

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
'''GLOBAL VARIABLES '''
PLAYER_WON = False
NUMBER_RAND = random.randint(1, 100)

'''Store and return every iteration the same number which was choose ealier above.'''
def randomizer():
    global NUMBER_RAND
    number = NUMBER_RAND
    return number

'''Checking player number with choosed number and player life control with info about attempts left. Also return True to main game loop when player is ran out of lifes'''
def checker(number,player_number):
    global PLAYER_LIFE
    if player_number > number:
        print("Too high!")
        print("Guess again.")
        PLAYER_LIFE -= 1
        if PLAYER_LIFE == 0:
            print(f"You ran out of attempts! You LOSE! The number was {number}")
            return True
        print(f"You have {PLAYER_LIFE} attempts remaining to guess the number")
    elif player_number < number:
        print("Too low!")
        print("Guess again.")
        PLAYER_LIFE -= 1
        if PLAYER_LIFE == 0:
            print(f"You ran out of attempts! You LOSE! The number was {number}")
            return True
        print(f"You have {PLAYER_LIFE} attempts remaining to guess the number")
    elif player_number == number:
        print(f"You won ! The hidden number was {number}")
        return True

'''Global var PLAYER_WON store the boolean value for main game loop'''
def check_player_won(number,player_number):
    global PLAYER_WON
    PLAYER_WON = checker(number,player_number)

'''player_number store and catch every player guess and return to the main loop.'''
def player_guess():
    player_number = int(input(" Make a guess: "))
    return player_number

'''Catching and storing choosen diff level and decide which value will be in GLOBAL PLAYER_LIFE depends of level'''
difficulty_level = input("Choose a difficulty level! Type 'easy' or 'hard': ").lower()
if difficulty_level == "easy":
    PLAYER_LIFE = 10
    print(f"You have {PLAYER_LIFE} attempts at level EASY")
elif difficulty_level == "hard":
    PLAYER_LIFE = 5
    print(f"You have {PLAYER_LIFE} attempts at level HARD")
else:
    print("You write invalid syntax! Please restart game and type 'easy' or 'hard' ")

'''Main Game Loop with validation if PLAYER_WON is diff than False, and call the rest of funct'''
while not PLAYER_WON and difficulty_level == "easy" or difficulty_level == "hard":
    number = randomizer()
    player_number = player_guess()
    check_player_won(number,player_number)
