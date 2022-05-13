"""
This code results in random Mega Sena game.
"""

from random import sample

number_of_games = int(input("Quantos jogos deseja jogar? "))
number_of_tens = int(input("Quantas dezenas por jogo (6 até 15)? "))

game_list = list()

while len(game_list) < number_of_games:
    jogo = sorted(list(sample(range(1, 61), number_of_tens)))
    game_list.append(jogo)

print()
print("-"*30)
print(f"{'MEGA SENA GAMES':^30}")
print("-"*30)

game_number = 0
for game in game_list:
    game_number += 1
    print(f"Game {game_number}: {game}")
