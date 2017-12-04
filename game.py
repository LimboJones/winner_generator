import os
from random import randint
from time import sleep
from operator import itemgetter

def clear_console():
    os.system('cls')


players = [
            ["Ben", 0],
            ["Brian", 0],
            ["Dan", 0],
            ["Dima", 0],
            ["George", 0],
            ["James", 0],
            ["Liam", 0],
            ["Pippa", 0],
            ["Tim", 0]
]

game_over = False
winner = None

while not game_over:
    earner_index = randint(0, len(players) - 1)
    players[earner_index][1] += 1
    clear_console()
    for player in sorted(players, key=itemgetter(1), reverse=True):
        print player

    if players[earner_index][1] >= 100:
        winner = players[earner_index][0]
        game_over = True
    sleep(0.04)

print "\n{} wins!\n".format(winner)