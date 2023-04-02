# todo: Making random number 1 to 100 to guess
# todo: Make difficulty level choose easy = 10 attempts and hard = 5 attempts
# todo: Make funct that tell player that he/she bet to low or to high
# todo: If player don't guess his number of attempts decrease, after last try player lose
# todo: If player guess the number then win

import random
PLAYER_WON = False
def randomizer():
    # number = random.randint(1,100)
    number = 10
    return number
def checker(number,player_number):
    if player_number > number:
        print("Too high!")
    elif player_number < number:
        print("Too low!")
    elif player_number == number:
        print(f"You won ! The hidden number is {number}")
        return True
def check_player_won(number,player_number):
    global PLAYER_WON
    PLAYER_WON = checker(number,player_number)
def player_guess():
    player_number = int(input(" Make a guess: "))
    return player_number
while not PLAYER_WON:
    number = randomizer()
    player_number = player_guess()
    check_player_won(number,player_number)