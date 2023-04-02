# todo: Making random number 1 to 100 to guess
# todo: Make difficulty level choose easy = 10 attempts and hard = 5 attempts
# todo: Make funct that tell player that he/she bet to low or to high
# todo: If player don't guess his number of attempts decrease, after last try player lose
# todo: If player guess the number then win

import random

def randomizer():
    number = random.randint(1,100)
    return number
def checker(number,player_number):
    if number == player_number:
        print("yes!")
def player_guess():
    player_number = int(input(" Make a guess: "))
    return player_number
number = randomizer()
player_number = player_guess()
checker(number,player_number)